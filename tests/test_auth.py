from getmipay.auth import Signature


def test_generate_signature():

    api_key = "test_key"

    method = "POST"

    path = "/payments/payin"

    timestamp = "1234567890"

    body = '{"amount":5000}'

    signature = Signature.generate(
        api_key,
        method,
        path,
        timestamp,
        body
    )

    assert signature is not None

    assert isinstance(signature, str)

    assert len(signature) == 64


def test_get_headers():

    headers = Signature.get_headers(
        api_key="test_key",
        method="POST",
        path="/payments/payin",
        body={"amount": 5000}
    )

    assert "X-API-KEY" in headers

    assert "x-signature" in headers

    assert "x-timestamp" in headers

    assert headers["Content-Type"] == "application/json"
