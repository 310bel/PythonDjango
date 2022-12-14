from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about-us',views.about, name='about'),
    path('create',views.create, name='create'),
    path('', include('social_django.urls', namespace='social'))
]
