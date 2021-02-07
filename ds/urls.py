"""ds URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jewelry import views as j_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', j_views.home, name='home'),
    path('add/', j_views.add_customer, name='add'),
    path('add-item/<int:pk>/', j_views.add_item, name='add-item'),
    path('items/<int:pk>/', j_views.items, name='items'),
    path('customers/', j_views.customers, name='customers'),
    path('customer-update/<int:pk>/',
         j_views.CustomerUpdateView.as_view(),
         name='customer-update'),
    path('item-update/<int:pk>/',
         j_views.ItemUpdateView.as_view(),
         name='item-update'),
    path('customer-delete/<int:pk>/',
         j_views.CustomerDeleteView.as_view(),
         name='customer-delete'),
    path('item-delete/<int:pk>/',
         j_views.ItemDeleteView.as_view(),
         name='item-delete'),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
