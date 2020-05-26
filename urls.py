"""
Contains the url mapping to the respective resources
"""
from resources.xor_predict import XorPredNn
from resources.welcome import Welcome


def pages(api):
    """
    This contains the urls for all the pages
    :param api: Flask-restful api object
    :return: None
    """
    # Used to check if API is up
    api.add_resource(Welcome, '/')
    api.add_resource(XorPredNn, '/api/v1/xor_prediction')

