from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-first_name']

    def save_editor(self):
        
        """
        class method saves objects in the database
        """
        self.save()

    def delete_editor(self):

        """
        class method deletes saved editors
        """
        self.delete()
    
    @classmethod
    def display_editors(cls):

        """
        methods returns all saved editors
        """
        editors= Editor.objects.all()
        return editors


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
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)

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

    
    