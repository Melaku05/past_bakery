from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from msigana_ecommerce.admin_site import admin_site
from django.views.generic import TemplateView
from django.contrib.staticfiles.views import serve

# from django.contrib import admin

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', views.home, name='home'),
    path('services/', include('catering.urls')),
    path('store/', include('store.urls')),
    path('orders/', views.lookbook, name='lookbook'),
    path('blog/', include('blog.urls')),
    path('about-us/', views.about_us, name='about-us'),
    path('contact-us/', include('contact.urls')),
    path('accounts/', include('allauth.urls')),
    path('minerals/', views.minerals, name='minerals'),
    path('carts/', include('carts.urls')),
    path('orders/', include('orders.urls')),
    path('bankpay/', include('bankpay.urls')),
    path('rewardpay', include('rewardpay.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

