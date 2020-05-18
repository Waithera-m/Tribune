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
            tags.objects.create(name="testing")


class ArticleTestClass(TestCase):
    
    def setUp(self):
        
        """
        method runs before each test
        """
        self.mary= Editor(first_name='Mary',last_name='Njihia',email='njihiamary1@gmail.com')
        self.mary.save_editor()

        self.tags = tags(name="testing")

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor=self.mary,tags=self.tags)

        self.new_article.save()
    
    


        
    
    

        

    