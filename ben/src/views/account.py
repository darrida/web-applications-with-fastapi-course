from fastapi import Request, APIRouter
# from ..core.utils import template
from fastapi_chameleon import template
from src.viewmodels.account.account_viewmodel import AccountViewModel
from src.viewmodels.account.login_viewmodel import LoginViewModel
from src.viewmodels.account.register_viewmodel import RegisterViewModel


router = APIRouter()


@router.get('/account')
@template('account/index.pt')
def index(request: Request):
    vm = AccountViewModel()
    return vm.to_dict(request)
    # return template('index.html', data, request)


@router.get('/account/register')
@template('account/register.pt')
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()
    # return template('index.html', data, request)


@router.get('/account/login')
@template('account/login.pt')
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()
    # return template('index.html', data, request)


@router.get('/acount/logout')
@template('account/logout.pt')
def logout(request: Request):
    return {}
    # return template('index.html', data, request)