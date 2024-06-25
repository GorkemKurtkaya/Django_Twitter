from django.contrib import admin
from tweetapp.models import Tweet

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Nickname', {'fields': ['nickname']}),
        ('Tweet', {'fields': ['tweet']}),
    ]
    list_display = ('nickname', 'tweet')




admin.site.register(Tweet, TweetAdmin)