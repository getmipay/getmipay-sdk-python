import pytest

from getmipay.client import GetMiPay

from getmipay.exceptions import ValidationError


def test_payin_missing_amount():

    client = GetMiPay(
        api_key="test_key"
    )

    with pytest.raises(ValidationError):

        client.payments.payin({
            "amount": 5000,
            "currency": "XOF",
            "wallet": "+2250700000000",
            "customer_name": "John Doe",
            "customer_email": "john@example.com",
            "description": "Test payment",
            "callback_url": "https://example.com/webhook"
        })


def test_payin_missing_currency():

    client = GetMiPay(
        api_key="test_key"
    )

    with pytest.raises(ValidationError):

        client.payments.payin({
            "amount": 5000,
            "currency": "XOF",
            "wallet": "+2250700000000",
            "customer_name": "John Doe",
            "customer_email": "john@example.com",
            "description": "Test payment",
            "callback_url": "https://example.com/webhook"
        })


def test_payin_missing_wallet():

    client = GetMiPay(
        api_key="test_key"
    )

    with pytest.raises(ValidationError):

        client.payments.payin({
            "amount": 5000,
            "currency": "XOF",
            "wallet": "+2250700000000",
            "customer_name": "John Doe",
            "customer_email": "john@example.com",
            "description": "Test payment",
            "callback_url": "https://example.com/webhook"
        })


def test_payin_missing_callback_url():

    client = GetMiPay(
        api_key="test_key"
    )

    with pytest.raises(ValidationError):

        client.payments.payin({
            "amount": 5000,
            "currency": "XOF",
            "wallet": "+2250700000000",
            "customer_name": "John Doe",
            "customer_email": "john@example.com",
            "description": "Test payment",
            "callback_url": "https://example.com/webhook"
        })