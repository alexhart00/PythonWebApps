from csv import writer
from django.core.management.base import BaseCommand

from hero.models import Article, Superhero

class Command(BaseCommand):
    def handle(self, *args, **options):
        save_data()

def save_data():
    table = [[b.name, b.identity, b.description, b.image, b.strengths, b.weaknesses] for b in Superhero.objects.all()]
    f = [b for b in Superhero.objects.all().values()]
    with open('hero_objects.csv', 'w', newline='') as f:
        writer(f).writerows(table)

    table = [[b.author, b.title, b.body] for b in Article.objects.all()]
    f = [b for b in Article.objects.all().values()]
    with open('article_objects.csv', 'w', newline='') as f:
        writer(f).writerows(table)

