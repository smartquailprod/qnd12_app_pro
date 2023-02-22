from django.db import models
from shop.models import Product
from django.db import models
from django.db.models.enums import Choices
from decimal import Decimal
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator, ip_address_validator_map
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    CLOUD_SERVERS = [
        ('AWS Cloud','AWS Cloud'),
        ('Digital Ocean','Digital Ocean'),
        ('Microsoft Azure','Microsoft Azure'),
        ('Google Cloud','Google Cloud'),
        ('SmartQuail Cloud','SmartQuail Cloud'),
    ]
    project_name = models.CharField(_('Project_name'), max_length=50,null=True)
    Business_name = models.CharField(_('Business name'), max_length=100,null=True)
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    CI = models.BigIntegerField(_('Identy ID'),max_length=13,null=True)
    email = models.EmailField(_('e-mail'))
    address = models.CharField(_('address'), max_length=250)
    postal_code = models.CharField(_('postal code'), max_length=20)
    city = models.CharField(_('city'), max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    deployd = models.BooleanField(default=False)
    cloud_server = models.CharField(_('Cloud Servers'),choices=CLOUD_SERVERS, max_length=50,null=True)
    braintree_id = models.CharField(max_length=150, blank=True) 
    ip_address_cloud= models.GenericIPAddressField(null=True)
    IVA = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)


    def iva(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return  total_cost * (self.IVA / Decimal('100'))


    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100')) + total_cost * (self.IVA / Decimal('100'))

   
    
    def get_total_cost_s(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost 

    def get_total_cost_s_iva(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost + total_cost * (self.IVA / Decimal('100'))


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
