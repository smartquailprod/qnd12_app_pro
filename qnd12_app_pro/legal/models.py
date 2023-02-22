from django.db import models
from comercial.models import service
from decimal import Decimal
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator
#from coupons.models import Coupon
from django.utils.translation import gettext_lazy as _
from orders.models import Order
from ckeditor.fields import RichTextField

 
class Contract(models.Model):
    TYPE_CHOICES = (
    ("Acuerdo de alianza estratégica", "ALIANZA"),
    ("Acuerdo de confidencialidad y privacidad de información", "ACUERDO"),
    ("Contrato de Servicios de Tecnologias de Información (IT)", "CONTRATO_1"),
    ("Contrato de Servicios de Consultoria en el departamento de gerencia", "CONTRATO_CG"),
    )

    TYPE_TITLE = (
    ("Sr", "Señor."),
    ("Sra", "Señora."),
    ("Sta", "Señorita."),
    ("Ing", "Ingeniero"),
    ("Arq", "Arquitecto"),
    ("Lic", "Licenciado"),
    ("Phd", "Doctor"),
    )
    LAW_TYPE = (
    ("Juridicamente ", "JURIDICO"),
    ("Naturalmente ", "NATURAL"),
    )

    BUSINESS_TYPE = (
    ("compañia", "compañia"),
    ("negocio", "negocio"),
    )

    type = models.CharField(_('Contract Type'),choices=TYPE_CHOICES, max_length=200,null=True)
    Law_type = models.CharField(_('Law Type'),choices=LAW_TYPE, max_length=20,null=True)
    Cli_title = models.CharField(_('Title Type'),choices=TYPE_TITLE, max_length=20,null=True)
    Business_type = models.CharField(_('Business Type'),choices=BUSINESS_TYPE, max_length=20, null=True)
    Business_name = models.CharField(_('Business names'), max_length=100, null = True)
    first_name = models.CharField(_('first names'), max_length=50)
    last_name = models.CharField(_('last names'), max_length=50)
    CI = models.BigIntegerField(_('Identy ID'),max_length=13,null=True)
    email = models.EmailField(_('e-mail'))
    address = models.CharField(_('address'), max_length=250)
    postal_code = models.CharField(_('postal code'), max_length=20)
    city = models.CharField(_('city'), max_length=100)
    country = models.CharField(_('country'), max_length=100,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)
   # coupon = models.ForeignKey(Coupon,related_name='contracts',null=True,blank=True,on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Contract {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))

 


class ContractItem(models.Model):
    contract = models.ForeignKey(Contract,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Order,
                                related_name='contract_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

class AcuerdoItem(models.Model):
    contract = models.ForeignKey(Contract,
                              related_name='Acuerdo_items',
                              on_delete=models.CASCADE,null=True)
    clausura = models.CharField(_('clausura'), max_length=250,null=True)
    intro = RichTextField(null=True)
   

    def __str__(self):
        return '{}'.format(self.id)

#--------------- ACUERDO DE CONFIDENCIALIDAD---------
