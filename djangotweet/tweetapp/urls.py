from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('add_tweet/', views.add_tweet, name='add_tweet'),
    path('', views.list_tweet, name='list_tweet'),
    path('add_tweetbyform/', views.add_tweetbyform, name='add_tweetbyform'),
    path('add_tweetbymodelform/', views.add_tweetbymodelform, name='add_tweetbymodelform'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('deletetweet/<int:id>/', views.deletetweet, name='deletetweet'),
    path('edit_tweet/<int:id>/', views.edit_tweet, name='edit_tweet')
]
