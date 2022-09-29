from django.views import generic
from django.urls import reverse_lazy

from . import models

class HomeView(generic.TemplateView):
    template_name = 'university/home.j2'


class RequestCreateView(generic.CreateView):
    model = models.Request
    fields = [
        'name',
        'tc',
        'phone',
        'area',
        'city',
        'message'
    ]
    success_url = reverse_lazy('university:request-create')
    template_name = 'university/request-create.j2'


class FAQListView(generic.TemplateView):
    template_name = 'university/faq-list.j2'


class PostListView(generic.TemplateView):
    template_name = 'university/post-list.j2'


class PostDetailView(generic.TemplateView):
    template_name = 'university/post-detail.j2'


class FacultyDetailView(generic.DetailView):
    model = models.Faculty
    template_name = 'university/faculty-detail.j2'


class FacultyListView(generic.TemplateView):
    template_name = 'university/faculty-list.j2'


class AreaListView(generic.TemplateView):
    template_name = 'university/area-list.j2'


class ContactUsView(generic.TemplateView):
    template_name = 'university/contact-us.j2'

class AboutUsView(generic.TemplateView):
    template_name = 'university/about-us.j2'