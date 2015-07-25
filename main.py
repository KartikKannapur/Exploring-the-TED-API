__author__ = "Kartik Kannapur"
__date__ = "25.07.2015"

#Import Files
import TED_Private_API as TED_Private_API

#Import Python Libraries
import requests
import json


class TEDAPI(object):
    """
    This class contains multiple functions that return the list of countries,
    ratings of each talk.
    """

    def __init__(self):
        print "----- TED API -----"
        self.api_key = TED_Private_API.Private_Key
        self.api_endpoint_url = "https://api.ted.com"
        self.api_endpoint_version = "/v1/"


    def get_countries(self):
        self.api_endpoint = self.api_endpoint_url + self.api_endpoint_version + "countries" + ".json?api-key=" + \
                       self.api_key

        self.response_countries = requests.get(self.api_endpoint)
        self.countries_json = json.loads(self.response_countries.content)
        print self.countries_json['states']
        print "Total Number of Countries: " + str(self.countries_json['counts'])


    def get_talk_ratings(self):
        """
        This function returns the ratings for each talk with the following parameters -
        ratingid, rating, talkid, ratingwordid and name
        """
        self.api_endpoint = self.api_endpoint_url + self.api_endpoint_version + "ratings" + ".json?api-key=" + \
                       self.api_key

        self.response_talk_ratings = requests.get(self.api_endpoint)
        self.talk_ratings_json = json.loads(self.response_talk_ratings)
        print self.talk_ratings_json

if __name__ == "__main__":
    my_ted_api_instance = TEDAPI()
    # my_ted_api_instance.get_countries()