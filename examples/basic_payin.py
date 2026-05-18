from getmipay import GetMiPay


mipay = GetMiPay(
    api_key="mipay_xxxxxxxxxxxxx",
    environment="production"
)

try:

    payment = mipay.payments.payin({
        "amount": 1000,
        "currency": "XAF",
        "wallet": "690000000",
        "service": "MTN",
        "customer_name": "John Doe",
        "customer_email": "john@example.com",
        "description": "Payment for Order #123",
        "callback_url": "https://yourapp.com/webhooks/payment"
    })

    print(payment)

except Exception as e:

    print("ERROR:", e)
