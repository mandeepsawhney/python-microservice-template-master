from werkzeug.exceptions import HTTPException

BAD_REQUEST_STATUS_CODE = 400
CONFLICT_STATUS_CODE = 409
INTERNAL_SERVER_ERROR_STATUS_CODE = 500
NOT_FOUND_STATUS_CODE = 404
NOT_IMPLEMENTED_STATUS_CODE = 501
UNPROCESSABLE_ENTITY_STATUS_CODE = 422


class BadRequest(HTTPException):
    code = BAD_REQUEST_STATUS_CODE
    message = 'Bad Request'


class Conflict(HTTPException):
    code = CONFLICT_STATUS_CODE
    message = 'Conflict'


class InternalServerError(HTTPException):
    code = INTERNAL_SERVER_ERROR_STATUS_CODE
    message = 'Internal Server Error'


class NotFound(HTTPException):
    code = NOT_FOUND_STATUS_CODE


class NotImplemented(HTTPException):
    code = NOT_IMPLEMENTED_STATUS_CODE
    message = 'Not Implemented'


class UnprocessableEntity(HTTPException):
    code = UNPROCESSABLE_ENTITY_STATUS_CODE
    message = 'Unprocessable Entity'
