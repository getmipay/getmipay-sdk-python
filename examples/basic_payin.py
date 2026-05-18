from getmipay import GetMiPay


mipay = GetMiPay(
    api_key="gmp_sk_test_xxxxxxxxx",
    environment="sandbox"
)

try:

    payment = mipay.payments.payin({
        "amount": 5000,
        "currency": "XOF",
        "wallet": "+2250700000000",
        "customer_name": "John Doe",
        "customer_email": "john@example.com",
        "description": "Test payment",
        "callback_url": "https://example.com/webhook"
    })

    print(payment)

except Exception as e:

    print("ERROR:", e)