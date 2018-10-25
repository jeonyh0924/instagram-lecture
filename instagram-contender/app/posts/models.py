from django.db import models

from members.models import User

class Post(models.Model):
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    photo = models.ImageField(
        upload_to='Post'
    )


class Comment(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    content = models.TextField(

    )


class HashTag(models.Model):
    name = models.CharField(max_length=15)
