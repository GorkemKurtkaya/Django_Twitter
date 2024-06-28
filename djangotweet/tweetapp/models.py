from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)#kullanıcı silinince on_delete twitleri de silinir 
    tweet=models.CharField(max_length=140)
    #created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Tweet User:{self.username}  Tweet: {self.tweet}"