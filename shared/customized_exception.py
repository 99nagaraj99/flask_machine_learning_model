"""
contains all customised exception
"""


class InternalError(Exception):
    """
    raised for db or calculation related problems
    """

    def __init__(self, message, code):
        self.message = message
        self.code = code

    def __str__(self):
        return repr(self.message), repr(self.code)

