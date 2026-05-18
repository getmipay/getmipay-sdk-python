from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class ApiResponse:
    """
    Standard API response object.
    """

    success: bool
    message: str
    data: Optional[Any] = None
    status_code: Optional[int] = None

    def to_dict(self) -> dict:
        """
        Convert response object to dictionary.
        """
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data,
            "status_code": self.status_code,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create ApiResponse object from dictionary.
        """
        return cls(
            success=data.get("success", False),
            message=data.get("message", ""),
            data=data.get("data"),
            status_code=data.get("status_code"),
        )