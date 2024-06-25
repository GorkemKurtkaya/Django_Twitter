from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('add_tweet/', views.add_tweet, name='add_tweet'),
    path('list_tweet/', views.list_tweet, name='list_tweet'),
    path('add_tweetbyform/', views.add_tweetbyform, name='add_tweetbyform'),
]
