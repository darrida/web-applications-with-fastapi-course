import os
from pathlib import Path
import fastapi
from starlette.staticfiles import StaticFiles
import uvicorn
import fastapi_chameleon
# from . import utils
from src.views import home, account, packages


app = fastapi.FastAPI()


def main():
    configure()
    uvicorn.run(app, host='127.0.0.1')    


def configure():
    configure_templates()
    configure_routes()


def configure_templates(dev_mode=True):
    folder = Path(os.path.dirname(__file__))
    template_folder = os.path.join(folder, 'templates')
    fastapi_chameleon.global_init(template_folder, auto_reload=dev_mode)


def configure_routes():
    app.mount(
        path='/static',
        app=StaticFiles(directory=Path(os.path.dirname(__file__)) / 'static'),
        name='static')
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


if __name__ == '__main__':
    main()
else:
    configure()
