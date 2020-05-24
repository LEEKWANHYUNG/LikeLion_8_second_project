from django.contrib import admin
from django.urls import path,include
import main.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name ='home'),
    path('accounts/',include('accounts.urls')),
    path('UNIV/',include('UNIV.urls')),
]
