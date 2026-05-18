from .config import Config
from .services.payments import Payments

class GetMiPay:

    def __init__(self, api_key, environment="production"):

        self.config = Config(
            api_key=api_key,
            environment=environment
        )

        self.payments = Payments(self.config)