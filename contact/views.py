from django.shortcuts import render
from .models import info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def send_message(request):
    my_info = info.objects.first()

    if request.method == "POST":
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )

    
    context = {'info':my_info}
    return render(request, 'contact/contact.html',context)
