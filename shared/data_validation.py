"""
data validation
"""


def check_input(input_data, data_type, message=None, code=None):
    """
    check if input data_type is as expected while api call string is
    accepeted as unicode so we will check
    for unicode when string comes in picture

    """

    # if not isinstance(input_data, (data_type, str)):
    #     raise TypeError(message, code)
    print(type(input_data))
    if not isinstance(input_data, data_type):
        raise TypeError(message, code)
    return True


def validate_input(data, data_type, message, code):
    """
    check if input is not None and of required data_type
    """

    if not (data and (check_input(data, data_type, message, code))):
        raise TypeError(message, code)


def validate_parameter(str_input, message, code):
    """
    check if str_input is number only
    """
    try:
        int(str_input)
    except Exception as e:
        raise TypeError(message, code)