from django.db import models

# Create your models here.

class Tweet(models.Model):
    nickname=models.CharField(max_length=50)
    tweet=models.CharField(max_length=140)
    #created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Tweet nick:{self.nickname}  says: {self.tweet}"