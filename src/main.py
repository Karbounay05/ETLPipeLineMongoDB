from pymongo import MongoClient

from config import MONGO_URI, DATABASE_NAME
from extract.api_extract import extract_api_data
from extract.csv_extract import extract_csv_data
from extract.sqlite_extract import extract_sqlite_data
from src.extract.json_extract import extract_json_data

from transform.transform import clean_dataframe

from load.mongo_loader import load_to_mongo
from load.logger import log_pipeline


def main():
    try:
        # Connect to MongoDB
        client = MongoClient(MONGO_URI)
        client.admin.command("ping")

        print("✅ Connected to MongoDB!")

        db = client[DATABASE_NAME]

        print(f"Database: {DATABASE_NAME}")
        print("Collections:", db.list_collection_names())

        # -------------------------
        # Extract
        # -------------------------
        api_df = extract_api_data()
        sales_df = extract_csv_data()
        employee_df = extract_sqlite_data()

        # -------------------------
        # Transform
        # -------------------------
        api_df = clean_dataframe(api_df)
        sales_df = clean_dataframe(sales_df)
        employee_df = clean_dataframe(employee_df)

        # -------------------------
        # Load
        # -------------------------
        # Load original collections
        load_to_mongo(api_df, "users")
        load_to_mongo(sales_df, "sales")
        load_to_mongo(employee_df, "employees")

        #----
        products_df = clean_dataframe(
            extract_json_data("data/products.json")
        )

        stores_df = clean_dataframe(
            extract_json_data("data/stores.json")
        )

        categories_df = clean_dataframe(
            extract_json_data("data/categories.json")
        )

        suppliers_df = clean_dataframe(
            extract_json_data("data/suppliers.json")
        )

        load_to_mongo(products_df, "products")
        load_to_mongo(stores_df, "stores")
        load_to_mongo(categories_df, "categories")
        load_to_mongo(suppliers_df, "suppliers")
        # -------------------------
        # Create Unified Warehouse
        # -------------------------

        warehouse_df = sales_df.merge(
            api_df,
            left_on="customer_id",
            right_on="id",
            how="inner"
        )

        warehouse_df = warehouse_df.merge(
            employee_df,
            on="id",
            how="inner"
        )

        load_to_mongo(warehouse_df, "warehouse")

        print(f"Loaded {len(warehouse_df)} records into warehouse")

        total_records = (
                len(api_df)
                + len(sales_df)
                + len(employee_df)
                + len(warehouse_df)
        )
        log_pipeline(
            status="SUCCESS",
            records=total_records,
            message="Pipeline executed successfully."
        )

        print(f"\n✅ ETL Pipeline completed successfully!")
        print(f"Total records processed: {total_records}")

    except Exception as e:
        print(f"\n❌ Pipeline failed: {e}")

        log_pipeline(
            status="FAILED",
            records=0,
            message=str(e)
        )


if __name__ == "__main__":
    main()

