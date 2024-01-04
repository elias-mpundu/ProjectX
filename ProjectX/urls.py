"""
URL configuration for ProjectX project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import auth
from django.urls import include
from django.urls import path
from django.views.generic.base import TemplateView 
from Report_Viewer import views as rv_views
from Image_Viewer import views as iv_views
from Users import views as u_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('report_viewer/', rv_views.report_viewer, name ='rv_views.report_viewer'),
    path('image_viewer/', iv_views.image_viewer, name ='iv_views.image_viewer'),
    path('users/', u_views.users, name ='u_views.users'),
    path('home_profile/', u_views.home_profile, name ='u_views.home_profile'),
    path("accounts/", include("django.contrib.auth.urls")), 
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('profile/', rv_views.profile, name ='rv_views.profile' )



]
#    path('login/', u_views.login, name ='u_views.login'),