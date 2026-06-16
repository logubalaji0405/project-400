from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-editor/', views.add_editor, name='add_editor'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('instagram-live/', views.instagram_live, name='instagram_live'),
]