from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from .models import Superhero


class PageAppTest(SimpleTestCase):

    def test_django(self):
        self.assertTrue(True)


class PageDataTest(TestCase):
    def test_page(self):
        self.assertEqual(len(Superhero.objects.all()), 0)
        Superhero.objects.create(title='Title 1')
        Superhero.objects.create(title='Title 2')
        self.assertEqual(len(Superhero.objects.all()), 2)

        a = Superhero.objects.get(pk=2)
        self.assertEqual(a.title, 'Title 2')

        a.title = "New Title"
        a.save()
        self.assertEqual(a.title, 'New Title')

        a.delete()
        self.assertEqual(len(Superhero.objects.all()), 1)


class SuperheroViewsTest(TestCase):
    def test_superhero_list_view(self):
        self.assertEqual(reverse("superhero_list"), "/superhero/")

    def test_superhero_add_view(self):
        a = dict(title='T 1', body='None')
        b = dict(title='T 2', body='None')
        response = self.client.post(reverse("superhero_add"), a)
        response = self.client.post(reverse("superhero_add"), b)
        self.assertEqual(len(Superhero.objects.all()), 2)