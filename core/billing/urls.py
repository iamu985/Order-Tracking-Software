from django.urls import path
from . import views


app_name = "billing"
urlpatterns = [
    path("", views.index, name='index'),
]

htmx_patterns = [
    path('search-items',
         views.search_items,
         name="search_items"
         ),

    path('add-item/<int:item_id>/',
         views.add_item,
         name="add_item"
         ),

    path('update-item-quantity/<int:item_id>/<int:order_id>',
         views.update_item_quantity,
         name="update_item_quantity"
         ),

    path('delete-item/<int:item_id>/<int:order_id>',
         views.delete_item,
         name="delete_item"
         ),

    path('create-order/<int:order_id>',
         views.create_order,
         name='create_order'),

    path('update-table-number/<int:order_id>',
         views.update_table_number,
         name='update_table_number')
]

urlpatterns += htmx_patterns
