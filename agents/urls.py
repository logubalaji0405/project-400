from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-editor/', views.add_editor, name='add_editor'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('projects/', views.projects, name='projects'),
    path('like/<int:pk>/', views.add_like, name='add_like'),
path('comment/<int:pk>/', views.add_comment, name='add_comment'),
]