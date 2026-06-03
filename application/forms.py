from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Tag
from .models import Post


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'picture',
            'password1',
            'password2'
        ]


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email kiriting'
        })
    )

class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ism'
        })
    )

    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Familiya'
        })

    )

    phone_number = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Telefon raqami'
        })
    )

    avatar = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'form-input',
            'placeholder': 'Avatar URL'
        })
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_number', 'avatar']

class UserProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-input',
            'placeholder': 'O\'zingiz haqingizda yozing!',
            'rows': 5
        })
    )

    website = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'form-input',
            'placeholder': 'Veb-sayt URL'
        })
    )

    class Meta:
        model = CustomUser
        fields = ['bio', 'website']

class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Post sarlavhasi'
        })
    )

    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-input',
            'placeholder': 'Post matni'
        })
    )

    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'form-file',
            'placeholder': 'Post rasmi'
        })
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'tag-checkbox'
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'tags']



    

