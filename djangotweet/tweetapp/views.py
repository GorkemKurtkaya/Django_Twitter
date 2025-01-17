from django.shortcuts import render,redirect
from . import models
from django.urls import reverse,reverse_lazy
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


# Create your views here.

@login_required(login_url="/login")
def add_tweet(request):
    if request.method == 'POST':
        tweet = request.POST["tweet"]
        models.Tweet.objects.create(username=request.user, tweet=tweet)
        return redirect(reverse('tweetapp:list_tweet'))
    else:
        return render(request, 'tweetapp/add_tweet.html')


def list_tweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict={'tweets':all_tweets} 
    return render(request, 'tweetapp/list_tweet.html', context=tweet_dict)

def add_tweetbyform(request):
    if request.method == 'POST':
        form = forms.AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname_input']
            tweet = form.cleaned_data['tweet_input']
            new_tweet = models.Tweet(nickname=nickname, tweet=tweet)
            new_tweet.save()
            return redirect(reverse('tweetapp:list_tweet'))
    else:
        form = forms.AddTweetForm()
    return render(request, 'tweetapp/add_tweetbyform.html', {'form': form})

def add_tweetbymodelform(request):
    if request.method == 'POST':
        form = forms.AddTweetModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tweetapp:list_tweet'))
    else:
        form = forms.AddTweetModelForm()
    return render(request, 'tweetapp/add_tweetbymodelform.html', {'form': form})

@login_required(login_url="/login")
def deletetweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect(reverse('tweetapp:list_tweet'))
    
def edit_tweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        if request.method == 'POST':
            tweet.tweet = request.POST['tweet']
            tweet.save()
            return redirect(reverse('tweetapp:list_tweet'))
        else:
            return render(request, 'tweetapp/edit_tweet.html', {'tweet': tweet})
   

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'
    
    
    
    
    
    