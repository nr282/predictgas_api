"""
PredictGas is an application that provides state-by-state prediction/estimation
of Natural Gas Consumption.

The code provided here calls the PredictGas API in a parallel fashion. The function that
does this parallelization is called "concurrent_request_execution".

This allows for our clients to easily parallelize their usage of our API.

"""

import requests
import json
import pandas as pd
import time
from requests_futures.sessions import FuturesSession
import logging



if __name__ == "__main__":

    url = "https://predictgas-671385643237.us-east4.run.app"
    content_type = "application/json"
    auth = ""
    payload = {
        "start_date": "2009-01-01",
        "end_date": "2025-09-30",
        "current_date": "2025-09-30",
        "state": "Virginia"
    }

    headers = {"Content-Type": "application/json"}

    for i in range(5):
        response = requests.get(url, headers=headers, params=payload)
        df = pd.DataFrame.from_dict(response.json())
        print(df.head())


