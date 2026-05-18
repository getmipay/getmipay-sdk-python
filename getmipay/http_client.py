import requests

from .exceptions import ApiError, NetworkError

class HttpClient:

    def __init__(self, config):
        self.config = config

    def post(self, path, payload, headers):

        url = self.config.base_url + path

        try:
            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=self.config.timeout
            )

            return self._handle_response(response)

        except requests.RequestException as e:
            raise NetworkError(str(e))

    def get(self, path, headers):

        url = self.config.base_url + path

        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=self.config.timeout
            )

            return self._handle_response(response)

        except requests.RequestException as e:
            raise NetworkError(str(e))

    def _handle_response(self, response):

        try:
            data = response.json()
        except:
            data = response.text

        if response.status_code >= 400:
            raise ApiError(
                str(data),
                response.status_code
            )

        return data