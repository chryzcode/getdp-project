from corsheaders import django
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.wsgi import get_wsgi_application
import os
from importlib.util import find_spec
from fastapi.staticfiles import StaticFiles
from django.conf import settings
from typing import List

#export Django settings env variable 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'getdp_project.settings')

django_app = get_wsgi_application()

#import models
from mydp_app.models import *

app = FastAPI()

#serve static files
app.mount("/static", StaticFiles(directory="mydp_app/static"), name="static")

@app.get("/")
def home():
    return {"message": "Welcome to mydp_app"}


@app.get("/banner/{banner_slug}")
def get_a_banner(banner_slug: str):
    banner = Banner.objects.filter(slug=banner_slug).first()
    if banner:
        return {"banner": banner}
    else:
        return {"message": "Banner not found"}

@app.get("/user/{user_username}")
def get_a_user(user_username: str):
    user = User.objects.filter(username=user_username).first()
    if user:
        return {"user": user}
    else:
        return {"message": "User not found"}


@app.get("/category/{category_name}")
def get_a_category(category_name: str):
    category = Category.objects.filter(name=category_name).first()
    if category:
        return {"category": category}
    else:
        return {"message": "Category not found"}


@app.get("/tag/{tag_name}")
def get_a_tag(tag_name: str):
    tag = Tag.objects.filter(name=tag_name).first()
    if tag:
        return {"tag": tag}
    else:
        return {"message": "Tag not found"}

# @app.post("/banner")
# def create_a_banner(
#     banner_user: str,
#     banner_name: str,
#     banner_description: str,
#     banner_category: str,
#     banner_tag: str,
#     banner_image: UploadFile = File(...)
# ):
#     banner = Banner(
#         user_id=User.objects.filter(username=banner_user).first().id,
#         name=banner_name,
#         description=banner_description,
#         category=banner_category,
#         tag=banner_tag,
#         image=banner_image,
#     )
#     banner.save()
#     return {"message": "Banner created"}

# app.mount('/mydp_app', WSGIMiddleware(django_app))


@app.delete("/banner/{banner_slug}")
def delete_a_banner(banner_slug: str):
    banner = Banner.objects.filter(slug=banner_slug).first()
    if banner:
        banner.delete()
        return {"message": "Banner deleted"}
    else:
        return {"message": "Banner not found"}

