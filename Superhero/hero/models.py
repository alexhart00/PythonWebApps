from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class Superhero(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200)
    description = models.TextField(default="None")
    image = models.CharField(max_length=200, default="None")
    strengths = models.CharField(max_length=200, default="None")
    weaknesses = models.CharField(max_length=200, default="None")

    def __str__(self):
        return self.identity

    def get_absolute_url(self):
        return reverse_lazy('hero_list')

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=200)
    body = models.TextField()

class Investigator(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=200)


def get_upload(instance, filename):
    return f'{filename}' ##images/ removed

class Photo (models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to=get_upload)

    def __str__(self):
        return f'{self.pk} - {self.title}'

    def get_absolute_url(self):
        return reverse_lazy('photo_detail', args=[str(self.id)])
