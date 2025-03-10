### lists/tests.py (ch03l013)
from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")  
        self.assertContains(response, "<title>To-Do lists</title>", html)   
        self.assertContains(response, "<html>")  
        self.assertContains(response, "</html>")  