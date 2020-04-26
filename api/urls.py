from django.urls import path
from api import views
urlpatterns = [
    path('categories/', views.category_list),
    path('games/', views.game_list),

    path('categories/<int:id>/', views.CategoryView.as_view()),
    path('games/<int:id>/', views.GameView.as_view()),
    
]