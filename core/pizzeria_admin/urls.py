from django.urls import path
from . import views

app_name = "pizzeria_admin"
urlpatterns = [
    path("login/", views.pizzeria_login, name='login'),
    path('', views.pizzeria_admin, name="admin"),
    path('statistics/', views.statistics, name="statistics"),
    path('admin-logout/', views.admin_logout, name="logout"),
    path('order-history', views.order_history, name="order_history"),
    path('order-detail/<int:order_id>',
         views.order_detail_view, name="order_detail"),

]

htmx_urlpatterns = [
    path('delete-item/<int:item_id>',
         views.delete_item_from_model,
         name="delete_item_from_model"),
    path('order-history-search/',
         views.order_history_search,
         name="order_history_search"),
    path('search-items/',
         views.search_items,
         name="search_items"),

]

urlpatterns += htmx_urlpatterns
