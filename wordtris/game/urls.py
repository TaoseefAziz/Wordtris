from django.urls import path
from . import views
urlpatterns = [
    path('game', views.game,name='game'),
    path('help', views.help,name='help'),
    path('scores', views.scores,name='scores'),
    path('my_scores', views.my_scores,name='my_scores'),
    path('add_game',views.add_game,name='add_game')
]
