from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = '_index_'),
    path('test/', views.test, name = '_test_')
]