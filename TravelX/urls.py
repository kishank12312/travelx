"""TravelX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include,path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.views import logout_view,login_view,info_view,ticket_view,cancel_ticket
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    
    path(r'logout/', logout_view,name='logout'),
    path(r'viewticket/', ticket_view),
    path(r'cancelticket/', cancel_ticket),
    path(r'login/', login_view,name='login'),
    path(r'trains/', views.trains,name='trains'),
    #path(r'accountinfo/', info_view,name='info'),
    path(r'admin/', admin.site.urls),
    path(r'Booking/',include('Booking.urls')),
    path(r'accountinfo/',include('accounts.urls')),
    path(r'home/',views.home,name='home'),
    path(r'<slug:slug>/',views.test,name='capture'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
