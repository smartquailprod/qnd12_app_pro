from django.urls import path
from . import views
#from django.utils.translation import gettext_lazy as _


app_name = 'contracts'

urlpatterns = [
   # path('create/', views.contract_create, name='contract_create'),
    path('admin/contract/<int:contract_id>/', views.admin_contract_detail, name='admin_contract_detail'),
    path('admin/contract/<int:contract_id>/pdf/', views.admin_contract_pdf, name='admin_contract_pdf'),
]