# superlists/urls.py (ch03l012)

from django.urls import path            # 1
from lists.views import home_page       # 2

urlpatterns = [
    path("", home_page, name="home"),   # 3
]
