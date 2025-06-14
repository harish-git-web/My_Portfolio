from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Project
from .models import ContactMessage

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    projects_list=Project.objects.all().order_by('-created_at')
    return render(request,'projects.html',{'projects':projects_list})

def contact(request):
    success=False
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        ContactMessage.objects.create(name=name,email=email,message=message)

        full_message=f"From: {name} <{email}\n\n message\n{message}>"
        send_mail(
            subject=f"New Message From {name}",
            message=full_message,
            from_email=email,
            recipient_list=['yourgmail@gmail.com'],
        )
        success = True
        # send_mail(subject, full_message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        # success = True

    return render(request, 'contact.html', {'success': success})

    