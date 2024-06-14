# This file was auto-generated by Fern from our API Definition.

from ....core.exceptions.fern_http_exception import FernHTTPException
from ..types.internal_server_error_body import InternalServerErrorBody


class InternalServerError(FernHTTPException):
    def __init__(self, error: InternalServerErrorBody):
        super().__init__(status_code=500, name="InternalServerError", content=error)
