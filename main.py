__author__ = "Kartik Kannapur"
__date__ = "24.06.2015"

#Import Files
import TED_Private_API as TED_Private_API

#Import Python Libraries
import requests


#Parameters
api_key = TED_Private_API.Private_Key
api_endpoint_url = "https://api.ted.com"
api_endpoint_version = "/v1/"

json_paramater = "countries"

api_endpoint = api_endpoint_url + api_endpoint_version + json_paramater + ".json?api-key=" + api_key


def main_function():
    # print api_endpoint
    response_countries = requests.get(api_endpoint)
    print response_countries.content
    


if __name__ == "__main__":
    main_function()
