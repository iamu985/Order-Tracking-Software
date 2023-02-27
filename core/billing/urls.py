from django.urls import path
from . import views


app_name = "billing"
urlpatterns = [
    path("", views.index, name='index'),
]

htmx_patterns = [
    path('search-items', views.search_items, name="search_items"),
    path('add-item/<int:item_id>/',
         views.add_item, name="add_item"),
    path('update-item-quantity/<int:item_id>/<int:order_id>',
         views.update_item_quantity, name="update_item_quantity"),
]

urlpatterns += htmx_patterns
