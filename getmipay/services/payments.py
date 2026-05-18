from typing import Dict, Any

from ..http_client import HttpClient
from ..auth import Signature
from ..exceptions import (
    ValidationError,
    ApiError
)


class Payments:

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
            "callback_url"
        ]

        for field in required_fields:

            if field not in params:

                raise ValidationError(
                    f"Missing required field: {field}"
                )

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
