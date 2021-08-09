from django.shortcuts import render, redirect
from blog.models import Post, Comment
from .forms import CommentForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')    

def about(request):
    return render(request, 'about.html') 

def thoughts(request):
    thought=Post.objects.all()
    context={
        'thoughts':thought
    }
    return render(request, 'thoughts.html', context)  

def thought(request, slug):
    thought=Post.objects.get(slug=slug)
    template=render_to_string('email_template.html')
    if request.method=='POST':
        email = EmailMessage(
            'Thanks for your response.',
            template,
            settings.EMAIL_HOST_USER,
            ['ramareksotinoyo@gmail.com']
            )
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = thought
            comment.save()
            email.fail_silently=False
            email.send()
            return redirect('thought', slug=thought.slug)
    else:
        form=CommentForm()    
    return render(request, 'thought.html', {'thoughts':thought,'form':form})      

def login(request):
    return render(request, 'login.html') 
