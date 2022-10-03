from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name = 'home'), # here we have added the new path
    path('about/', views.About.as_view(), name = 'about'),
    path('birds/', views.BirdsList.as_view(), name='birds_list'),
    # here is the new route
    path('birds/new/', views.BirdsCreate.as_view(), name='birds_create'),
]