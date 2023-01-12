
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.utils.encoding import force_bytes  
from django.core.mail import EmailMessage 
from django.contrib.auth.tokens import default_token_generator

def send_activation_email(user, request, to_email):
    email_subject = "Подтверждение аккаунта на сайта foodtales.com"
    
    data = {
        "domain":get_current_site(request),
        'uid':urlsafe_base64_encode(force_bytes(user.id)),  
        'token': default_token_generator.make_token(user),
        'user':user
    }
    message = render_to_string("email_template/register_confirm_email.html",data)
    email = EmailMessage(email_subject, message, to=[to_email])
    email.content_subtype = "html"
    print(email.message())
    email.send(fail_silently=True)
    