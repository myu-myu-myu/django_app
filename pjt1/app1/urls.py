from django.urls import path

from pjt1.app1 import views

urlpatterns = [
    path('', views.music_list, name='music_list'),
    path('upload/', views.upload_music, name='upload_music'),
    path('<int:pk>/', views.delete_music, name='delete_music'),
]