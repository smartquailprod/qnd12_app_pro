from django.urls import reverse
from django.shortcuts import render, redirect
from .models import ContractItem
#from .forms import ContractCreateForm
#from cart_c.cart_c import Cart_C
#from .tasks import contract_created
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Contract
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from qr_code.qrcode.utils import QRCodeOptions
import weasyprint





@staff_member_required
def admin_contract_detail(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    return render(request,
                  'admin/contracts/contract/detail.html',
                  {'contract': contract})


@staff_member_required
def admin_contract_pdf(request, contract_id):
    context = dict(my_options=QRCodeOptions(size='t', border=6, error_correction='L'),)
    contract = get_object_or_404(Contract, id=contract_id)
    html = render_to_string('contracts/pdf.html',
                            {'contract': contract})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename = contract_{}.pdf"'.format(contract.id)
    weasyprint.HTML(string=html,  base_url=request.build_absolute_uri() ).write_pdf(response,stylesheets=[weasyprint.CSS('legal/static/css/pdf.css')], presentational_hints=True)
    return response

