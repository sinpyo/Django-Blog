"""wink_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
import blog.views
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.index, name='index'),
#    path('index/', blog.views.index, name='index'),
    path('about/', blog.views.about, name='about'),
    path('contact/', blog.views.contact, name='contact'),
    path('post/', blog.views.post, name='post'),
    path('create/', blog.views.create, name='create'),
    path('post_create/', blog.views.post_create, name='post_create'),
    path('post/<int:pk>/', blog.views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit', blog.views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete', blog.views.post_delete, name='post_delete'),
    path('success/', blog.views.success, name='success'),
    path('ckeditor/', include('ckeditor_uploader.urls'))

]

#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
