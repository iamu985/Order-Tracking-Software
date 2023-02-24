from django.urls import path
from . import views


app_name = "billing"
urlpatterns = [
    path("", views.index, name='index'),
]

htmx_patterns = [
    path('search-items', views.search_items, name="search_items")
]

urlpatterns += htmx_patterns
