"""
URL configuration for Railway project.

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
from django.urls import path, include
from reservation.views import *
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', CustomLogoutView.as_view(), name = 'logout'),
    path('signup/', signup, name = 'signup'),
    path('profile/', profile, name = 'profile'),
    path('add_balance/', add_balance, name = 'add_balance'),
    path('home/', home, name = 'home'),
    path('search/', home, name='search_trains'),
    path('booking/<str:coachCode>/<str:trainName>/<str:fromStation>/<str:toStation>/<str:journey_date>/', book_ticket, name='book_ticket'),
    path('', RedirectView.as_view(url='home/', permanent=False)),

]


