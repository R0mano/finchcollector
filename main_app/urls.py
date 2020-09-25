from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('characters/', views.characters_index, name='index'),
  path('characters/<int:character_id>/', views.character_detail, name='detail'),
  path('characters/create/', views.CharacterCreate.as_view(), name='characters_create'),
  path('characters/<int:pk>/update/', views.CharacterUpdate.as_view(), name='characters_update'),
  path('characters/<int:pk>/delete/', views.CharacterDelete.as_view(), name='characters_delete'),
  path('characters/<int:character_id>/add_force/', views.add_force, name='add_force'),
  path('characters/<int:character_id>/assoc_spaceship/<int:spaceship_id>/', views.assoc_spaceship, name='assoc_spaceship'),
  path('spaceships/', views.SpaceshipList.as_view(), name='spaceships_index'),
  path('spaceships/<int:pk>/', views.SpaceshipDetail.as_view(), name='spaceships_detail'),
  path('spaceships/create/', views.SpaceshipCreate.as_view(), name='spaceships_create'),
  path('spaceships/<int:pk>/update/', views.SpaceshipUpdate.as_view(), name='spaceships_update'),
  path('spaceships/<int:pk>/delete/', views.SpaceshipDelete.as_view(), name='spaceships_delete'),
]
