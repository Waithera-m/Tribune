from django.shortcuts import render,redirect

from django.http import HttpResponse,Http404,HttpResponseRedirect

import datetime as dt

from .models import Article, NewsLetterRecipients

from .forms import NewsLetterForm, NewsArticleForm

from .email import send_welcome_email

from django.contrib.auth.decorators import login_required

# Create your views here.



def welcome(request):
    return render(request,'welcome.html')

def convert_dates(dates):

    #function gets the weekday number for the date
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #return actual day of the week
    day = days[day_number]
    return day



def past_days_news(request,past_date):

    try:
        #convert data from the string url
        date=dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    
    except ValueError:
        raise Http404()
        

    if date==dt.date.today():
        return redirect(news_today)

    news = Article.days_news(date)

    
    return render(request,'all-news/past-news.html',{"date":date,"news":news})

def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('news_today')
            print('valid')
    else:
        form = NewsLetterForm()
    return render(request,'all-news/today-news.html',{"date":date,"news":news, "letterform":form})

def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET["article"]
        searched_articles = Article.search_by_title(search_term)
        message = f'{search_term}'

        return render(request,'all-news/search.html',{"message":message,"articles":searched_articles})
    
    else:
        message = "Please type a different search term"
        return render(request,'all-news/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def article(request,article_id):

    try:
        article = Article.objects.get(id=article_id)
    except DoesNotExist:
        raise Http404()

    return render(request,'all-news/article.html', {"article":article})

@login_required(login_url='/accounts/login/')
def new_article(request):
    """
    view function returns form for adding new article
    """
    current_user = request.user
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('newsToday')
    else:
        form = NewsArticleForm()
    return render(request, 'news_article.html', {"form":form})
