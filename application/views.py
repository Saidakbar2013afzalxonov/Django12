from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render
from . import models
from django.shortcuts import redirect
import uuid
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileUpdateForm, UserProfileUpdateForm
from django.contrib.auth import logout as logaut
from django.shortcuts import get_object_or_404
from .forms import PostForm

User=get_user_model()
# Create your views here.

def run(request):
    users=User.objects.all() 
    return render(request, 'start.html',context={'users':users})

def users_list(request):
    users=User.objects.all() 
    return render(request, 'admin.html',{'users':users})

def user_view(request,slug):
    one_user=User.objects.get(slug=slug)
    if request.method == "POST":
        one_user = request.user
        one_user.first_name = request.POST.get("first_name")
        one_user.last_name = request.POST.get("last_name")
        one_user.phone_number = request.POST.get("phone_number")
        one_user.email = request.POST.get("email")

    return render(request,'user_view.html',{'user':one_user})

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
        user.phone_number = request.POST.get('phone_number')

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

def home_view(request, slug):
    user = User.objects.get(slug=slug)

    if request.POST:
        user.phone_number = request.POST.get('phone_number')
    return render(request, 'profile.html', {'user': user})

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

def update_user_with_password(request, slug):
    one_user = User.objects.get(slug=slug)
    if request.method == "POST":
        one_user = request.user

        one_user.first_name = request.POST.get("first_name")
        one_user.last_name = request.POST.get("last_name")
        one_user.phone_number = request.POST.get("phone_number")
        one_user.email = request.POST.get("email")


        if request.FILES.get("picture"):
            one_user.picture = request.FILES.get("picture")

        new_password = request.POST.get("password")
        if new_password:
            one_user.set_password(new_password)
            update_session_auth_hash(request, one_user)

        one_user.save()

        return redirect("profile")

    return render(request, "update_user.html")


@login_required

def home_view_1(request):
    return render(request, 'home.html')

@login_required

def abc(request):
    return render(request, 'profile.html')

@login_required
def profile_view(request):
    profile =  request.user.profile
    return render(request, 'profile_view.html', {'profile': profile, 'user': request.user})

def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('login')
    return render(request, 'delete_profile.html')

@login_required
def update_profile(request):
    user_form = ProfileUpdateForm(instance=request.user)
    profile_form = UserProfileUpdateForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    return render(request, 'update_profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def profile_delete(request):
    if request.method == 'POST':
        user = request.user
        logaut(request)
        user.delete()
        return redirect('login')
    return render(request, 'delete_profile.html')

def post_list(request):
    posts = models.Post.objects.select_related('author').all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(models.Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def post_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', slug=post.slug)

    return render(request, 'post_create.html', {'form': form})

