from email.policy import default
from django.db import models
#from shop.models import Product
from decimal import Decimal
from django.contrib import admin
from phone_field import PhoneField
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator
#from coupons.models import Coupon
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):
    
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(blank=True,null=True)
   # detail = models.FileField(upload_to='tours/%Y/%m/%d',null=True)
    terms = models.TextField(blank=True)

    

    class Meta:
        #ordering = ('name',)
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'

    def __str__(self):
        return self.name

  #  def get_absolute_url(self):
  #          return reverse('shop:product_list_by_category',
  #                         args=[self.slug])


class service(models.Model):

    LIMPIEZA_CONTRATO = 'Limpieza complementaria'
    LIMPIEZA_VIDRIOS = 'Limpieza de vidrios'
    LIMPIEZA_PARQUEADEROS = 'Limpieza de parqueaderos'
    RECICLADO_RESIDUOS = 'Reciclado de residuos'
    VENTA_INSUMOS = 'Venta de Insumos'


    SERVICES = [
        (LIMPIEZA_CONTRATO, 'Limpieza complementaria'),
        (LIMPIEZA_VIDRIOS, 'Limpieza de vidrios'),
        (LIMPIEZA_PARQUEADEROS, 'Limpieza de parqueaderos'),
        (RECICLADO_RESIDUOS, 'Reciclado de residuos'),
        (VENTA_INSUMOS, 'Venta de Insumos'),
    ]
  
    
    name = models.CharField(_('Nombre de Servicio'),max_length=200,choices=SERVICES, db_index=True,null=True)
    #slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(_('Descripción'),blank=True)
    puntos = models.IntegerField(_('Puntos de limpieza'))
   # price = models.DecimalField(_('Costo por punto'),max_digits=100, decimal_places=2,null=True)
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE,null=True)
    
    available = models.BooleanField(default=True),
    

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total =  models.DecimalField(_('Costo base de servicio'),max_digits=100, decimal_places=2,null=True)

    def get_cost(self):
        return self.price * self.puntos
    
    def save(self):
        self.total = self.get_cost()
        super (service, self).save()

    class Meta:
        #ordering = ('name',)
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    
    #class Meta:
     #   ordering = ('name',)
     #   index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    

