from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name, receiver):
    """
    function facilitates the sending of emails to new subscribers
    """
    subject = 'Welcome to TheMoringaTribune Newsletter'
    sender = 'watchlist.flask@gmail.com'

    text_content = render_to_string('email/newsemail.txt', {"name":name})
    html_content =  render_to_string('email/newsemail.html', {"name":name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()