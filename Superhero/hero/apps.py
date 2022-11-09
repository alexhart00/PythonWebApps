from django.apps import AppConfig


class HeroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hero'

class PhotosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'photos'
