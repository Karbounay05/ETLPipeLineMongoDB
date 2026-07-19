import requests
import pandas as pd
from config import REQRES_API_KEY

API_URL = "https://reqres.in/api/users?page=1"

def extract_api_data():
    headers = {
        "x-api-key": REQRES_API_KEY,
        "Accept": "application/json"
    }

    response = requests.get(API_URL, headers=headers)

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code != 200:
        return pd.DataFrame()

    data = response.json()["data"]
    return pd.DataFrame(data)