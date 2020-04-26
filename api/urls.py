from django.urls import path
from api import views
urlpatterns = [
    path('categories/', views.category_list),
    path('games/', views.game_list),
    
]