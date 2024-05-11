from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('about/', views.about, name='about'),
    path('posts/',views.posts, name='posts'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)