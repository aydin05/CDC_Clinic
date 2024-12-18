from datetime import timezone

from django.db import models


# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.surname


class SocialNetworks(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.ImageField(upload_to='social_networks/')


class Contact(models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    social_network = models.ForeignKey(SocialNetworks, on_delete=models.CASCADE)
    email = models.EmailField()


class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    gallery_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='gallery/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.__str__()


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='aboutus/')
    video_url = models.URLField(blank=True, null=True)


class Reviews(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
