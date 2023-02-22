from django.urls import path
from . import views
#from django.utils.translation import gettext_lazy as _


app_name = 'ofertas'

urlpatterns = [
    #path('create/', views.contract_create, name='contract_create'),
    path('admin/oferta/<int:contract_id>/', views.admin_oferta_detail, name='admin_oferta_detail'),
    path('admin/oferta/<int:contract_id>/pdf/', views.admin_oferta_pdf, name='admin_oferta_pdf'),
]