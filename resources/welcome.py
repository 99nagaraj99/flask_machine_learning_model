"""
API for authentication validation
"""
from flask import request
from flask_restful import Resource
from flask_restful_swagger_2 import swagger
from operations.neural_network.xor.xor_pred import predict_xor_output
# from flask_api import status
# from shared.user_validation import authenticate
# from shared.internal_status import StatusCodes as SC, ErrorMessages as EM
from shared.responses import get_response
# from shared.customized_exception import AuthorizationException, PACException
# from log import logger


class Welcome(Resource):
    """
    API for authentication validation
    """
    # @swagger.doc({
    #     'tags': ['Hierarchy'],
    #     'description': 'Authentication validate',
    #     "parameters": [
    #         {
    #             "in": "header",
    #             "name": "Authorisation",
    #             "type": "string",
    #             "required": True,
    #             "default": "abcdefg"
    #         }
    #     ],
    #     'responses': {
    #         '200': {
    #             'description': 'auth',
    #             'examples': {
    #                 'application/json': {
    #                     "message": "operation successful",
    #                     "code": 2000,
    #                     "data": "No data found",
    #                     "success": True
    #                 }
    #             }
    #         },
    #         '401': {
    #             'description': 'Unauthorized',
    #             'examples': {
    #                 'application/json': {
    #                     "success": False,
    #                     "data": "Not Available",
    #                     "message": "Unauthorized Key",
    #                     "code": 4421
    #                 }
    #             }
    #         }
    #     }
    # })
    def get(self):
        """
        authentication validation
        :return:
        """
        try:
            res = "Welcome to Machine Learning Prediction Application"
            return get_response(data=res, code=2000)
        # except:
        #     res = {
        #         'success': False,
        #         'message': 'Unknown error'
        #     }
        # return res
        # logger.info("success")

        # except PACException as message:
        #     internal_message = message.message
        #     logger.error("error is %s", internal_message)
        #     return get_response(message=internal_message['message'],
        #                         code=internal_message['code'],
        #                         data={"error": internal_message['error']},
        #                         success=False), message.code
        # except AuthorizationException as message:
        #     logger.error("error is %s", str(message.message))
        #     return get_response(message=str(message.message),
        #                         code=int(message.code.value),
        #                         success=False), status.HTTP_401_UNAUTHORIZED
        except Exception as err:
            # logger.error("error is %s", _)
            return get_response(message=err.message, success=False)

