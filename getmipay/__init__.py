from .client import GetMiPay
from .exceptions import (
    GetMiPayError,
    ValidationError,
    AuthenticationError,
    ApiError,
    NetworkError
)

__version__ = "1.0.0"
__all__ = [
    "GetMiPay",
    "GetMiPayError",
    "ValidationError",
    "AuthenticationError",
    "ApiError",
    "NetworkError"
]
from getmipay import GetMiPay

client = GetMiPay(
    api_key="test_key"
)

print(client.config.base_url)