from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('add/', views.add_book, name='add_book'),
    path('update/<int:pk>/', views.update_book, name='update_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('download/<int:pk>/', views.download_book, name='download_book'),
]
