from django.urls import reverse
from django.shortcuts import render, redirect
from .models import ContractItem, oferta
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from qr_code.qrcode.utils import QRCodeOptions
import weasyprint



@staff_member_required
def admin_oferta_detail(request, contract_id):
    contract = get_object_or_404(oferta, id=contract_id)
    return render(request,
                  'admin/contracts/contract/detail.html',
                  {'contract': contract})


@staff_member_required
def admin_oferta_pdf(request, contract_id):
    context = dict(my_options=QRCodeOptions(size='t', border=6, error_correction='L'),)
    contract = get_object_or_404(oferta, id=contract_id)
    html = render_to_string('contracts/contract/pdf.html',
                            {'contract': contract})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename = contract_{}.pdf"'.format(contract.id)
    weasyprint.HTML(string=html,  base_url=request.build_absolute_uri() ).write_pdf(response,stylesheets=[weasyprint.CSS('qnode41_app/static/css/pdf.css')], presentational_hints=True)
    return response

