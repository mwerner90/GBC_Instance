from django.urls import path
from . import views

app_name = "inventory"


urlpatterns = [
    path("", views.index, name="index"),
    path("new_item/", views.new_item, name="new_item"),
    path("new_location/", views.new_location, name="new_location"),
    path("count/", views.count, name="count"),
    path("stock/", views.stock, name="stock")
]
