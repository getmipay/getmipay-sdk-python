import re
from urllib.parse import urlparse

from ..exceptions import ValidationError


SUPPORTED_CURRENCIES = [
    "XAF",
    "XOF",
    "USD",
    "EUR",
]


def validate_amount(amount):
    """
    Validate payment amount.
    """

    if amount is None:
        raise ValidationError("Amount is required")

    if not isinstance(amount, (int, float)):
        raise ValidationError("Amount must be a number")

    if amount <= 0:
        raise ValidationError("Amount must be greater than zero")


def validate_currency(currency):
    """
    Validate currency code.
    """

    if not currency:
        raise ValidationError("Currency is required")

    if currency not in SUPPORTED_CURRENCIES:
        raise ValidationError(
            f"Unsupported currency: {currency}"
        )


def validate_wallet(wallet):
    """
    Validate mobile money wallet number.
    """

    if not wallet:
        raise ValidationError("Wallet number is required")

    pattern = r"^\+?[1-9]\d{7,14}$"

    if not re.match(pattern, wallet):
        raise ValidationError(
            "Invalid wallet phone number format"
        )


def validate_email(email):
    """
    Validate email format.
    """

    if not email:
        return

    pattern = r"^[^@]+@[^@]+\.[^@]+$"

    if not re.match(pattern, email):
        raise ValidationError(
            "Invalid email address"
        )


def validate_callback_url(url):
    """
    Validate callback URL.
    """

    if not url:
        raise ValidationError(
            "Callback URL is required"
        )

    parsed = urlparse(url)

    if parsed.scheme not in ["http", "https"]:
        raise ValidationError(
            "Callback URL must start with http:// or https://"
        )

    if not parsed.netloc:
        raise ValidationError(
            "Invalid callback URL"
        )