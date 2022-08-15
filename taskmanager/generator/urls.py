from django.urls import path
from generator import views

urlpatterns = [
    path('generator',views.generator, name='generator'),
    path('passw',views.passw, name='passw'),
    path('About',views.About, name='About'),
]
