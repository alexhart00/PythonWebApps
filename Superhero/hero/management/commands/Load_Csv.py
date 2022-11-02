from csv import reader
from django.core.management.base import BaseCommand

from hero.models import Article, Superhero

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_data_hero()
        load_data_article()

def load_data_hero():
    table = [[b.name, b.identity, b.description, b.image, b.strengths, b.weaknesses] for b in Superhero.objects.all()]
    f = [b for b in Superhero.objects.all().values()]
    with open('hero_objects.csv') as f:
        return [row for row in reader(f)]

def load_data_article():
    table = [[b.author, b.title, b.body] for b in Article.objects.all()]
    f = [b for b in Article.objects.all().values()]
    with open('article_objects.csv') as f:
        return [row for row in reader(f)]
