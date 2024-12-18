from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from dashboard.forms import PostForm, EmployeesForm, AboutUsForm, GalleryForm, ReviewsForm
from myapp.models import Post, Employees, AboutUs, Gallery, Reviews


def dashboard_home(request):
    return render(request, 'dashboard/home.html')


def reviews_list(request):
    reviews = Reviews.objects.all()
    return render(request, 'dashboard/reviews/reviews_list.html', {'reviews': reviews})


def reviews_create(request):
    if request.method == 'POST':
        form = ReviewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:reviews_list')
    else:
        form = ReviewsForm()
    return render(request, 'dashboard/reviews/reviews_form.html', {'form': form})


def reviews_update(request, id):
    reviews = get_object_or_404(Reviews, id=id)
    if request.method == 'POST':
        form = ReviewsForm(request.POST, request.FILES, instance=reviews)
        if form.is_valid():
            form.save()
            return redirect('dashboard:reviews_list')
    else:
        form = ReviewsForm(instance=reviews)
    return render(request, 'dashboard/reviews/reviews_form.html', {'form': form})


def reviews_delete(request, id):
    reviews = get_object_or_404(Reviews, id=id)
    if request.method == 'POST':
        reviews.delete()
        return redirect('dashboard:reviews_list')
    return render(request, 'dashboard/reviews/reviews_confirm_delete.html', {'reviews': reviews})


def gallery_list(request):
    gallery = Gallery.objects.all()
    return render(request, 'dashboard/gallery/gallery_list.html', {'gallery': gallery})


def gallery_create(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:gallery_list')
    else:
        form = GalleryForm()
    return render(request, 'dashboard/gallery/gallery_form.html', {'form': form})


def gallery_delete(request, gallery_id):
    gallery = get_object_or_404(Gallery, gallery_id=gallery_id)
    if request.method == 'POST':
        gallery.delete()
        return redirect('dashboard:gallery_list')
    return render(request, 'dashboard/gallery/gallery_confirm_delete.html', {'gallery': gallery})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'dashboard/post/post_list.html', {'posts': posts})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:post_list')
    else:
        form = PostForm()
    return render(request, 'dashboard/post/post_form.html', {'form': form})


def post_update(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard:post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'dashboard/post/post_form.html', {'form': form})


def post_delete(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('dashboard:post_list')
    return render(request, 'dashboard/post/post_confirm_delete.html', {'post': post})


def employee_list(request):
    employees = Employees.objects.all()
    return render(request, 'dashboard/employees/employee_list.html', {'employees': employees})


def employee_create(request):
    if request.method == 'POST':
        form = EmployeesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:employee_list')
    else:
        form = EmployeesForm()
    return render(request, 'dashboard/employees/employee_form.html', {'form': form})


def employee_update(request, employee_id):
    employee = get_object_or_404(Employees, employee_id=employee_id)
    if request.method == 'POST':
        form = EmployeesForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('dashboard:employee_list')
    else:
        form = EmployeesForm(instance=employee)
    return render(request, 'dashboard/employees/employee_form.html', {'form': form})


def employee_delete(request, employee_id):
    employee = get_object_or_404(Employees, employee_id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('dashboard:employee_list')
    return render(request, 'dashboard/employees/employee_confirm_delete.html', {'employee': employee})


def about_list(request):
    about = AboutUs.objects.all()
    return render(request, 'dashboard/about-us/about_list.html', {'about': about})


def about_create(request):
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:about_list')
    else:
        form = AboutUsForm()
    return render(request, 'dashboard/about-us/about_form.html', {'form': form})


def about_update(request, id):
    about = get_object_or_404(AboutUs, id=id)
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('dashboard:about_list')
    else:
        form = AboutUsForm(instance=about)
    return render(request, 'dashboard/about-us/about_form.html', {'form': form})


def about_delete(request, id):
    about = get_object_or_404(AboutUs, id=id)
    if request.method == 'POST':
        about.delete()
        return redirect('dashboard:about_list')
    return render(request, 'dashboard/about-us/about_confirm_delete.html', {'about': about})
