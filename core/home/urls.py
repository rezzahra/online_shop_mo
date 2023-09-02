from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
                  path('', views.HomeView.as_view(), name='home'),
                  path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
