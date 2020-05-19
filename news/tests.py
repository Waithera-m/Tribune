from django.test import TestCase
from .models import Editor,tags,Article
import datetime as dt

# Create your tests here.

class EditorTestClass(TestCase):

    #set up function to run before each test unit
    def setUp(self):

        """
        method runs before each test
        """
        self.mary = Editor(first_name='Mary',last_name='Njihia',email='njihiamary1@gmail.com')
    
    def test_instance(self):

        """
        method tests if objects are initialized properly
        """
        self.assertTrue(isinstance(self.mary,Editor))
    
    def test_save_method(self):

        """
        methods tests class save functionality
        """
        self.mary.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)

    def test_delete_method(self):

        """
        method tests class delete functionality
        """
        self.mary.save_editor()
        self.mary.delete_editor()
        editor = Editor.objects.all()
        self.assertTrue(len(editor)==0)

    def test_display_all_editors(self):

        """
        method tests class display all editors functionality
        """
        self.mary.save_editor()
        self.assertTrue(Editor.display_editors(),Editor.objects.all())
    
class TagsTestClass(TestCase):

        def setUp(self):

            """
            method runs before each test
            """
            self.tag = tags(name="Testing")
        
        def test_save_tag(self):

            """
            methods tests class save functionality
            """
            self.tag.save_tag()
            tag = tags.objects.all()
            self.assertTrue(len(tag)>0)



class ArticleTestClass(TestCase):
    
    def setUp(self):

        """
        method runs before each test
        """
        # Creating a new editor and saving it
        self.mary = Editor(first_name='Mary',last_name='Njihia',email='njihiamary1@gmail.com')
        self.mary.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.mary)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):

        """
        method runs after all tests
        """
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
    
    def test_get_news_today(self):

        """
        method tests class retrieval functionality
        """
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)
    
    def test_get_news_by_date(self):

        """
        method tests class retrieval functionality
        """
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
    
    


        
    
    

        

    