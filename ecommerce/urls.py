"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

# from django.urls import path
# from . import views
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("accounts/", include("accounts.urls")),
#     path("products/", include("products.urls")),   # ✅ Add this
#     path("", include("core.urls")),   # 👈 root URL ye handle karega
#     path("cart/", include("cart.urls")),
#     path("cart/", views.view_cart, name="view_cart"),
#     path("cart/update/<int:product_id>/", views.update_cart, name="update_cart"),
#     path("cart/remove/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),
# ]
from django.contrib import admin
from django.urls import path, include
from . import views   # ab ye kaam karega

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("accounts/", include("accounts.urls")),
    path("products/", include("products.urls")),
    path("orders/", include("orders.urls")),
    
]
