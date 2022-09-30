from django.urls import include, path
from . import views
from . import views_page

app_name = 'university'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),

    path('fiyat-listesi/',views.AreaListView.as_view(),name='area-list'),
    path('kayit-ol/',views.RequestCreateView.as_view(),name='request-create'),
    
    # path('sss/',views.FAQListView.as_view(),name='faq-list'),

    path('haberler/',views.PostListView.as_view(),name='post-list'),
    path('haber/<str:slug>',views.PostDetailView.as_view(),name='post-detail'),
    

    path('iletisim/',views.ContactUsView.as_view(),name='contact-us'),

    # pages
    path('kayit-evraklari/',views_page.KayitEvraklari.as_view(),name='page-kayit-evraklari')
]