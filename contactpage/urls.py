from django.urls import path
from . import views


app_name = 'contactpage'
urlpatterns = [
    path('', views.contactform, name=''),
    path('success/', views.success, name='success'),
]
