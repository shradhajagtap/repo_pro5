from django.urls import path
from .views import student_view, show_view, update_view, delete_view

urlpatterns = [
    path("", student_view, name="student_url"),
    path("show/", show_view, name="show_url"),
    path("update/", update_view, name="update_url"),
    path("delete/", delete_view, name="delete_url")
]
