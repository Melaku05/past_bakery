from django.urls import path
from .views import catering
from django.views.generic import TemplateView

urlpatterns = [
    path('', catering, name='catering'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]
