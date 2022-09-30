from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse_lazy

from . import models
from . import forms

class HomeView(generic.TemplateView):
    template_name = 'university/home.j2'


class RequestCreateView(SuccessMessageMixin,generic.CreateView):
    model = models.Request
    success_url = reverse_lazy('university:request-create')
    success_message = 'Basvurunuz olusturuldu'
    template_name = 'university/request-create.j2'

    def get_form_class(self):
        return forms.RequestForm


class FAQListView(generic.TemplateView):
    template_name = 'university/faq-list.j2'


class PostListView(generic.ListView):
    model = models.Post
    paginate_by = 3
    template_name = 'university/post-list.j2'


class PostDetailView(generic.DetailView):
    model = models.Post
    template_name = 'university/post-detail.j2'


class AreaListView(generic.ListView):
    model = models.Area
    template_name = 'university/area-list.j2'


class ContactUsView(generic.TemplateView):
    template_name = 'university/contact-us.j2'