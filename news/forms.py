from django import forms

class NewsLetterForm(forms.Form):
    """
    class facilitates the creation of subscribe form objects
    """
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')