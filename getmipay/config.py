from dataclasses import dataclass

@dataclass
class Config:
    api_key: str = ""
    environment: str = "sandbox"
    timeout: int = 30

    BASE_URLS = {
        "sandbox": "https://sandbox.getmipay.com/v1",
        "production": "https://getmipay.com/api/v1"
    }

    def __post_init__(self):
        if not self.api_key:
            raise ValueError("API key is required")

        if self.environment not in self.BASE_URLS:
            raise ValueError("Invalid environment")

    @property
    def base_url(self):
        return self.BASE_URLS[self.environment]
