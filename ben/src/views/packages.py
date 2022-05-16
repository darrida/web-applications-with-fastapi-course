from fastapi import Request, APIRouter
# from ..core.utils import template
from fastapi_chameleon import template
from starlette.requests import Request
from src.viewmodels.packages.details_viewmodel import DetailsViewModel

router = APIRouter()


@router.get('/project/{packge_name}')
@template('packages/details.pt')
def details(package_name: str, request: Request):
    vm = DetailsViewModel(package_name, request)
    return vm.to_dict()