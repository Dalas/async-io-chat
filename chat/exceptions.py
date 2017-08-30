

class BaseResponseException(Exception):
    status = 500
    error = {
        'code': None,
        'message': 'Internal server error!'
    }

    def __init__(self, message=None):
        if message:
            self.error['message'] = message


class BadRequest(BaseResponseException):
    status = 400
    error = {
        'code': 1001,
        'message': 'Bad request!'
    }


class ExternalServiceError(BaseResponseException):
    status = 503
    error = {
        'code': 1002,
        'message': 'External service error!'
    }