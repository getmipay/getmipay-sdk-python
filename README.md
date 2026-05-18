# GetMiPay Python SDK

## Pay-in

```python
from getmipay import GetMiPay

mipay = GetMiPay(
    api_key="mipay_xxxxxxxxxxxxx",
    environment="production",
)

payment = mipay.payments.payin({
    "amount": 1000,
    "currency": "XAF",
    "wallet": "690000000",
    "service": "MTN",
    "description": "Payment for Order #123",
    "customer_name": "John Doe",
    "customer_email": "john@example.com",
    "callback_url": "https://yourapp.com/webhooks/payment",
})
```

Pay-in requests are sent to `/payments/payin` with `operation: 2`.

Service values:

- `MTN` or `1`
- `Orange` or `2`

## Direct Status

```python
status = mipay.payments.direct_status({
    "order_id": "MPAYIN_ABC123DEF456",
    "pay_id": "MLS690d472dd7ee7B",
    "service": "MTN",
})
```

Direct status requests are sent to `/payments/direct-status` with this JSON body:

```json
{
  "order_id": "MPAYIN_ABC123DEF456",
  "pay_id": "MLS690d472dd7ee7B",
  "operation": "2",
  "service": "1"
}
```
