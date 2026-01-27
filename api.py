
"""
Module focuses on calling the relevant API.
"""

import requests
import json
import pandas as pd
import time
from requests_futures.sessions import FuturesSession
import logging

def call_predict_gas_api(link):

    result = requests.get(link)
    status_code = result.status_code
    return result.json(), result.status_code



def get_request_with_authentication(state: str,
                                    start_date: str,
                                    end_date: str,
                                    component_type: str = "residential"):

    api_key = "1ocgRB9yyf0QBhis3R3T3f8Rp2J0raO2OLxgSnI5"  #API Key Used for authentication.
    headers = {'x-api-key': api_key,
               'start_date': start_date,
               'end_date': end_date,
               'state': state,
               'component_type': component_type
               }

    request_string = "https://7hebop3w6c.execute-api.us-east-2.amazonaws.com/default/predictgas"
    return request_string, headers


def test_api_gateway(request_string, headers, result=None):

    if result is None:
        try:
            result = requests.get(request_string, headers=headers)
        except Exception as error:
            raise RuntimeError(error)

    status = "Success"
    if not result.ok:
        message_dict = json.loads(result.text)
        message = message_dict['message']
        if message == 'Missing Authentication Token':
            status = """Failure in the API Gateway. There is a missing Authentication Token. 
                               To get a Authentication token, please contact nr282@cornell.edu, if you are
                               entitled to the token. Need to make sure that the request has the relevant
                               headers"""
        if message == "Internal server error":
            status = """Internal Service Error was found. The issue is with the server not the client.
                               The client has the correct authentication key, but server is not working properly.
                               Please contact nr282@cornell.edu for maintenance."""
        if message == "Forbidden":
            status = """API Key exists, but is incorrect."""
    else:
        status = "Success"

    try:
        df = pd.DataFrame.from_dict(json.loads(result.text))
    except:
        df = None

    return df, status

def test_concurrent_request_execution(state: str,
                                      start_date: str,
                                      end_date: str,
                                      component_type: str = "residential"):

    logging.basicConfig(level=logging.DEBUG)
    session = FuturesSession()
    request_string, headers = get_request_with_authentication(state,
                                                              start_date,
                                                              end_date,
                                                              component_type)

    results = []
    for i in range(20):
        start = time.time()
        future_result = session.get(request_string, headers=headers)
        results.append(future_result)
        end = time.time()
        print(f"Time taken to call API Gateway: {end - start}")


    for future_result in results:
        response = future_result.result()
        result, status_code = test_api_gateway(response.text, headers, result=response)
        assert(status_code, "Success")

    return result



def get_state_gas_consumption(state: str,
                              start_date: str,
                              end_date: str):


    component_type = "residential"
    result = test_concurrent_request_execution(state,
                                               start_date,
                                               end_date,
                                               component_type)
    return result




if __name__ == "__main__":



    state = "Virginia"
    start_date = "2021-01-01"
    end_date = "2027-12-31"

    get_state_gas_consumption(state, start_date, end_date)
