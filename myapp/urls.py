from django.urls import path
from .views import (HomePageView, ServiceListView, EmployeeListView, PostListView, GalleryListView, AboutUsListView, EmployeeDetailView, PostDetailView)
from django.conf.urls.static import static
from django.conf import settings

app_name = 'myapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('services/', ServiceListView.as_view(), name='services'),
    path('employees/', EmployeeListView.as_view(), name='employees'),
    path('employee_about/<int:pk>', EmployeeDetailView.as_view(), name='employee_about'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post_lists/<int:pk>', PostDetailView.as_view(), name='posts_lists'),
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('about-us/', AboutUsListView.as_view(), name='about-us'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
