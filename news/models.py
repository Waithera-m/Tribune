from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

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
    tags = models.ForeignKey(tags, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    
    