class oferta(models.Model):
    OFERTA_CHOICES = (
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

    # EDIFICIOS
    ADRIANPETRO = 'AP'
    CENTRODIDECOBOSQUE = 'CDB'
    ALCAZARSALAMANCA = 'ASM'
    ALCAZARSEVILLA = 'ASV'
    SIERRA = 'CHS'
    SANMARTIN = 'CSM'
    SIRAH = 'CS'
    VALLECARTAGO ='VC'
    VILLAMARINAUNO ='VMU'
    PIAZZATOSCANA = 'PZT'
    ARISTOPLAZA = 'APZ'
    ASIEL= 'AL'
    ASPEN= 'ASP'
    BATANPLAZA= 'BTP'
    BIZANCIO= 'BZ'
    BLUEDIAMOND = 'BD'
    BRISTOLTORRE = 'BT'
    CAMPUSCENTRAL = 'CC'
    CORYBA = 'CB'
    PEDREGAL = 'PD'
    FOURSEASONS = 'FS'
    KORONI = 'KN'
    KOUROS = 'KS'
    LAFARGUE = 'LG'
    METROPOLITAN = 'MN'
    PLUSDOS = 'PD'
    PUERTASDELSOL = 'PS'
    SCALA = 'SL'
    SOHOGALAXY = 'SG'
    SORELINA = 'SR'
    TENISBOULEVARD = 'TB'
    TERRAZASATRIUM = 'TA'
    TORRECARE = 'TC'
    TORREFINLANDIA = 'TF'
    TORRESOL = 'TS'
    TORRESUR = 'TSR'
    TRIER = 'TR'
    TRINIDAD = 'TD'
    VERONES = 'VR'
    VIENA = 'VN'
    AQUA = 'AQ'
    HOMEDETAIL = 'HD'
    KENZE = 'KZ'
    CASAENPARQUE = 'CP'
    NOVAKSTATUS = 'NS'
    PRISMANORTE = 'PN'
    CRISTIANSILVA = 'CS'
    TORREDELSOL = 'VN'
    TORRENOHA = 'TN'



    EDIFICIOS = [
        (ADRIANPETRO, 'ADRIAN PETROLEUM SERVICES S.A'),
        (CENTRODIDECOBOSQUE, 'CENTRO DE DISEÑO Y DECORACIÓN EL BOSQUE'),
        (ALCAZARSALAMANCA, 'CONJUNTO ALCAZAR DE SALAMANCA'),
        (SIERRA, 'CONJUNTO HABITACIONAL SIERRA I Y II'),
        (SANMARTIN, 'CONJUNTO SAN MARTÍN'),
        (SIRAH, 'CONJUNTO SIRAH'),
        (VALLECARTAGO, 'CONJUNTO VALLE CARTAGO'),
        (VILLAMARINAUNO, 'CONJUNTO VIA MARINA UNO'),
        (PIAZZATOSCANA, 'EDIFICIO PIAZZA TOSCANA'),
        (ARISTOPLAZA, 'EDIFICIO ARISTO PLAZA'),
        (ASIEL, 'EDIFICIO ASIEL'),
        (ASPEN, 'EDIFICIO ASPEN'),
        (BATANPLAZA, 'EDIFICIO BATAN PLAZA'),
        (BIZANCIO, 'EDIFICIO BIZANCIO'),
        (BLUEDIAMOND, 'EDIFICIO BLUE DIAMOND II'),
        (BRISTOLTORRE, 'EDIFICIO BRISTOL TORRE II'),
        (CAMPUSCENTRAL, 'EDIFICIO CAMPUS CENTRAL'),
        (CORYBA, 'EDIFICIO CORYBA'),
        (PEDREGAL, 'EDIFICIO EL PEDREGAL'),
        (FOURSEASONS, 'EDIFICIO FOUR SEASONS I'),
        (KORONI, 'EDIFICIO KORONI'),
        (KOUROS, 'EDIFICIO KOUROS'),
        (LAFARGUE, 'EDIFICIO LAFARGUE'),
        (METROPOLITAN, 'EDIFICIO METROPOLITAN'),
        (PLUSDOS, 'EDIFICIO PLUS DOS CENTRO DE NEGOCIOS'),
        (PUERTASDELSOL, 'EDIFICIO PUERTAS DEL SOL'),
        (SCALA , 'EDIFICIO SCALA '),
        (SOHOGALAXY, 'EDIFICIO SOHO GALAXY'),
        (SORELINA, 'EDIFICIO SORELINA'),
        (TENISBOULEVARD, 'EDIFICIO TENIS BOULEVARD'),
        (TERRAZASATRIUM, 'EDIFICIO TERRAZAS ATRIUM'),
        (TORRECARE, 'EDIFICIO TORRE CARE'),
        (TORREFINLANDIA, 'EDIFICIO TORRE FINLANDIA'),
        (TORRESOL, 'EDIFICIO TORRE SOL I'),
        (TRIER, 'EDIFICIO TRIER'),
        (VERONES, 'EDIFICIO VERONES'),
        (VIENA, 'EDIFICIO VIENA'),
        (AQUA, 'FIDEICOMISO INMOBILIARIO PARK QUITO'),
        (HOMEDETAIL, 'AGENCIA HOMEDETAIL'),
        (KENZE, 'EDIFICIO KENZE'),
        (CASAENPARQUE, 'LA CASA EN EL PARQUE'),
        (NOVAKSTATUS, 'EDIFICIO NOVAK STATUS'),
        (PRISMANORTE, 'EDIFICIO PRISMA NORTE'),
        (CRISTIANSILVA, 'CRISTIAN SILVA DOMINGUEZ'),
        (TORREDELSOL, 'EDIFICIO TORRE DEL SOL'),
        (TORRENOHA , 'EDIFICIO TORRE NOHA'),

    ]
    

    type = models.CharField(_('Tipo de oferta'),choices=OFERTA_CHOICES, max_length=200,null=True)
    Law_type = models.CharField(_('Law Type'),choices=LAW_TYPE, max_length=20,null=True)
    Cli_title = models.CharField(_('Title Type'),choices=TYPE_TITLE, max_length=20,null=True)
    Business_type = models.CharField(_('Business Type'),choices=BUSINESS_TYPE, max_length=20, null=True)
    Business_name = models.CharField(_('Nombre de edificio'),choices=EDIFICIOS, max_length=100, null = True)
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
    contract = models.ForeignKey(oferta,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(service,
                                related_name='service_items',
                                on_delete=models.CASCADE)
    #price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

class AcuerdoItem(models.Model):
    contract = models.ForeignKey(oferta,
                              related_name='Acuerdo_items',
                              on_delete=models.CASCADE,null=True)
    clausura = models.CharField(_('clausura'), max_length=250,null=True)
    intro = RichTextField(null=True)
   

    def __str__(self):
        return '{}'.format(self.id)