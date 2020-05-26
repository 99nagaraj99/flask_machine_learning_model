"""
for running the application
"""
from flask import Flask
from flask_restful_swagger_2 import Api, swagger
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

# from db import db, USERNAME, PASSWORD, HOST, DATABASE
from urls import pages
from log import logger
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app)

api = Api(app, api_version='0.1', api_spec_url='/api/swagger', consumes=['application/json'],
          produces=['application/json'], host='AWS_HOST', schemes=['http'], base_path='',
          title='Trail', description='This app is use to get machine learning model prediction')
# api = swagger.docs(Api(app), apiVersion='0.1', api_spec_url='/api/swagger')

# ## swagger specific ##############################################
# SWAGGER_URL = '/api/swagger'
# API_URL = '/static/swagger.json'
# SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config={
#         'app_name': "Trail"
#     }
# )
# app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
# ##################################################################
pages(api)
if __name__ == '__main__':
    app.run(debug=True)
