from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=300, null=True, blank=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)



    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username']


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Banner(models.Model, HitCountMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    banner_name = models.CharField(max_length=100 , unique=True)
    description = RichTextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    banner_image = models.ImageField(upload_to='banner/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    banner_users = models.ManyToManyField(User, related_name='banner_users')
    slug = models.SlugField(unique=True, max_length=100)
    hit_count_generic = GenericRelation(
    HitCount, object_id_field='object_pk',
    related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.banner_name)
        return super(Banner, self).save(*args, **kwargs)