from django.urls import path
from .forms import LoginForm
from . import views
from django.contrib.auth.views import  LoginView, LogoutView 

urlpatterns=[
    path("",views.run,name='user_list'),
    path("user/<slug:slug>/", views.user_view, name='user_view'),
    path("user/create",views.create_user, name='create_user'),
    path("user/update/<slug:slug>/", views.update_user, name='update_user'),
    path("user/delete/<slug:slug>/", views.delete_user, name='delete_user'),
    path('register/', views.register_view, name='register'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    path('login/', LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.home_view, name='profile'),  # bu aslida home ,profile emas
    path('home/', views.profile_view, name='home'), # bu aslida profile, home emas
]