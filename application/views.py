import email
from django.shortcuts import render
from . import models
from django.shortcuts import redirect
import uuid

# Create your views here.

def run(request):
    users=models.CustomUser.objects.all() 
    return render(request, 'index.html',context={'users':users})

def user_view(request,slug):
    user=models.CustomUser.objects.get(slug=slug)
    return render(request,'user_view.html',{'user':user})

def create_user(request):
    if request.POST:
        name=request.POST.get('first_name')
        surename=request.POST.get('last_name')
        picture=request.FILES.get('picture')

        models.CustomUser.objects.create(
            first_name=name,
            last_name=surename,
            email=f"{name}{surename}{str(uuid.uuid4())[:6]}@gmail.com",
            picture=picture
        )
        return redirect('/')
    return render(request,'create_user.html')


def update_user(request, slug):
    user = models.CustomUser.objects.get(slug=slug)

    if request.POST:
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')

        if request.FILES.get('picture'):
            user.picture = request.FILES.get('picture')

        user.save()
        return redirect('/')

    return render(request, 'update_user.html', {'user': user})

def delete_user(request, slug):
    user = models.CustomUser.objects.get(slug=slug)

    if request.POST:
        user.delete()
        return redirect('/')

    return render(request, 'delete_user.html', {'user': user})
