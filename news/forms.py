from django import forms
from .models import Article

class NewsLetterForm(forms.Form):
    """
    class facilitates the creation of subscribe form objects
    """
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')

class NewsArticleForm(forms.ModelForm):
    """
    class facilitates the creation of news form objects
    """
    class Meta:
        model = Article
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }