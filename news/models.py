from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tag(self):

        """
        class method saves objects in the database
        """
        self.save()

class Article(models.Model):
    title = models.CharField(max_length=70)
    post = HTMLField()
    editor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to='articles/%Y/%m/%d')

    @classmethod
    def todays_news(cls):

        """
        method returns present-day news
        """
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def days_news(cls,date):

        """
        function returns news published on a given day
        """
        news = cls.objects.filter(pub_date__date = date)
        return news
    
    @classmethod
    def search_by_title(cls,search_term):
        articles = cls.objects.filter(title__icontains=search_term)
        return articles
    
class NewsLetterRecipients(models.Model):
    """
    class facilitates the creation of recipients objects
    """
    name = models.CharField(max_length=30)
    email = models.EmailField()

class MoringaMerch(models.Model):
    """
    class facilitates the creation of merch objects
    """
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)

    
    