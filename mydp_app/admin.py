from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Banner)
admin.site.register(Tag)
admin.site.register(UserBanner)
admin.site.register(Comment)
