"""
API for authentication validation
"""
from flask import request
from flask_restful import Resource
from flask_restful_swagger_2 import swagger
from operations.neural_network.xor.xor_pred import predict_xor_output
from flask_api import status
from shared.internal_status import StatusCodes as SC, ErrorMessages as EM
from shared.responses import get_response
from shared.customized_exception import InternalError


class XorPredNn(Resource):
    """
    API for authentication validation
    """
    # @swagger.operation(notes='Some really good newa')
    @swagger.doc({
        'tags': ['Xor'],
        'description': 'Predict Xor Using NN',
        "parameters": [
            {
                "in": "header",
                "name": "Authorisation",
                "type": "string",
                "required": True,
                "default": "abcdefg"
            }
        ],
        'responses': {
            '200': {
                'description': 'auth',
                'examples': {
                    'application/json': {
                        "data": {
                            "output_prediction_of_xor": 1
                        },
                        "code": 2000,
                        "success": True,
                        "message": "operation successful"
                    }
                }
            },
            '401': {
                'description': 'Unauthorized',
                'examples': {
                    'application/json': {
                        "data": "No data found",
                        "code": 2001,
                        "success": False,
                        "message": "'Invalid value'"
                    }
                }
            }
        }
    })
    def get(self):
        """
        authentication validation
        :return:
        """
        try:
            num1, num2 = self.validate_path_parameter()
            res = predict_xor_output(num1, num2)
            return get_response(data=res, code=2000)
        except InternalError as message:
            # logger.error("error is %s", str(message.message))
            return get_response(message=str(message.message),
                                code=int(message.code.value),
                                success=False), status.HTTP_500_INTERNAL_SERVER_ERROR
        except Exception as ex:
            # logger.error("error is %s", str(ex))
            return get_response(message=str(EM.IM_5000_INTERNAL_ERROR),
                                code=str(SC.IC_5000_INTERNAL_ERROR),
                                success=False), \
                   status.HTTP_500_INTERNAL_SERVER_ERROR

    def validate_path_parameter(self):
        """Validating path parameters"""
        try:
            num1 = int(request.args.get('x1'))
            num2 = int(request.args.get('x2'))
        except Exception:
            raise InternalError(message=EM.IM_2001_INVALID_VALUE, code=SC.IC_2001_INVALID_VALUE)
        if not (num1 in [0, 1] and num2 in [0, 1]):
            raise InternalError(message=EM.IM_2001_INVALID_VALUE, code=SC.IC_2001_INVALID_VALUE)
        return num1, num2
