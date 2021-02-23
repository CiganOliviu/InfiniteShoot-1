from django.db import models
from django.contrib.auth.models import User

COLUMN_NUMBER = (
    ("First Column", "First Column"),
    ("Second Column", "Second Column"),
    ("Third Column", "Third Column"),
    ("Fourth Column", "Fourth Column"),
)


class PlatformPresentationImage(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')
    column = models.CharField(max_length=255, choices=COLUMN_NUMBER, default="First Column")

    def __str__(self):
        return self.name


class ImagesClient(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='specific_user_gallery_images/')
    pick_image = models.BooleanField(default=False)
    column = models.CharField(max_length=255, choices=COLUMN_NUMBER, default="First Column")

    def __str__(self):
        return self.name

