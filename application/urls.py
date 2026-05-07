from django.urls import path
from . import views

urlpatterns=[
    path("",views.run,name='user_list'),
    path("user/<slug:slug>/", views.user_view, name='user_view'),
    path("user/create",views.create_user, name='create_user'),
    path("user/update/<slug:slug>/", views.update_user, name='update_user'),
    path("user/delete/<slug:slug>/", views.delete_user, name='delete_user'),
]