from django.shortcuts import render, redirect
from blog.models import Post, Comment
from .forms import CommentForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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
    # template=render_to_string('email_template.html')
    if request.method=='POST':
        # email = EmailMessage(
        #     'Thanks for your response.',
        #     template,
        #     settings.EMAIL_HOST_USER,
        #     ['ramareksotinoyo@gmail.com']
        #     )
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = thought
            comment.save()
            # email.fail_silently=False
            # email.send()
            return redirect('thought', slug=thought.slug)
    else:
        form=CommentForm()    
    return render(request, 'thought.html', {'thoughts':thought,'form':form})      

def login(request):
    return render(request, 'login.html') 

def register(request):
    if request.POST :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
        else:
            messages.error(request, 'Invalid form')
            return redirect('register')
    else:
        form = UserCreationForm()
        context = {
            'form': form
        }
    return render(request, 'register.html', context)

def dashboard(request):
    posts = Post.objects.all()
    total = posts.count()
    context = {
        'posts': posts,
        'total': total
    }
    return render(request, 'dashboard.html', context)