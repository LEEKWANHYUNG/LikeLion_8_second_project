from django.contrib import admin
from django.urls import path, include
from . import views

# app_name = 'main'

urlpatterns = [
    path('',views.home, name = "home"),
    path('<int:blog_id>',views.detail,name="detail"),
    path('create',views.create,name="create"),
    # path('read/<int:blog id>',views.read,name='read'),
    path('update/<int:blog_id>',views.update, name="update"),
    path('new',views.new, name ="new"),
]