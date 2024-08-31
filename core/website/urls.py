from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.expertise, name='expertise'),
    #path('expertise/<slug:detail_slug>/', views.expertise_details, name='expertise_details'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   
