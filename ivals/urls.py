from django.contrib import admin
from django.urls import path
from main.views import index, form, result


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
	path('form/', form),
    path('result/', result),   
]
