from django.db.models.query_utils import select_related_descend
from django.test import TestCase,SimpleTestCase
from django.conf.urls import url
from django.urls import reverse
# Create your tests here.
class SnackTest(TestCase):
    def test_list_page(self):
        url=reverse('home')
        actual= self.client.get(url).status_code
        excepted=200
        self.assertEqual(actual,excepted)
    def test_home_template(self):
        url=reverse('home')
        actual= self.client.get(url)
        excepted='snack_list.html'
        self.assertEqual(actual.templates[0].name,excepted)



'''

    def test_home_url_template(self):
        url=reverse('home')
        response=self.client.get(url)
        excepted='home.html'
        self.assertTemplateUsed(response,excepted)
    def test_about_url_template(self):
        url=reverse('about')
        response=self.client.get(url)
        excepted='about.html'
        self.assertTemplateUsed(response,excepted)

'''