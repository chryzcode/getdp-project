from datetime import datetime
from black import re
from corsheaders import django
from django.urls import re_path
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.wsgi import get_wsgi_application
import os
from importlib.util import find_spec
from fastapi.staticfiles import StaticFiles
from django.conf import settings
from typing import List
import cloudinary
import cloudinary.uploader
from pydantic import BaseModel
from fastapi_cloudinary_config import *

# export Django settings env variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "getdp_project.settings")

django_app = get_wsgi_application()

# import models
from mydp_app.models import *


def serialize_banner(banner):
    return {
        "user": banner.user.username,
        "name": banner.name,
        "description": banner.description,
        "image": banner.image,
        "tag": banner.tag,
        "category": banner.category,
        "slug": banner.slug,
        "created": banner.created,
        "updated": banner.updated,
    }


def banner_serializer(banners, many=False):
    if many:
        return [serialize_banner(banner) for banner in banners]
    return [serialize_banner(banners)]


class BannerModel(BaseModel):
    user: str
    name: str
    description: str
    category: str
    tag: str
    image: dict

app = FastAPI()

# serve static files
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


@app.post("/banner")
def create_a_banner(
    banner_user: str,
    banner_name: str,
    banner_description: str,
    banner_category: str,
    banner_tag: str,
    banner_image: UploadFile = File(...),
):
    banner = Banner.objects.create(
        user_id=User.objects.filter(username=banner_user).first().id,
        name=banner_name,
        description=banner_description,
        category=Category.objects.filter(name=banner_category).first(),
        tag=Tag.objects.filter(name=banner_tag).first(),
        image=cloudinary.uploader.upload(
            banner_image.file, folder="mydp_app/banner-images/"
        ),
    )
    banner.save()
    return {"message": "Banner created"}


@app.delete("/banner/{banner_slug}")
def delete_a_banner(banner_slug: str):
    banner = Banner.objects.filter(slug=banner_slug).first()
    if banner:
        banner.delete()
        return {"message": "Banner deleted"}
    else:
        return {"message": "Banner not found"}


@app.get("/banners")
def get_all_banners():
    banners = Banner.objects.all()
    banner_list = []
    if banners:
        for banner in banners:
            banner_list.append(banner)
        return banner_list
    else:
        return {"message": "No banners found"}

@app.get("/users")
def get_all_users():
    users  = User.objects.all()
    user_list = []
    if users:
        for user in users:
            user_list.append(user)
        return user_list
    else:
        return {"message": "No users found"}

app.mount("/mydp_app", WSGIMiddleware(django_app))
