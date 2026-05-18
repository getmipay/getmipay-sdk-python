import pytest

from getmipay.client import GetMiPay

from getmipay.exceptions import ValidationError


class FakeHttp:

    def __init__(self):

        self.headers = None

    def post(self, path, payload, headers):

        self.headers = headers

        return {
            "path": path,
            "payload": payload
        }


def test_payin_missing_amount():

    client = GetMiPay(
        api_key="test_key"
    )

    with pytest.raises(ValidationError):

        client.payments.payin({
            "currency": "XOF",
            "wallet": "+2250700000000",
            "service": "MTN",
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
            "wallet": "+2250700000000",
            "service": "MTN",
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
            "service": "MTN",
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
            "service": "MTN",
            "customer_name": "John Doe",
            "customer_email": "john@example.com",
            "description": "Test payment",
        })


def test_payin_missing_service():

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


def test_resolve_named_payin_service():

    client = GetMiPay(
        api_key="test_key"
    )

    assert client.payments._resolve_service("MTN") == "1"
    assert client.payments._resolve_service("Orange") == "2"
    assert client.payments._resolve_service(1) == "1"


def test_resolve_invalid_payin_service():

    client = GetMiPay(
        api_key="test_key"
    )

    with pytest.raises(ValidationError):

        client.payments._resolve_service("Moov")


def test_payin_sends_operation_and_service_headers():

    client = GetMiPay(
        api_key="test_key"
    )
    fake_http = FakeHttp()
    client.payments.http = fake_http

    response = client.payments.payin({
        "amount": 1000,
        "currency": "XAF",
        "wallet": "690000000",
        "service": "Orange",
        "customer_name": "John Doe",
        "customer_email": "john@example.com",
        "description": "Payment for Order #123",
        "callback_url": "https://yourapp.com/webhooks/payment"
    })

    assert response["path"] == "/payments/payin"
    assert fake_http.headers["operation"] == "2"
    assert fake_http.headers["service"] == "2"
    assert fake_http.headers["X-API-KEY"] == "test_key"


def test_direct_status_sends_required_payload():

    client = GetMiPay(
        api_key="test_key"
    )
    fake_http = FakeHttp()
    client.payments.http = fake_http

    response = client.payments.direct_status({
        "order_id": "MPAYIN_ABC123DEF456",
        "pay_id": "MLS690d472dd7ee7B",
        "service": "MTN"
    })

    assert response["path"] == "/payments/direct-status"
    assert response["payload"] == {
        "order_id": "MPAYIN_ABC123DEF456",
        "pay_id": "MLS690d472dd7ee7B",
        "operation": "2",
        "service": "1"
    }
    assert fake_http.headers["X-API-KEY"] == "test_key"


def test_direct_status_missing_pay_id():

    client = GetMiPay(
        api_key="test_key"
    )

    with pytest.raises(ValidationError):

        client.payments.direct_status({
            "order_id": "MPAYIN_ABC123DEF456",
            "service": "MTN"
        })
