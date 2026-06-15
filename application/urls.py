from django.urls import path
from .forms import LoginForm
from . import views
from django.contrib.auth.views import  LoginView, LogoutView 

urlpatterns=[
    path("",views.run,name='user_list'),
    path("user/<slug:slug>/", views.user_view, name='user_view'),
    path("user/create",views.create_user, name='create_user'),
    path("user/update/<slug:slug>/", views.update_user_with_password, name='update_user'),
    path("user/delete/<slug:slug>/", views.delete_user, name='delete_user'),
    path('register/', views.register_view, name='register'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    path('login/', LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.home_view_1, name='profile'),  # bu aslida home ,profile emas
    path('home/', views.profile_view, name='home'), # bu aslida profile, home emas
    path('admin_panel/', views.users_list, name='admin_panel'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('admin/', views.users_list, name='admin'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/delete/', views.profile_delete, name='profile_delete'),
    path('profile12/', views.abc, name='abc'),
    path('posts/', views.post_list, name='post_list'),
    path('post_detail/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post_create/', views.post_create,name = 'post_create'),
    path('post_update/<slug:slug>/',views.post_update,name = 'post_update'),
    path('post_delete/<slug:slug>/',views.post_delete,name='post_delete'),
    path('search/',views.search_posts,name = 'search_posts'),
    path('post/<slug:slug>/',views.post_detail, name = 'post_detail'),
    path('post/<slug:slug>/like/', views.like_toggle, name='like_toggle'),
    path('post/<slug:slug>/comment/', views.add_comment, name='add_comment'),

]