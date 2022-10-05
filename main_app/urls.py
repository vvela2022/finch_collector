from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name = 'home'), # here we have added the new path
    path('about/', views.About.as_view(), name = 'about'),
    path('birds/', views.BirdsList.as_view(), name='birds_list'),
    # here is the new route
    path('birds/new/', views.BirdsCreate.as_view(), name='birds_create'),
    path('birds/<int:pk>/', views.BirdsDetail.as_view(), name='birds_detail'),
    path('birds/<int:pk>/update', views.BirdsUpdate.as_view(), name = 'birds_update'),
    path('birds/<int:pk>/delete', views.BirdsDelete.as_view(), name='birds_delete'),
    path('birds/<int:pk>/habitat/new/', views.HabitatCreate.as_view(), name='habitat_create'),
    path('zoos/<int:pk>/birds/<int:birds_pk>/', views.ZooBirdsAssoc.as_view(), name="zoo_birds_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name='signup')
 ]