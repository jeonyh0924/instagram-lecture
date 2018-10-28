from django.db import models


class User(models.Model):
    username = models.CharField(
        max_length=10,
        unique=True,

    )
    img_profile = models.ImageField(
        upload_to='User',
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=10,
    )
    site = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    introduce = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
