"""djangostripe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from payments.views import(home,
	stripe_config,
	create_checkout_session,
	Success,
	Cancelled)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('config/',stripe_config,name='stripe_config'),
    path('create-checkout-session/',create_checkout_session,name='create_checkout_session'),
    path('success/',Success,name='Success'),
    path('cancelled/',Cancelled,name='Cancelled'),

]
