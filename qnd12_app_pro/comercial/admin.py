import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from .models import Category, service ,ContractItem ,AcuerdoItem , oferta 
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.db.models import Count
from django.views.generic import ListView

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

@admin.register(Category)
class OrderAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'description']
    list_filter = ['name']
    actions = [export_to_csv]

@admin.register(service)
class serviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'puntos', 'total']
    #list_filter = ['created', 'updated']
    readonly_fields = ['total']
    actions = [export_to_csv]

class ContractItemInline(admin.TabularInline):
    model = ContractItem
    raw_id_fields = ['product']

class AcuerdoItemInline(admin.TabularInline):
    model = AcuerdoItem

def oferta_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(
        reverse('ofertas:admin_oferta_pdf', args=[obj.id])))
oferta_pdf.short_description = 'Oferta'


def oferta_detail(obj):
    return mark_safe('<a href="{}">View</a>'.format(
        reverse('ofertas:admin_oferta_detail', args=[obj.id])))


@admin.register(oferta)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'CI', 'city',
                    'created', 'updated', oferta_detail, oferta_pdf]
    list_filter = ['created', 'updated']
    inlines = [ContractItemInline,AcuerdoItemInline]
    
    actions = [export_to_csv]