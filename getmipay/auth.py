import hashlib
import hmac
import time
import json

class Signature:

    @staticmethod
    def generate(api_key, method, path, timestamp, body=""):

        string_to_sign = f"{method}\n{path}\n{timestamp}\n{body}"

        return hmac.new(
            api_key.encode(),
            string_to_sign.encode(),
            hashlib.sha256
        ).hexdigest()

    @staticmethod
    def get_headers(api_key, method, path, body=None):

        timestamp = str(int(time.time()))

        body_str = json.dumps(body) if body else ""

        signature = Signature.generate(
            api_key,
            method,
            path,
            timestamp,
            body_str
        )

        return {
            "X-API-KEY": api_key,
            "x-timestamp": timestamp,
            "x-signature": signature,
            "Content-Type": "application/json",
            "x-sdk-version": "1.0.0",
            "x-sdk-language": "python"
        }
