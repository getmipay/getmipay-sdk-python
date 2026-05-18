from typing import Dict, Any

from ..http_client import HttpClient
from ..auth import Signature
from ..exceptions import (
    ValidationError,
    ApiError
)


class Payments:
    PAYIN_OPERATION = "2"
    SERVICES = {
        "MTN": "1",
        "ORANGE": "2",
    }

    def __init__(self, config):

        self.config = config
        self.http = HttpClient(config)

    def payin(
        self,
        params: Dict[str, Any]
    ) -> Dict[str, Any]:

        """
        Initiate a PayIn transaction
        """

        required_fields = [
            "amount",
            "currency",
            "wallet",
            "service",
            "callback_url"
        ]

        for field in required_fields:

            if field not in params:

                raise ValidationError(
                    f"Missing required field: {field}"
                )

        service = self._resolve_service(params["service"])

        payload = {
            "amount": params["amount"],
            "currency": params["currency"],
            "wallet": params["wallet"],
            "customer_name": params.get(
                "customer_name",
                ""
            ),
            "customer_email": params.get(
                "customer_email",
                ""
            ),
            "description": params.get(
                "description",
                ""
            ),
            "callback_url": params["callback_url"]
        }

        path = "/payments/payin"
        method = "POST"

        headers = Signature.get_headers(
            self.config.api_key,
            method,
            path,
            payload
        )
        headers.update({
            "operation": self.PAYIN_OPERATION,
            "service": service,
        })

        try:

            response = self.http.post(
                path,
                payload,
                headers
            )

            return response

        except Exception as e:

            raise ApiError(str(e))

    def _resolve_service(self, service: Any) -> str:
        service_key = str(service).strip().upper()

        if service_key in self.SERVICES:
            return self.SERVICES[service_key]

        if service_key in self.SERVICES.values():
            return service_key

        raise ValidationError(
            "Invalid service. Use 'MTN'/'1' or 'Orange'/'2'."
        )

    def direct_status(
        self,
        params: Dict[str, Any]
    ) -> Dict[str, Any]:

        """
        Check payment status using order and payment identifiers.
        """

        required_fields = [
            "order_id",
            "pay_id",
            "service"
        ]

        for field in required_fields:

            if field not in params:

                raise ValidationError(
                    f"Missing required field: {field}"
                )

        payload = {
            "order_id": params["order_id"],
            "pay_id": params["pay_id"],
            "operation": str(params.get(
                "operation",
                self.PAYIN_OPERATION
            )),
            "service": self._resolve_service(params["service"])
        }

        path = "/payments/direct-status"
        method = "POST"

        headers = Signature.get_headers(
            self.config.api_key,
            method,
            path,
            payload
        )

        try:

            response = self.http.post(
                path,
                payload,
                headers
            )

            return response

        except Exception as e:

            raise ApiError(str(e))

    def get_status(
        self,
        reference: str
    ) -> Dict[str, Any]:

        """
        Get payment status
        """

        path = f"/payments/{reference}/status"

        method = "GET"

        headers = Signature.get_headers(
            self.config.api_key,
            method,
            path
        )

        try:

            response = self.http.get(
                path,
                headers
            )

            return response

        except Exception as e:

            raise ApiError(str(e))
