from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import About, Patents

# Create your views here.

def home(request):
    data = About.objects.first()
    return render(request, 'portfolio/home.html', {'profile': data})

# experience
def experience(request):
    return render(request, 'portfolio/experience.html')


# skills
def skills(request):
    return render(request, 'portfolio/skills.html')

# research
def research(request):
    data = Patents.objects.all()
    return render(request, 'portfolio/research.html', {'research': data})

# contact
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # send main
        send_mail(
            f'Contact Form Submission from {name}',
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    
    return render(request, 'portfolio/contact.html')
