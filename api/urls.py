from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('categories/', views.category_list),
    path('games/', views.game_list),

    path('categories/<int:id>/', views.CategoryView.as_view()),
    path('games/<int:id>/', views.GameView.as_view()),

    path('games/comment/', views.CommentView.as_view()),
    path('login/', obtain_jwt_token)
]