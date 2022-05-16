from typing import Optional
from src.data.package import Package


def release_count() -> int:
    return 2_234_847


def package_count() -> int:
    return 274_000


def latest_packages(limit: int = 5) -> list:
    return [
        {'id': 'fastapi', 'summary': "A great web framework"},
        {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
        {'id': 'httpx', 'summary': "Requests for an async world"},
    ][:limit]


def get_package_by_id(package_name: str) -> Optional[Package]:
    return None