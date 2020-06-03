from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Article, NewsLetterRecipients, MoringaMerch
from .forms import NewsLetterForm, NewsArticleForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import MerchSerializer
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

def newsletter(request):
    """
    view function facilitates the sending of newsletter emails and saving of new subscribers asychronously
    """
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have beeen added successfully to our mailing list'}
    return JsonResponse(data)

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = MoringaMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)