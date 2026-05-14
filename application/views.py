from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render
from . import models
from django.shortcuts import redirect
import uuid
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

User=get_user_model()
# Create your views here.

def run(request):
    users=User.objects.all() 
    return render(request, 'home.html',context={'users':users})

def user_view(request,slug):
    user=User.objects.get(slug=slug)
    return render(request,'index.html',{'user':user})

def create_user(request):
    if request.POST:
        name=request.POST.get('first_name')
        surename=request.POST.get('last_name')
        picture=request.FILES.get('picture')

        user=User.objects.create(
            first_name=name,
            last_name=surename,
            email=f"{name}{surename}{str(uuid.uuid4())[:6]}@gmail.com",
            picture=picture
        )
        return redirect('/')
    return render(request,'create_user.html')


def update_user(request, slug):
    user = User.objects.get(slug=slug)

    if request.POST:
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')

        if request.FILES.get('picture'):
            user.picture = request.FILES.get('picture')

        user.save()
        return redirect('/')

    return render(request, 'update_user.html', {'user': user})

def delete_user(request, slug):
    user = User.objects.get(slug=slug)

    if request.POST:
        user.delete()
        return redirect('/')

    return render(request, 'delete_user.html', {'user': user})

#LOGIN, LOGOUT, REGISTER VIEWS

def home_view(request):
    return render(request, 'profile.html')

def register_view(request):
    form = RegisterForm()
    
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})



# def login_view(request):
#     form = LoginForm()

#     if request.method == 'POST':
#         form = LoginForm(request, data=request.POST)

#         if form.is_valid():
#             email = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(
#                request,
#                email=email,
#                password=password
#             )

#             if user is not None:
#                 login(request, user)
#                 return redirect('home')

#     return render(request,'login.html',{'form': form})

# def logout_view(request):
#     logout(request)
#     return redirect('/')


@login_required

def home_view(request):
    return render(request, 'home.html')

def profile_view(request):
    return render(request, 'profile.html')
