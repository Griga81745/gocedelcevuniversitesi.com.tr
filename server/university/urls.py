from django.urls import include, path
from . import views

app_name = 'university'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),

    path('fiyat-listesi/',views.AreaListView.as_view(),name='area-list'),
    path('kayit-ol/',views.RequestCreateView.as_view(),name='request-create'),

    path('fakulteler/',views.FacultyListView.as_view(),name='faculty-list'),
    path('fakulteler/<int:pk>',views.FacultyDetailView.as_view(),name='faculty-detail'),
    
    path('sss/',views.FAQListView.as_view(),name='faq-list'),

    path('haberler/',views.PostListView.as_view(),name='post-list'),
    path('haber/',views.PostDetailView.as_view(),name='post-detail'),
    

    path('universitemiz/',views.AboutUsView.as_view(),name='about-us'),
    path('iletisim/',views.ContactUsView.as_view(),name='contact-us'),
]