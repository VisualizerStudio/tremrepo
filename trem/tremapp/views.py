from django.shortcuts import render
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from .models import *
import datetime

# Create your views here.


def index(request):
    latest_post = Post.objects.order_by('-date')[:3]
    context = {
        'latest':latest_post,
    }
    return render (request, 'frontend/index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phoneNo')
        subject = "I've made a choice today (Salvation Form)"
        context = {
            'fname':name,
            'lname':lname,
            'phone':phone,
        }
        html_message = render_to_string('frontend/mail-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'From <visualizerxstudio@gmail.com>'
        send = mail.send_mail(subject, plain_message, from_email, [
                    'chidieberendubuisi105@gmail.com'], html_message=html_message)
        if send:
            messages.success(request, 'Email sent')
        else:
            messages.error(request, 'Mail not sent')
    return render(request, 'frontend/index.html')