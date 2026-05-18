from dataclasses import dataclass
from typing import Optional


@dataclass
class Payment:
    """
    Represents a payment transaction.
    """

    reference: str
    status: str
    amount: float
    currency: str
    wallet: str

    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    description: Optional[str] = None

    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    provider: Optional[str] = None
    transaction_id: Optional[str] = None

    def to_dict(self) -> dict:
        """
        Convert Payment object to dictionary.
        """
        return {
            "reference": self.reference,
            "status": self.status,
            "amount": self.amount,
            "currency": self.currency,
            "wallet": self.wallet,
            "customer_name": self.customer_name,
            "customer_email": self.customer_email,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "provider": self.provider,
            "transaction_id": self.transaction_id,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create Payment object from API response.
        """
        return cls(
            reference=data.get("reference", ""),
            status=data.get("status", ""),
            amount=data.get("amount", 0),
            currency=data.get("currency", ""),
            wallet=data.get("wallet", ""),
            customer_name=data.get("customer_name"),
            customer_email=data.get("customer_email"),
            description=data.get("description"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
            provider=data.get("provider"),
            transaction_id=data.get("transaction_id"),
        )