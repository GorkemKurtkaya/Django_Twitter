from django import forms

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(max_length=50, label='Your nickname')
    tweet_input = forms.CharField(max_length=140)
    