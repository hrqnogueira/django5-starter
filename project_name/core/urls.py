from django.urls import path

from {{ project_name }}.core import views

urlpatterns = [
    path('', views.index)
]