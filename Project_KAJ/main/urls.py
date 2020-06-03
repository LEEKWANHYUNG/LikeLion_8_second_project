from django.contrib import admin
from django.urls import path, include
from . import views

# app_name = 'main'

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:blog_id>', views.detail, name="detail"),
    path('create', views.create, name="create"),
    path('update/<int:blog_id>', views.update, name="update"),
    path('edit/<int:blog_id>', views.edit, name="edit"),
    path('new', views.new, name="new"),
    path('delete/<int:blog_id>', views.delete, name= "delete"),
    path('seeun/', views.seeun, name="seeun"),
]
