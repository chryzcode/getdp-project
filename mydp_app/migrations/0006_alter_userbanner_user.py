# Generated by Django 4.0.4 on 2022-04-24 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mydp_app', '0005_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbanner',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]