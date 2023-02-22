import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from .models import Contract, ContractItem,AcuerdoItem
from django.urls import reverse
from django.utils.safestring import mark_safe

def contract_detail(obj):
    return mark_safe('<a href="{}">View</a>'.format(
        reverse('contracts:admin_contract_detail', args=[obj.id])))

 
def export_to_csv(modeladmin, request, queryset): 
    opts = modeladmin.model._meta 
    response = HttpResponse(content_type='text/csv') 
    response['Content-Disposition'] = 'attachment;' \
        'filename={}.csv'.format(opts.verbose_name) 
    writer = csv.writer(response) 
     
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many] 
    # Write a first row with header information 
    writer.writerow([field.verbose_name for field in fields]) 
    # Write data rows 
    for obj in queryset: 
        data_row = [] 
        for field in fields: 
            value = getattr(obj, field.name) 
            if isinstance(value, datetime.datetime): 
                value = value.strftime('%d/%m/%Y') 
            data_row.append(value) 
        writer.writerow(data_row) 
    return response 
export_to_csv.short_description = 'Export to CSV' 


class ContractItemInline(admin.TabularInline):
    model = ContractItem
    raw_id_fields = ['product']

class AcuerdoItemInline(admin.TabularInline):
    model = AcuerdoItem


def contract_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(
        reverse('contracts:admin_contract_pdf', args=[obj.id])))
contract_pdf.short_description = 'Contract'


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'CI', 'city', 'paid',
                    'created', 'updated', contract_detail, contract_pdf]
    list_filter = ['paid', 'created', 'updated']
    inlines = [ContractItemInline,AcuerdoItemInline]
    
    actions = [export_to_csv]
