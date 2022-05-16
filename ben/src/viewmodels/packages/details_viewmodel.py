from typing import List
from starlette.requests import Request
from viewmodels.shared.viewmodel import ViewModelBase
from src.services import package_service, user_service

class DetailsViewModel(ViewModelBase):
    def __init__(self, package_name: str, request: Request):
        super().__init__(request)

        self.package_name = package_name
        self.package = package_service.get_package_by_id(package_name)

        if not self.package:
            return
        self.x = 9