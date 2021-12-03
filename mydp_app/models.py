from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=300, null=True, blank=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='user-profile-images/', null=True)

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username']


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category-images/')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name




class Banner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150 , unique=True)
    description = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banner-images/')
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add = True)
    banner_users = models.ManyToManyField(User, related_name='banner_users', blank=True)
    slug = models.SlugField(unique=True, max_length=100)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_p',
 related_query_name='hit_count_generic_relation')
  
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Banner, self).save(*args, **kwargs)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE)
    name  = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class UserBanner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='banner-users-image/',)
    full_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.user.username + ' ' + str('use banner')


