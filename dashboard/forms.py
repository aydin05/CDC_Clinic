from django import forms
from myapp.models import Post, Employees, AboutUs, Gallery, Reviews
from django.contrib.auth.forms import AuthenticationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'
