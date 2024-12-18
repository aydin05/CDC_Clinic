from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from dashboard import views
from django.contrib.auth import views as auth_views

app_name = 'dashboard'

urlpatterns = [
                  path('', views.dashboard_home, name='dashboard_home'),
                  # Posts
                  path('posts/', views.post_list, name='post_list'),
                  path('posts/create/', views.post_create, name='post_create'),
                  path('posts/<int:post_id>/update/', views.post_update, name='post_update'),
                  path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),

                  # Employee
                  path('employees/', views.employee_list, name='employee_list'),
                  path('employees/create/', views.employee_create, name='employee_create'),
                  path('employees/<int:employee_id>/update/', views.employee_update, name='employee_update'),
                  path('employees/<int:employee_id>/delete/', views.employee_delete, name='employee_delete'),

                  # About Us
                  path('about/', views.about_list, name='about_list'),
                  path('about/create/', views.about_create, name='about_create'),
                  path('about/<int:id>/update/', views.about_update, name='about_update'),
                  path('about/<int:id>/delete/', views.about_delete, name='about_delete'),

                  # Gallery
                  path('gallery/', views.gallery_list, name='gallery_list'),
                  path('gallery/create/', views.gallery_create, name='gallery_create'),
                  path('gallery/<int:gallery_id>/delete/', views.gallery_delete, name='gallery_delete'),

                  # Reviews
                  path('reviews/', views.reviews_list, name='reviews_list'),
                  path('reviews/create/', views.reviews_create, name='reviews_create'),
                  path('reviews/<int:id>/update/', views.reviews_update, name='reviews_update'),
                  path('reviews/<int:id>/delete/', views.reviews_delete, name='reviews_delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
