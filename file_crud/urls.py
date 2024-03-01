from django.urls import path
from .views import file_home

app_name = 'file_crud'

urlpatterns = [
    path("", file_home, name="file_home"),
]