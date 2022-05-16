# import os
# from pathlib import Path
# from fastapi import Request
# from fastapi.templating import Jinja2Templates


# folder = Path(os.path.dirname(__file__)).parent
# template_folder = os.path.join(folder, 'templates')
# templates = Jinja2Templates(template_folder)


# def template(request: Request, html: str, params: dict = {}):
#     params['request'] = request
#     return templates.TemplateResponse(html, params)