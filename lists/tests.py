### lists/tests.py (ch03l003)
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()   # 1
        response = home_page(request)   # 2
        html = response.content.decode("utf8")   # 3
        self.assertIn("<title>To-Do lists</title>", html)   # 4
        self.assertTrue(html.startswith("<html>"))   # 5
        self.assertTrue(html.endswith("</html>"))   # 6
