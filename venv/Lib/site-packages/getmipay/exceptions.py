class GetMiPayError(Exception):
    pass

class ValidationError(GetMiPayError):
    pass

class AuthenticationError(GetMiPayError):
    pass

class ApiError(GetMiPayError):

    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code

class NetworkError(GetMiPayError):
    pass
