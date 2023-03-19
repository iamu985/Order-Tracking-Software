from django.urls import path
from . import views

app_name = "pizzeria_admin"
urlpatterns = [
    path("login/", views.pizzeria_login, name='login'),
    path('', views.pizzeria_admin, name="admin"),
    path('statistics/', views.statistics, name="statistics"),
    path('admin-logout/', views.admin_logout, name="logout"),

]

htmx_urlpatterns = [
    path('delete-item/<int:item_id>',
         views.delete_item_from_model,
         name="delete_item_from_model"),

]

urlpatterns += htmx_urlpatterns
