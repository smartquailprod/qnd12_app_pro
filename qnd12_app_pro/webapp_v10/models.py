import datetime
from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.functional import cached_property
from django.http import Http404
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import Tag as TaggitTag
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from streams import blocks
#from wagtail.core import blocks
from wagtail.core.models import Page,Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import StreamField, RichTextField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.search import index
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField


from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


class consultas_under(AbstractFormField):
    page = ParentalKey('under_contruction', on_delete=models.CASCADE, related_name='form_fields')

class under_contruction(AbstractEmailForm):
    # Empieza Barner de Inicio
    template = "webapp_v10/under_contruction.html"
    #cliente_Navbar = RichTextField(blank=True,verbose_name='Cliente-url')
    
   # banner_title1 = RichTextField(blank=True,verbose_name='Titulo del primer banner ')
   # banner_info1 = RichTextField(blank=True,verbose_name='Informacion del primer banner ')
   # banner_title2 = RichTextField(blank=True,verbose_name='Titulo del segundo banner ')
   # banner_info2 = RichTextField(blank=True,verbose_name='Informacion del segundo banner ')
   # banner_title3 = RichTextField(blank=True,verbose_name='Titulo del tercer banner ')
   # banner_info3 = RichTextField(blank=True,verbose_name='Informacion del tercer banner ')

    # Empieza Banner de Galerias
    bio = RichTextField(blank=True,verbose_name='rseña bibliografica')

    banner_title4 = RichTextField(blank=True,verbose_name='Titulo de galeria-1 ')
    banner_title5 = RichTextField(blank=True,verbose_name='Titulo de galeria-2  ')

    #Campos de Noticias

    #template = "webapp_0/index.html"
    custom_title = models.CharField(max_length=100,blank=True,null=True,help_text="Reescribe el  Titulo de la publicacion ")


    
    # Campos de consulta

    consulta_under= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    # galeria de imagenes barner de presentacion

    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [

       # FieldPanel('title', classname="full"),
      #  FieldPanel('cliente_Navbar', classname="full"),
      #  FieldPanel('banner_info1', classname="full"),
      #  FieldPanel('banner_title2', classname="full"),
      #  FieldPanel('banner_info2', classname="full"),
      #  FieldPanel('banner_title3', classname="full"),
      #  FieldPanel('banner_info3', classname="full"),
    #Panel Gelerias
        FieldPanel('bio', classname="full"),
        FieldPanel('banner_title4', classname="full"),
        FieldPanel('banner_title5', classname="full"),

#panel para campos de consulta
        FieldPanel('consulta_under', classname="full"),

        InlinePanel('galleria_under', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas_under"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
#Panel capo de noticas
        FieldPanel("custom_title"),
    ]

  #  def get_context(self, request, *args, **kwargs):
   #     context = super().get_context(request, *args, **kwargs)
    #    context["posts"] = NewsDetailPage.objects.live().public()
    #    return context
        

class GaleriadeImagenes_under(Orderable):
    page = ParentalKey(under_contruction, on_delete=models.CASCADE, related_name='galleria_under')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de Juan Silva Photo')
    profile_pic = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto de perfil')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
   
     

    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('profile_pic'),
        ImageChooserPanel('image'),        
    ]



    



# pagina de inicio
class consultas(AbstractFormField):
    page = ParentalKey('home', on_delete=models.CASCADE, related_name='form_fields')

