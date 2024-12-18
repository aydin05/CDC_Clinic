from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from myapp.models import Services, Employees, Post, Gallery, AboutUs, Reviews, Contact, SocialNetworks


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Services.objects.all()
        context["employee"] = Employees.objects.all()
        context["gallery"] = Gallery.objects.all()
        context["reviews"] = Reviews.objects.all()
        context["contact"] = Contact.objects.all()
        context["social_network"] = SocialNetworks.objects.all()
        return context


class FooterPageView(TemplateView):
    template_name = 'includes/footer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = Contact.objects.all()
        context["social_network"] = SocialNetworks.objects.all()
        print(context["social_network"])
        return context

class ReviewsListView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = Contact.objects.all()
        context["reviews"] = Reviews.objects.all()
        context["social_network"] = SocialNetworks.objects.all()
        return context


class ServiceListView(TemplateView):
    template_name = 'service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = Contact.objects.all()
        context["services"] = Services.objects.all()
        context["social_network"] = SocialNetworks.objects.all()
        return context


class PostListView(TemplateView):
    template_name = 'posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = Contact.objects.all()
        context["posts"] = Post.objects.all()
        context["social_network"] = SocialNetworks.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts_lists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = Contact.objects.all()
        context["social_network"] = SocialNetworks.objects.all()
        return context


class EmployeeListView(TemplateView):
    template_name = 'employees.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["employees"] = Employees.objects.all()
        context["contact"] = Contact.objects.all()
        context["social_network"] = SocialNetworks.objects.all()
        return context


class EmployeeDetailView(DetailView):
    model = Employees  # Specify the model
    template_name = 'employee_about.html'  # Template for employee detail page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = Contact.objects.all()
        context["social_network"] = SocialNetworks.objects.all()
        return context


class GalleryListView(TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = Contact.objects.all()
        context["gallery"] = Gallery.objects.all()
        context["social_network"] = SocialNetworks.objects.all()
        return context


class AboutUsListView(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = Contact.objects.all()
        context["about_us"] = AboutUs.objects.all()
        context["social_network"] = SocialNetworks.objects.all()
        return context
