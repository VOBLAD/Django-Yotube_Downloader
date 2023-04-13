from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('download/', views.download, name='download'),
    path('download/{done}', views.done, name='done'),
    path('download/{mp3}', views.mp3, name='mp3'),
]

