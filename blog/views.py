from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import ListView, DetailView

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 4


class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Post
    template_name = 'post_detail.html'

def AboutPageView(request):
    return render(request, 'about.html')

@login_required
def ContactPageView(request):
    return render(request, 'contact.html')



def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html', {'form': UserCreationForm()})
    else:
        #create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signupuser.html',{'forms':UserCreationForm(),'error':"That user name has been taken. Please try someother username"})
        else:
            return render(request, 'signupuser.html',{'forms':UserCreationForm(), 'error':'password did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request,username = request.POST['username'],password = request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html', {'form':AuthenticationForm,'error':'Username and password did not match'})
        else:
            login(request,user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

