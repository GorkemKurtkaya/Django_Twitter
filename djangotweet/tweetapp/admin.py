from django.contrib import admin
from tweetapp.models import Tweet

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Username', {'fields': ['username']}),
        ('Tweet', {'fields': ['tweet']}),
    ]
    list_display = ('username', 'tweet')




admin.site.register(Tweet, TweetAdmin)