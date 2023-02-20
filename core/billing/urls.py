from django.urls import path
from . import views


app_name = "billing"
urlpatterns = [
        path("", views.index, name='index'),
        path("search-items", 
             views.search_item, 
             name="search_item"),
        ]
