"""
URL configuration for CarProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from carApp import views

from CarProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('repairs/', views.repairs, name="repairs"),
    path('repairs/delete/<int:repair_id>', views.deleteRepair, name="deleteRepair"),
    path('repairs/edit/<int:repair_id>/', views.editRepair, name="editRepair"),
    path('manufacturers/', views.manufacturer_list, name='manufacturer_list'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('offers/', views.offers_view, name='offers'),
    path('send-estimate/', views.send_estimate_request, name='send_estimate_request'),
    path('fix-request/', views.fix_request_view, name='fix_request'),

]

# Statik faylları servis etmək üçün əlavə et:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# Media fayllar üçün (səndə bu artıq var)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)