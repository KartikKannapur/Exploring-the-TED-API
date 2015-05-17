__author__ = "Kartik Kannapur"
__date__ = "17.05.2015"

#Import Files
import TED_Private_API as TED_Private_API

#Import Python Libraries
import requests


#Parameters
api_key = TED_Private_API.Private_Key
api_endpoint_url = "http://api.ted.com"
api_endpoint_version = "/v1"

api_endpoint = api_endpoint_url + api_endpoint_version



if __name__ == "__main__":
    mainFunction()