class Home(AbstractEmailForm):
    # Empieza Barner de Inicio
    template = "webapp_v10/home.html"
    #cliente_Navbar = RichTextField(blank=True,verbose_name='Cliente-url')
    
   # banner_title1 = RichTextField(blank=True,verbose_name='Titulo del primer banner ')
   # banner_info1 = RichTextField(blank=True,verbose_name='Informacion del primer banner ')
   # banner_title2 = RichTextField(blank=True,verbose_name='Titulo del segundo banner ')
   # banner_info2 = RichTextField(blank=True,verbose_name='Informacion del segundo banner ')
   # banner_title3 = RichTextField(blank=True,verbose_name='Titulo del tercer banner ')
   # banner_info3 = RichTextField(blank=True,verbose_name='Informacion del tercer banner ')

    # Empieza Banner de Galerias
    bio = RichTextField(blank=True,verbose_name='rseña bibliografica')

    banner_title4 = RichTextField(blank=True,verbose_name='Titulo de galeria-1 ')
    banner_title5 = RichTextField(blank=True,verbose_name='Titulo de galeria-2  ')
    banner_title6 = RichTextField(blank=True,verbose_name='Titulo de galeria-3  ')
    banner_title7 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')
    banner_title8 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')
    banner_title9 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')
    banner_title10 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')
    banner_title11 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')



    # Empieza Banner de Tearsheet
    TS_info1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-1 info')
    TS_date1 = models.DateField("Fecha de Tearsheet-1",null=True, blank=True)
    TS_info2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-2 info')
    TS_date2 = models.DateField("Fecha de Tearsheet-2",null=True, blank=True)
    TS_info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-3 info')
    TS_date3 = models.DateField("Fecha de Tearsheet-3",null=True, blank=True)
    TS_info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-4 info')
    TS_date4 = models.DateField("Fecha de Tearsheet-4",null=True, blank=True)
    TS_info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-5 info')
    TS_date5 = models.DateField("Fecha de Tearsheet-5",null=True, blank=True)
    TS_info6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-6 info')
    TS_date6 = models.DateField("Fecha de Tearsheet-6",null=True, blank=True)
    TS_info7 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-7 info')
    TS_date7 = models.DateField("Fecha de Tearsheet-7",null=True, blank=True)
    TS_info8 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-8 info')
    TS_date8 = models.DateField("Fecha de Tearsheet-8",null=True, blank=True)
    TS_info9 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-9 info')
    TS_date9 = models.DateField("Fecha de Tearsheet-9",null=True, blank=True)
    TS_info10 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-10 info')
    TS_date10 = models.DateField("Fecha de Tearsheet-10",null=True, blank=True)
    TS_info11 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-11 info')
    TS_date11 = models.DateField("Fecha de Tearsheet-11",null=True, blank=True)
    TS_info12 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-12 info')
    TS_date12 = models.DateField("Fecha de Tearsheet-12",null=True, blank=True)
    TS_info13 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-13 info')
    TS_date13 = models.DateField("Fecha de Tearsheet-13",null=True, blank=True)
    TS_info14 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-14 info')
    TS_date14 = models.DateField("Fecha de Tearsheet-14",null=True, blank=True)
    TS_info15 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-15 info')
    TS_date15 = models.DateField("Fecha de Tearsheet-15",null=True, blank=True)
    TS_info16 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-16 info')
    TS_date16 = models.DateField("Fecha de Tearsheet-16",null=True, blank=True)
    TS_info17 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-17 info')
    TS_date17 = models.DateField("Fecha de Tearsheet-17",null=True, blank=True)
    TS_info18 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-18 info')
    TS_date18 = models.DateField("Fecha de Tearsheet-18",null=True, blank=True)
    TS_info19 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-19 info')
    TS_date19 = models.DateField("Fecha de Tearsheet-19",null=True, blank=True)
    TS_info20 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-20 info')
    TS_date20 = models.DateField("Fecha de Tearsheet-20",null=True, blank=True)
    
    #Campos de Noticias

    #template = "webapp_0/index.html"
    custom_title = models.CharField(max_length=100,blank=True,null=True,help_text="Reescribe el  Titulo de la publicacion ")


    
    # Campos de consulta

    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    # galeria de imagenes barner de presentacion

    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [

       # FieldPanel('title', classname="full"),
      #  FieldPanel('cliente_Navbar', classname="full"),
      #  FieldPanel('banner_info1', classname="full"),
      #  FieldPanel('banner_title2', classname="full"),
      #  FieldPanel('banner_info2', classname="full"),
      #  FieldPanel('banner_title3', classname="full"),
      #  FieldPanel('banner_info3', classname="full"),
    #Panel Gelerias
        FieldPanel('bio', classname="full"),
        FieldPanel('banner_title4', classname="full"),
        FieldPanel('banner_title5', classname="full"),
        FieldPanel('banner_title6', classname="full"),
        FieldPanel('banner_title7', classname="full"),
        FieldPanel('banner_title8', classname="full"),
        FieldPanel('banner_title9', classname="full"),
        FieldPanel('banner_title10', classname="full"),
        FieldPanel('banner_title11', classname="full"),
    #Tearsheet Info
        FieldPanel('TS_info1', classname="full"),
        FieldPanel('TS_date1', classname="full"),
        FieldPanel('TS_info2', classname="full"),
        FieldPanel('TS_date2', classname="full"),
        FieldPanel('TS_info3', classname="full"),
        FieldPanel('TS_date3', classname="full"),
        FieldPanel('TS_info4', classname="full"),
        FieldPanel('TS_date4', classname="full"),
        FieldPanel('TS_info5', classname="full"),
        FieldPanel('TS_date5', classname="full"),
        FieldPanel('TS_info6', classname="full"),
        FieldPanel('TS_date6', classname="full"),
        FieldPanel('TS_info7', classname="full"),
        FieldPanel('TS_date7', classname="full"),
        FieldPanel('TS_info8', classname="full"),
        FieldPanel('TS_date8', classname="full"),
        FieldPanel('TS_info9', classname="full"),
        FieldPanel('TS_date9', classname="full"),
        FieldPanel('TS_info10', classname="full"),
        FieldPanel('TS_date10', classname="full"),
        FieldPanel('TS_info11', classname="full"),
        FieldPanel('TS_date11', classname="full"),
        FieldPanel('TS_info12', classname="full"),
        FieldPanel('TS_date12', classname="full"),
        FieldPanel('TS_info13', classname="full"),
        FieldPanel('TS_date13', classname="full"),
        FieldPanel('TS_info14', classname="full"),
        FieldPanel('TS_date14', classname="full"),
        FieldPanel('TS_info15', classname="full"),
        FieldPanel('TS_date15', classname="full"),
        FieldPanel('TS_info16', classname="full"),
        FieldPanel('TS_date16', classname="full"),
        FieldPanel('TS_info17', classname="full"),
        FieldPanel('TS_date17', classname="full"),
        FieldPanel('TS_info18', classname="full"),
        FieldPanel('TS_date18', classname="full"),
        FieldPanel('TS_info19', classname="full"),
        FieldPanel('TS_date19', classname="full"),
        FieldPanel('TS_info20', classname="full"),
        FieldPanel('TS_date20', classname="full"),
#panel para campos de consulta
        FieldPanel('consulta', classname="full"),

        InlinePanel('galleria', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
#Panel capo de noticas
        FieldPanel("custom_title"),
    ]

  #  def get_context(self, request, *args, **kwargs):
   #     context = super().get_context(request, *args, **kwargs)
    #    context["posts"] = NewsDetailPage.objects.live().public()
    #    return context
        

class GaleriadeImagenes(Orderable):
    page = ParentalKey(Home, on_delete=models.CASCADE, related_name='galleria')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de Juan Silva Photo')
    profile_pic = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto de perfil')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
    image_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 2')
    image_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 3')

    # Imagenes Thumb Portfolio
    
    image_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Advertising Thumb-Galeria')
    image_5 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Product Thumb2-Galeria')
    image_6 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Documentary Thumb3-Galeria')
    image_7 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Landscape Thumb4-Galeria')

    # Fotos TearSheate
    image_8 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-1')
    image_9 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-2')
    image_10 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-3')
    image_11 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-4')
    image_12 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-5 ')
    image_13 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-6')
    image_14 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-7')
    image_15 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-8')
    image_16 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-9')
    image_17 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-10')
    image_18 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-11')
    image_19 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-12')
    image_20 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-13')
    image_21 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-14')
    image_22 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-15')
    image_23 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-16')
    image_24 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-17')
    image_25 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-18')
    image_26 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-19')
    image_27 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-20')
     

    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('profile_pic'),
        ImageChooserPanel('image'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image_3'),
        ImageChooserPanel('image_4'),
        ImageChooserPanel('image_5'),
        ImageChooserPanel('image_6'),
        ImageChooserPanel('image_7'),
        ImageChooserPanel('image_8'),
        ImageChooserPanel('image_9'),
        ImageChooserPanel('image_10'),
        ImageChooserPanel('image_11'),
        ImageChooserPanel('image_12'),
        ImageChooserPanel('image_13'),
        ImageChooserPanel('image_14'),
        ImageChooserPanel('image_15'),
        ImageChooserPanel('image_16'),
        ImageChooserPanel('image_17'),
        ImageChooserPanel('image_18'),
        ImageChooserPanel('image_19'),
        ImageChooserPanel('image_20'),
        ImageChooserPanel('image_21'),
        ImageChooserPanel('image_22'),
        ImageChooserPanel('image_23'),
        ImageChooserPanel('image_24'),
        ImageChooserPanel('image_25'),
        ImageChooserPanel('image_26'),
        ImageChooserPanel('image_27'),
        
    ]





# pagina de inicio
class consultas_1(AbstractFormField):
    page = ParentalKey('History', on_delete=models.CASCADE, related_name='form_fields')

class History(AbstractEmailForm):
    # Empieza Barner de Inicio
    template = "webapp_v10/history.html"
    #cliente_Navbar = RichTextField(blank=True,verbose_name='Cliente-url')
    
   # banner_title1 = RichTextField(blank=True,verbose_name='Titulo del primer banner ')
   # banner_info1 = RichTextField(blank=True,verbose_name='Informacion del primer banner ')
   # banner_title2 = RichTextField(blank=True,verbose_name='Titulo del segundo banner ')
   # banner_info2 = RichTextField(blank=True,verbose_name='Informacion del segundo banner ')
   # banner_title3 = RichTextField(blank=True,verbose_name='Titulo del tercer banner ')
   # banner_info3 = RichTextField(blank=True,verbose_name='Informacion del tercer banner ')

    # Empieza Banner de Galerias
    bio = RichTextField(blank=True,verbose_name='rseña bibliografica')

    banner_title4 = RichTextField(blank=True,verbose_name='Titulo de galeria-1 ')
    banner_title5 = RichTextField(blank=True,verbose_name='Titulo de galeria-2  ')
    banner_title6 = RichTextField(blank=True,verbose_name='Titulo de galeria-3  ')
    banner_title7 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')
    banner_title8 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')
    banner_title9 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')
    banner_title10 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')
    banner_title11 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')

    
    #Campos de Noticias

    #template = "webapp_0/index.html"
    custom_title = models.CharField(max_length=100,blank=True,null=True,help_text="Reescribe el  Titulo de la publicacion ")


    
    # Campos de consulta

    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    # galeria de imagenes barner de presentacion

    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [

       # FieldPanel('title', classname="full"),
      #  FieldPanel('cliente_Navbar', classname="full"),
      #  FieldPanel('banner_info1', classname="full"),
      #  FieldPanel('banner_title2', classname="full"),
      #  FieldPanel('banner_info2', classname="full"),
      #  FieldPanel('banner_title3', classname="full"),
      #  FieldPanel('banner_info3', classname="full"),
    #Panel Gelerias
        FieldPanel('bio', classname="full"),
        FieldPanel('banner_title4', classname="full"),
        FieldPanel('banner_title5', classname="full"),
        FieldPanel('banner_title6', classname="full"),
        FieldPanel('banner_title7', classname="full"),
        FieldPanel('banner_title8', classname="full"),
        FieldPanel('banner_title9', classname="full"),
        FieldPanel('banner_title10', classname="full"),
        FieldPanel('banner_title11', classname="full"),

#panel para campos de consulta
        FieldPanel('consulta', classname="full"),

        InlinePanel('galleria_1', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
#Panel capo de noticas
        FieldPanel("custom_title"),
    ]

  #  def get_context(self, request, *args, **kwargs):
   #     context = super().get_context(request, *args, **kwargs)
    #    context["posts"] = NewsDetailPage.objects.live().public()
    #    return context
        

class GaleriadeImagenes_1(Orderable):
    page = ParentalKey(History, on_delete=models.CASCADE, related_name='galleria_1')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de Juan Silva Photo')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
    image_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 2')
    image_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 3')

    # Imagenes Thumb Portfolio
    
    image_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Advertising Thumb-Galeria')
    image_5 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Product Thumb2-Galeria')
    image_6 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Documentary Thumb3-Galeria')
    
     

    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('image'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image_3'),
        ImageChooserPanel('image_4'),
        ImageChooserPanel('image_5'),
        ImageChooserPanel('image_6'),
    ]


# pagina de inicio
class consultas_2(AbstractFormField):
    page = ParentalKey('Charms', on_delete=models.CASCADE, related_name='form_fields')

class Charms(AbstractEmailForm):
    # Empieza Barner de Inicio
    template = "webapp_v10/charms.html"
    #cliente_Navbar = RichTextField(blank=True,verbose_name='Cliente-url')
    
   # banner_title1 = RichTextField(blank=True,verbose_name='Titulo del primer banner ')
   # banner_info1 = RichTextField(blank=True,verbose_name='Informacion del primer banner ')
   # banner_title2 = RichTextField(blank=True,verbose_name='Titulo del segundo banner ')
   # banner_info2 = RichTextField(blank=True,verbose_name='Informacion del segundo banner ')
   # banner_title3 = RichTextField(blank=True,verbose_name='Titulo del tercer banner ')
   # banner_info3 = RichTextField(blank=True,verbose_name='Informacion del tercer banner ')

    # Empieza Banner de Galerias
    bio = RichTextField(blank=True,verbose_name='rseña bibliografica')

    banner_title4 = RichTextField(blank=True,verbose_name='Titulo de galeria-1 ')
    banner_detail4 = models.CharField(max_length=1000,blank=True,verbose_name='detalle de galeria-1 ')
    banner_title5 = RichTextField(blank=True,verbose_name='Titulo de galeria-2  ')
    banner_detail5 =  models.CharField(max_length=1000,blank=True,verbose_name='detalle de galeria-2 ')
    banner_title6 = RichTextField(blank=True,verbose_name='Titulo de galeria-3  ')
    banner_detail6 = models.CharField(max_length=1000,blank=True,verbose_name='detalle de galeria-3 ')
    banner_title7 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')
    banner_detail7 =  models.CharField(max_length=1000,blank=True,verbose_name='detalle de galeria-4 ')
    banner_title8 = RichTextField(blank=True,verbose_name='Titulo de galeria-5  ')
    banner_detail8 =  models.CharField(max_length=1000,blank=True,verbose_name='detalle de galeria-5 ')
    banner_title9 = RichTextField(blank=True,verbose_name='Titulo de galeria-6  ')
    banner_detail9 =  models.CharField(max_length=1000,blank=True,verbose_name='detalle de galeria-6 ')
    banner_title10 = RichTextField(blank=True,verbose_name='Titulo de galeria-7  ')
    banner_detail10 =  models.CharField(max_length=1000,blank=True,verbose_name='detalle de galeria-7 ')
    banner_title11 = RichTextField(blank=True,verbose_name='Titulo de galeria-8  ')
    banner_detail11 =  models.CharField(max_length=1000,blank=True,verbose_name='detalle de galeria-8')
    banner_title12 = RichTextField(blank=True,verbose_name='Titulo de galeria-9  ')
    banner_detail12 =  models.CharField(max_length=1000,blank=True,verbose_name='detalle de galeria-9 ')
    banner_title13 = RichTextField(blank=True,verbose_name='Titulo de galeria-10  ')
    banner_detail13 =  models.CharField(max_length=1000,blank=True,verbose_name='detalle de galeria-10')
    banner_title14 = RichTextField(blank=True,verbose_name='Titulo de galeria-11 ')
    banner_detail14 =  models.CharField(max_length=1000,blank=True,verbose_name='detalle de galeria-11 ')
    banner_title15 = RichTextField(blank=True,verbose_name='Titulo de galeria-12  ')
    banner_detail15 =  models.CharField(max_length=1000,blank=True,verbose_name='detalle de galeria-12')

    
    #Campos de Noticias

    #template = "webapp_0/index.html"
    custom_title = models.CharField(max_length=100,blank=True,null=True,help_text="Reescribe el  Titulo de la publicacion ")


    
    # Campos de consulta

    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    # galeria de imagenes barner de presentacion

    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [

       # FieldPanel('title', classname="full"),
      #  FieldPanel('cliente_Navbar', classname="full"),
      #  FieldPanel('banner_info1', classname="full"),
      #  FieldPanel('banner_title2', classname="full"),
      #  FieldPanel('banner_info2', classname="full"),
      #  FieldPanel('banner_title3', classname="full"),
      #  FieldPanel('banner_info3', classname="full"),
    #Panel Gelerias
        FieldPanel('bio', classname="full"),
        FieldPanel('banner_title4', classname="full"),
        FieldPanel('banner_detail4', classname="full"),
        FieldPanel('banner_title5', classname="full"),
        FieldPanel('banner_detail5', classname="full"),
        FieldPanel('banner_title6', classname="full"),
        FieldPanel('banner_detail6', classname="full"),
        FieldPanel('banner_title7', classname="full"),
        FieldPanel('banner_detail7', classname="full"),
        FieldPanel('banner_title8', classname="full"),
        FieldPanel('banner_detail8', classname="full"),
        FieldPanel('banner_title9', classname="full"),
        FieldPanel('banner_detail9', classname="full"),
        FieldPanel('banner_title10', classname="full"),
        FieldPanel('banner_detail10', classname="full"),
        FieldPanel('banner_title11', classname="full"),
        FieldPanel('banner_detail11', classname="full"),
        FieldPanel('banner_title12', classname="full"),
        FieldPanel('banner_detail12', classname="full"),
        FieldPanel('banner_title13', classname="full"),
        FieldPanel('banner_detail13', classname="full"),
        FieldPanel('banner_title14', classname="full"),
        FieldPanel('banner_detail14', classname="full"),
        FieldPanel('banner_title15', classname="full"),
        FieldPanel('banner_detail15', classname="full"),

#panel para campos de consulta
        FieldPanel('consulta', classname="full"),

        InlinePanel('galleria_2', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
#Panel capo de noticas
        FieldPanel("custom_title"),
    ]

  #  def get_context(self, request, *args, **kwargs):
   #     context = super().get_context(request, *args, **kwargs)
    #    context["posts"] = NewsDetailPage.objects.live().public()
    #    return context
        

class GaleriadeImagenes_2(Orderable):
    page = ParentalKey(Charms, on_delete=models.CASCADE, related_name='galleria_2')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de Juan Silva Photo')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
    image_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 2')
    image_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 3')

    # Imagenes Thumb Portfolio
    
    image_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Advertising Thumb-Galeria')
    image_5 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Product Thumb2-Galeria')
    image_6 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Documentary Thumb3-Galeria')
    image_7 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 2')
    image_8 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 3')

    # Imagenes Thumb Portfolio
    
    image_9 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Advertising Thumb-Galeria')
    image_10 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Product Thumb2-Galeria')
    image_11 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Documentary Thumb3-Galeria')
    image_12 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 2')
  
    
     

    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('image'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image_3'),
        ImageChooserPanel('image_4'),
        ImageChooserPanel('image_5'),
        ImageChooserPanel('image_6'),
        ImageChooserPanel('image_7'),
        ImageChooserPanel('image_8'),
        ImageChooserPanel('image_9'),
        ImageChooserPanel('image_10'),
        ImageChooserPanel('image_11'),
        ImageChooserPanel('image_12'),
    ]



# pagina de inicio
class consultas_3(AbstractFormField):
    page = ParentalKey('Hosts', on_delete=models.CASCADE, related_name='form_fields')

class Hosts(AbstractEmailForm):
    # Empieza Barner de Inicio
    template = "webapp_v10/hosts.html"
    #cliente_Navbar = RichTextField(blank=True,verbose_name='Cliente-url')
    
   # banner_title1 = RichTextField(blank=True,verbose_name='Titulo del primer banner ')
   # banner_info1 = RichTextField(blank=True,verbose_name='Informacion del primer banner ')
   # banner_title2 = RichTextField(blank=True,verbose_name='Titulo del segundo banner ')
   # banner_info2 = RichTextField(blank=True,verbose_name='Informacion del segundo banner ')
   # banner_title3 = RichTextField(blank=True,verbose_name='Titulo del tercer banner ')
   # banner_info3 = RichTextField(blank=True,verbose_name='Informacion del tercer banner ')

    # Empieza Banner de Galerias
    bio = RichTextField(blank=True,verbose_name='rseña bibliografica')

    banner_title4 = RichTextField(blank=True,verbose_name='Titulo de galeria-1 ')
    banner_title5 = RichTextField(blank=True,verbose_name='Titulo de galeria-2  ')
    banner_title6 = RichTextField(blank=True,verbose_name='Titulo de galeria-3  ')
    banner_title7 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')


    
    #Campos de Noticias

    #template = "webapp_0/index.html"
    custom_title = models.CharField(max_length=100,blank=True,null=True,help_text="Reescribe el  Titulo de la publicacion ")


    
    # Campos de consulta

    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    # galeria de imagenes barner de presentacion

    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [

       # FieldPanel('title', classname="full"),
      #  FieldPanel('cliente_Navbar', classname="full"),
      #  FieldPanel('banner_info1', classname="full"),
      #  FieldPanel('banner_title2', classname="full"),
      #  FieldPanel('banner_info2', classname="full"),
      #  FieldPanel('banner_title3', classname="full"),
      #  FieldPanel('banner_info3', classname="full"),
    #Panel Gelerias
        FieldPanel('bio', classname="full"),
        FieldPanel('banner_title4', classname="full"),
        FieldPanel('banner_title5', classname="full"),
        FieldPanel('banner_title6', classname="full"),
        FieldPanel('banner_title7', classname="full"),
  

#panel para campos de consulta
        FieldPanel('consulta', classname="full"),

        InlinePanel('galleria_3', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
#Panel capo de noticas
        FieldPanel("custom_title"),
    ]

  #  def get_context(self, request, *args, **kwargs):
   #     context = super().get_context(request, *args, **kwargs)
    #    context["posts"] = NewsDetailPage.objects.live().public()
    #    return context
        

class GaleriadeImagenes_3(Orderable):
    page = ParentalKey(Hosts, on_delete=models.CASCADE, related_name='galleria_3')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de Juan Silva Photo')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
    image_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 2')
    image_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 3')

    # Imagenes Thumb Portfolio
    
    image_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Advertising Thumb-Galeria')



    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('image'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image_3'),
        ImageChooserPanel('image_4'),
      
    ]

# pagina de inicio
class consultas_4(AbstractFormField):
    page = ParentalKey('Host', on_delete=models.CASCADE, related_name='form_fields')

class Host(AbstractEmailForm):
    # Empieza Barner de Inicio
    template = "webapp_v10/host.html"
    #cliente_Navbar = RichTextField(blank=True,verbose_name='Cliente-url')
    
   # banner_title1 = RichTextField(blank=True,verbose_name='Titulo del primer banner ')
   # banner_info1 = RichTextField(blank=True,verbose_name='Informacion del primer banner ')
   # banner_title2 = RichTextField(blank=True,verbose_name='Titulo del segundo banner ')
   # banner_info2 = RichTextField(blank=True,verbose_name='Informacion del segundo banner ')
   # banner_title3 = RichTextField(blank=True,verbose_name='Titulo del tercer banner ')
   # banner_info3 = RichTextField(blank=True,verbose_name='Informacion del tercer banner ')

    # Empieza Banner de Galerias
   

    banner_title4 = RichTextField(blank=True,verbose_name='Titulo de galeria-1 ')
    bio = RichTextField(blank=True,verbose_name='rseña bibliografica')
    banner_title5 = RichTextField(blank=True,verbose_name='Titulo de galeria-2  ')
    banner_title6 = RichTextField(blank=True,verbose_name='Titulo de galeria-3  ')
    banner_title7 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')


    
    #Campos de Noticias

    #template = "webapp_0/index.html"
    custom_title = models.CharField(max_length=100,blank=True,null=True,help_text="Reescribe el  Titulo de la publicacion ")


    
    # Campos de consulta

    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    # galeria de imagenes barner de presentacion

    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [

       # FieldPanel('title', classname="full"),
      #  FieldPanel('cliente_Navbar', classname="full"),
      #  FieldPanel('banner_info1', classname="full"),
      #  FieldPanel('banner_title2', classname="full"),
      #  FieldPanel('banner_info2', classname="full"),
      #  FieldPanel('banner_title3', classname="full"),
      #  FieldPanel('banner_info3', classname="full"),
    #Panel Gelerias
        FieldPanel('bio', classname="full"),
        FieldPanel('banner_title4', classname="full"),
        FieldPanel('banner_title5', classname="full"),
        FieldPanel('banner_title6', classname="full"),
        FieldPanel('banner_title7', classname="full"),
  

#panel para campos de consulta
        FieldPanel('consulta', classname="full"),

        InlinePanel('galleria_4', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
#Panel capo de noticas
        FieldPanel("custom_title"),
    ]

  #  def get_context(self, request, *args, **kwargs):
   #     context = super().get_context(request, *args, **kwargs)
    #    context["posts"] = NewsDetailPage.objects.live().public()
    #    return context
        

class GaleriadeImagenes_4(Orderable):
    page = ParentalKey(Host, on_delete=models.CASCADE, related_name='galleria_4')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de Juan Silva Photo')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')

    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('image'),
    ]


class consultas_5(AbstractFormField):
    page = ParentalKey('Contacts', on_delete=models.CASCADE, related_name='form_fields')

class Contacts(AbstractEmailForm):
    # Empieza Barner de Inicio
    template = "webapp_v10/contacts.html"
    #cliente_Navbar = RichTextField(blank=True,verbose_name='Cliente-url')
    
   # banner_title1 = RichTextField(blank=True,verbose_name='Titulo del primer banner ')
   # banner_info1 = RichTextField(blank=True,verbose_name='Informacion del primer banner ')
   # banner_title2 = RichTextField(blank=True,verbose_name='Titulo del segundo banner ')
   # banner_info2 = RichTextField(blank=True,verbose_name='Informacion del segundo banner ')
   # banner_title3 = RichTextField(blank=True,verbose_name='Titulo del tercer banner ')
   # banner_info3 = RichTextField(blank=True,verbose_name='Informacion del tercer banner ')

    # Empieza Banner de Galerias
   

    banner_title4 = RichTextField(blank=True,verbose_name='Descripcion de la localizacion')
    bio = RichTextField(blank=True,verbose_name='rseña bibliografica')
    banner_title5 = RichTextField(blank=True,verbose_name='Email  ')
    banner_title6 = RichTextField(blank=True,verbose_name='Adress  ')
    banner_title7 = RichTextField(blank=True,verbose_name='phone number')


    
    #Campos de Noticias

    #template = "webapp_0/index.html"
    custom_title = models.CharField(max_length=100,blank=True,null=True,help_text="Reescribe el  Titulo de la publicacion ")


    
    # Campos de consulta

    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    # galeria de imagenes barner de presentacion

    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [

       # FieldPanel('title', classname="full"),
      #  FieldPanel('cliente_Navbar', classname="full"),
      #  FieldPanel('banner_info1', classname="full"),
      #  FieldPanel('banner_title2', classname="full"),
      #  FieldPanel('banner_info2', classname="full"),
      #  FieldPanel('banner_title3', classname="full"),
      #  FieldPanel('banner_info3', classname="full"),
    #Panel Gelerias
        FieldPanel('bio', classname="full"),
        FieldPanel('banner_title4', classname="full"),
        FieldPanel('banner_title5', classname="full"),
        FieldPanel('banner_title6', classname="full"),
        FieldPanel('banner_title7', classname="full"),
  

#panel para campos de consulta
        FieldPanel('consulta', classname="full"),

        InlinePanel('galleria_5', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
#Panel capo de noticas
        FieldPanel("custom_title"),
    ]

  #  def get_context(self, request, *args, **kwargs):
   #     context = super().get_context(request, *args, **kwargs)
    #    context["posts"] = NewsDetailPage.objects.live().public()
    #    return context
        

class GaleriadeImagenes_5(Orderable):
    page = ParentalKey(Contacts, on_delete=models.CASCADE, related_name='galleria_5')
    logo  = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Isla Florena')
    logo_1 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logo Isla Florena blanco')
    logo_0 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logo Isla Florena')
    logo_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logo 0')
    logo_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logo 1')
    logo_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logo 2')
    logo_5 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logo 3')
    logo_6 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logo 4')
    logo_7 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logo 5')

    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('logo_1'),
        ImageChooserPanel('logo_0'),
        ImageChooserPanel('logo_2'),
        ImageChooserPanel('logo_3'),
        ImageChooserPanel('logo_4'),
        ImageChooserPanel('logo_5'),
        ImageChooserPanel('logo_6'),
        ImageChooserPanel('logo_7'),
    ]




# pagina de inicio
class consultas_9(AbstractFormField):
    page = ParentalKey('worlds', on_delete=models.CASCADE, related_name='form_fields')

class Worlds(AbstractEmailForm):
    # Empieza Barner de Inicio
    template = "webapp_v10/worlds.html"
    #cliente_Navbar = RichTextField(blank=True,verbose_name='Cliente-url')
    
   # banner_title1 = RichTextField(blank=True,verbose_name='Titulo del primer banner ')
   # banner_info1 = RichTextField(blank=True,verbose_name='Informacion del primer banner ')
   # banner_title2 = RichTextField(blank=True,verbose_name='Titulo del segundo banner ')
   # banner_info2 = RichTextField(blank=True,verbose_name='Informacion del segundo banner ')
   # banner_title3 = RichTextField(blank=True,verbose_name='Titulo del tercer banner ')
   # banner_info3 = RichTextField(blank=True,verbose_name='Informacion del tercer banner ')

    # Empieza Banner de Galerias
    bio = RichTextField(blank=True,verbose_name='rseña bibliografica')

    banner_title4 = RichTextField(blank=True,verbose_name='Titulo de galeria-1 ')
    banner_title5 = RichTextField(blank=True,verbose_name='Titulo de galeria-2  ')
    banner_title6 = RichTextField(blank=True,verbose_name='Titulo de galeria-3  ')
    banner_title7 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')


    
    #Campos de Noticias

    #template = "webapp_0/index.html"
    custom_title = models.CharField(max_length=100,blank=True,null=True,help_text="Reescribe el  Titulo de la publicacion ")


    
    # Campos de consulta

    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    # galeria de imagenes barner de presentacion

    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [

       # FieldPanel('title', classname="full"),
      #  FieldPanel('cliente_Navbar', classname="full"),
      #  FieldPanel('banner_info1', classname="full"),
      #  FieldPanel('banner_title2', classname="full"),
      #  FieldPanel('banner_info2', classname="full"),
      #  FieldPanel('banner_title3', classname="full"),
      #  FieldPanel('banner_info3', classname="full"),
    #Panel Gelerias
        FieldPanel('bio', classname="full"),
        FieldPanel('banner_title4', classname="full"),
        FieldPanel('banner_title5', classname="full"),
        FieldPanel('banner_title6', classname="full"),
        FieldPanel('banner_title7', classname="full"),
  

#panel para campos de consulta
        FieldPanel('consulta', classname="full"),

        InlinePanel('galleria_7', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
#Panel capo de noticas
        FieldPanel("custom_title"),
    ]

  #  def get_context(self, request, *args, **kwargs):
   #     context = super().get_context(request, *args, **kwargs)
    #    context["posts"] = NewsDetailPage.objects.live().public()
    #    return context
        

class GaleriadeImagenes_7(Orderable):
    page = ParentalKey(Worlds, on_delete=models.CASCADE, related_name='galleria_7')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de Juan Silva Photo')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
    image_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 2')
    image_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 3')

    # Imagenes Thumb Portfolio
    
    image_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Advertising Thumb-Galeria')



    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('image'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image_3'),
        ImageChooserPanel('image_4'),
      
    ]



# pagina de inicio
class consultas_7(AbstractFormField):
    page = ParentalKey('Environs', on_delete=models.CASCADE, related_name='form_fields')

class Environs(AbstractEmailForm):
    # Empieza Barner de Inicio
    template = "webapp_v10/environs.html"
    #cliente_Navbar = RichTextField(blank=True,verbose_name='Cliente-url')
    
   # banner_title1 = RichTextField(blank=True,verbose_name='Titulo del primer banner ')
   # banner_info1 = RichTextField(blank=True,verbose_name='Informacion del primer banner ')
   # banner_title2 = RichTextField(blank=True,verbose_name='Titulo del segundo banner ')
   # banner_info2 = RichTextField(blank=True,verbose_name='Informacion del segundo banner ')
   # banner_title3 = RichTextField(blank=True,verbose_name='Titulo del tercer banner ')
   # banner_info3 = RichTextField(blank=True,verbose_name='Informacion del tercer banner ')

    # Empieza Banner de Galerias
    bio = RichTextField(blank=True,verbose_name='rseña bibliografica')

    banner_title4 = RichTextField(blank=True,verbose_name='Titulo de galeria-1 ')
    banner_title5 = RichTextField(blank=True,verbose_name='Titulo de galeria-2  ')
    banner_title6 = RichTextField(blank=True,verbose_name='Titulo de galeria-3  ')
    banner_title7 = RichTextField(blank=True,verbose_name='Next  ')
    banner_title8 = RichTextField(blank=True,verbose_name='Prev ')
    banner_title9 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')
    banner_title10 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')
    banner_title11 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')
    next = models.CharField(max_length=150, null=True, blank=True,verbose_name='Next')
    prev = models.CharField(max_length=150, null=True, blank=True,verbose_name='Prev')




    # Empieza Banner de Tearsheet
    TS_info1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-1 info')
    TS_date1 = models.DateField("Fecha de Tearsheet-1",null=True, blank=True)
    TS_info2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-2 info')
    TS_date2 = models.DateField("Fecha de Tearsheet-2",null=True, blank=True)
    TS_info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-3 info')
    TS_date3 = models.DateField("Fecha de Tearsheet-3",null=True, blank=True)
    TS_info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-4 info')
    TS_date4 = models.DateField("Fecha de Tearsheet-4",null=True, blank=True)
    TS_info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-5 info')
    TS_date5 = models.DateField("Fecha de Tearsheet-5",null=True, blank=True)
    TS_info6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-6 info')
    TS_date6 = models.DateField("Fecha de Tearsheet-6",null=True, blank=True)
    TS_info7 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-7 info')
    TS_date7 = models.DateField("Fecha de Tearsheet-7",null=True, blank=True)
    TS_info8 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-8 info')
    TS_date8 = models.DateField("Fecha de Tearsheet-8",null=True, blank=True)
    TS_info9 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-9 info')
    TS_date9 = models.DateField("Fecha de Tearsheet-9",null=True, blank=True)
    TS_info10 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-10 info')
    TS_date10 = models.DateField("Fecha de Tearsheet-10",null=True, blank=True)
    TS_info11 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-11 info')
    TS_date11 = models.DateField("Fecha de Tearsheet-11",null=True, blank=True)
    TS_info12 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-12 info')
    TS_date12 = models.DateField("Fecha de Tearsheet-12",null=True, blank=True)
    TS_info13 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-13 info')
    TS_date13 = models.DateField("Fecha de Tearsheet-13",null=True, blank=True)
    TS_info14 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-14 info')
    TS_date14 = models.DateField("Fecha de Tearsheet-14",null=True, blank=True)
    TS_info15 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-15 info')
    TS_date15 = models.DateField("Fecha de Tearsheet-15",null=True, blank=True)
    TS_info16 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-16 info')
    TS_date16 = models.DateField("Fecha de Tearsheet-16",null=True, blank=True)
    TS_info17 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-17 info')
    TS_date17 = models.DateField("Fecha de Tearsheet-17",null=True, blank=True)
    TS_info18 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-18 info')
    TS_date18 = models.DateField("Fecha de Tearsheet-18",null=True, blank=True)
    TS_info19 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-19 info')
    TS_date19 = models.DateField("Fecha de Tearsheet-19",null=True, blank=True)
    TS_info20 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Tearsheet-20 info')
    TS_date20 = models.DateField("Fecha de Tearsheet-20",null=True, blank=True)
    
    #Campos de Noticias

    #template = "webapp_0/index.html"
    custom_title = models.CharField(max_length=100,blank=True,null=True,help_text="Reescribe el  Titulo de la publicacion ")


    
    # Campos de consulta

    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    # galeria de imagenes barner de presentacion

    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [

       # FieldPanel('title', classname="full"),
      #  FieldPanel('cliente_Navbar', classname="full"),
      #  FieldPanel('banner_info1', classname="full"),
      #  FieldPanel('banner_title2', classname="full"),
      #  FieldPanel('banner_info2', classname="full"),
      #  FieldPanel('banner_title3', classname="full"),
      #  FieldPanel('banner_info3', classname="full"),
    #Panel Gelerias
        FieldPanel('bio', classname="full"),
        FieldPanel('banner_title4', classname="full"),
        FieldPanel('banner_title5', classname="full"),
        FieldPanel('banner_title6', classname="full"),
        FieldPanel('banner_title7', classname="full"),
        FieldPanel('banner_title8', classname="full"),
        FieldPanel('banner_title9', classname="full"),
        FieldPanel('banner_title10', classname="full"),
        FieldPanel('banner_title11', classname="full"),
    #Tearsheet Info
        FieldPanel('next', classname="full"),
        FieldPanel('prev', classname="full"),
        FieldPanel('TS_info1', classname="full"),
        FieldPanel('TS_date1', classname="full"),
        FieldPanel('TS_info2', classname="full"),
        FieldPanel('TS_date2', classname="full"),
        FieldPanel('TS_info3', classname="full"),
        FieldPanel('TS_date3', classname="full"),
        FieldPanel('TS_info4', classname="full"),
        FieldPanel('TS_date4', classname="full"),
        FieldPanel('TS_info5', classname="full"),
        FieldPanel('TS_date5', classname="full"),
        FieldPanel('TS_info6', classname="full"),
        FieldPanel('TS_date6', classname="full"),
        FieldPanel('TS_info7', classname="full"),
        FieldPanel('TS_date7', classname="full"),
        FieldPanel('TS_info8', classname="full"),
        FieldPanel('TS_date8', classname="full"),
        FieldPanel('TS_info9', classname="full"),
        FieldPanel('TS_date9', classname="full"),
        FieldPanel('TS_info10', classname="full"),
        FieldPanel('TS_date10', classname="full"),
        FieldPanel('TS_info11', classname="full"),
        FieldPanel('TS_date11', classname="full"),
        FieldPanel('TS_info12', classname="full"),
        FieldPanel('TS_date12', classname="full"),
        FieldPanel('TS_info13', classname="full"),
        FieldPanel('TS_date13', classname="full"),
        FieldPanel('TS_info14', classname="full"),
        FieldPanel('TS_date14', classname="full"),
        FieldPanel('TS_info15', classname="full"),
        FieldPanel('TS_date15', classname="full"),
        FieldPanel('TS_info16', classname="full"),
        FieldPanel('TS_date16', classname="full"),
        FieldPanel('TS_info17', classname="full"),
        FieldPanel('TS_date17', classname="full"),
        FieldPanel('TS_info18', classname="full"),
        FieldPanel('TS_date18', classname="full"),
        FieldPanel('TS_info19', classname="full"),
        FieldPanel('TS_date19', classname="full"),
        FieldPanel('TS_info20', classname="full"),
        FieldPanel('TS_date20', classname="full"),
#panel para campos de consulta
        FieldPanel('consulta', classname="full"),

        InlinePanel('galleria_6', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas_7"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
#Panel capo de noticas
        FieldPanel("custom_title"),
    ]

  #  def get_context(self, request, *args, **kwargs):
   #     context = super().get_context(request, *args, **kwargs)
    #    context["posts"] = NewsDetailPage.objects.live().public()
    #    return context
        

class GaleriadeImagenes_6(Orderable):
    page = ParentalKey(Environs, on_delete=models.CASCADE, related_name='galleria_6')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de Juan Silva Photo')
    profile_pic = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto de perfil')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
    image_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 2')
    image_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 3')

    # Imagenes Thumb Portfolio
    
    image_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Advertising Thumb-Galeria')
    image_5 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Product Thumb2-Galeria')
    image_6 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Documentary Thumb3-Galeria')
    image_7 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Landscape Thumb4-Galeria')

    # Fotos TearSheate
    image_8 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-1')
    image_9 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-2')
    image_10 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-3')
    image_11 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-4')
    image_12 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-5 ')
    image_13 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-6')
    image_14 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-7')
    image_15 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-8')
    image_16 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-9')
    image_17 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-10')
    image_18 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-11')
    image_19 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-12')
    image_20 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-13')
    image_21 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-14')
    image_22 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-15')
    image_23 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-16')
    image_24 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-17')
    image_25 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-18')
    image_26 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-19')
    image_27 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Tear-Sheet-20')
     

    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('profile_pic'),
        ImageChooserPanel('image'),
        ImageChooserPanel('image_2'),
        ImageChooserPanel('image_3'),
        ImageChooserPanel('image_4'),
        ImageChooserPanel('image_5'),
        ImageChooserPanel('image_6'),
        ImageChooserPanel('image_7'),
        ImageChooserPanel('image_8'),
        ImageChooserPanel('image_9'),
        ImageChooserPanel('image_10'),
        ImageChooserPanel('image_11'),
        ImageChooserPanel('image_12'),
        ImageChooserPanel('image_13'),
        ImageChooserPanel('image_14'),
        ImageChooserPanel('image_15'),
        ImageChooserPanel('image_16'),
        ImageChooserPanel('image_17'),
        ImageChooserPanel('image_18'),
        ImageChooserPanel('image_19'),
        ImageChooserPanel('image_20'),
        ImageChooserPanel('image_21'),
        ImageChooserPanel('image_22'),
        ImageChooserPanel('image_23'),
        ImageChooserPanel('image_24'),
        ImageChooserPanel('image_25'),
        ImageChooserPanel('image_26'),
        ImageChooserPanel('image_27'),
        
    ]

@register_setting
class SocialMediaSettings_v10(BaseSetting):
    facebook = models.URLField(blank=True,null=True,help_text="")
    twitter = models.URLField(blank=True,null=True,help_text="")
    instagram = models.URLField(blank=True,null=True,help_text="")
    youtube = models.URLField(blank=True,null=True,help_text="")

    panels = [
        MultiFieldPanel(
            [
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("instagram"),
            FieldPanel("youtube"),           
            ]
        ,heading= "Social Media Settings")
    ]