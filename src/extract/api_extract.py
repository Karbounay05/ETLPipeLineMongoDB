import requests
import pandas as pd

def extract_api():

    url="https://jsonplaceholder.typicode.com/users"

    data=requests.get(url).json()

    return pd.DataFrame(data)