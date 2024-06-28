from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(max_length=50, label='Your nickname')
    tweet_input = forms.CharField(max_length=140)
    
    
class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['username', 'tweet'] 