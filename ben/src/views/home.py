from fastapi import APIRouter
# from ..core.utils import template
from fastapi_chameleon import template
from starlette.requests import Request

from ben.src.viewmodels.home.index_viewmodel import IndexViewModel
from src.viewmodels.shared.viewmodel import ViewModelBase

router = APIRouter()


@router.get('/')
@template('home/index.pt')
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()
    # return template(request, 'home/index.j2', data)


@router.get('/about')
@template('home/about.pt')
def about(request: Request):
    vm = ViewModelBase(request)
    # TODO: Use the vm.
    return {}
    # return template(request, 'home/about.j2')