from .base import *

DEBUG=  "1"




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
    }
}



BATON = {
    'SITE_HEADER': '<a href="#"><img src="/static/img/m2.png" height="26px"></a>',
    'SITE_TITLE': '',
    'INDEX_TITLE': 'TODO EN ORDEN CLEAN & BUILDING CIA. LTDA.- BUSINESS ANALITYCS CONSULTING',
    'SUPPORT_HREF': '#',
    'COPYRIGHT': '<a href="#"><img src="/static/img/m2.png" height="18px"></a>&nbsp;&nbsp; copyright © 2022', # noqa
    'POWERED_BY': '<a href="#"><img src="/static/img/logo_smartquailgray.png" height="13px"</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'MENU_ALWAYS_COLLAPSED': True,
    'MENU_TITLE': 'Todo en Orden',
    'MESSAGES_TOASTS': False,
    'GRAVATAR_DEFAULT_IMG': 'retro',
    'LOGIN_SPLASH': '/static/img/login_splash.jpg',
    'SEARCH_FIELD': {
        'label': 'Search contents...',
         'url': '/search/',
    },
    'MENU': (
        { 'type': 'title', 'label': 'Gerencia', 'apps': ('auth','todo_en_orden', ) },
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },
         {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Dpto Contable',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
        {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Dpto Operativo',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
         {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Dpto RRHH',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
        {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Dpto Legal',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
        {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Dpto Marketing',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
         { 'type': 'title', 'label': 'Administración Operativa', 'apps': ('auth','todo_en_orden', ) },
              {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Entradas y salidas',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
         {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Propuestas',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
         {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Servicios',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
        {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Kardex por Venta',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
         {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Kardex por Contrato ',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
                 {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Contratos ',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },

         {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Kardex de herramientas ',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },

          
        
        { 'type': 'title', 'label': 'Administración Contable', 'apps': ('auth','todo_en_orden', ) },
              {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Cuentas por cobrar',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
         {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Cuentas por pagar',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
         {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Egresos',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
        {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'venta de Insumos',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
         {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Facturación',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },

        {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Nómina',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },

                {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'IESS',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },

          {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Bancos',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Banco Guayaquil'
                },
                {
                    'name': 'order',
                    'label': 'Banco Internacional'
                },
            )
        },
              
    ),
}



ADMINS= (
    ('SILVA MAU', 'smartquail.dev@gmail.com')
)

ALLOWED_HOSTS = ['*']

#Static files DevMod

MEDIA_URL = "/media/"
MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [BASE_DIR / "staticfiles"]  
STATIC_URL = "/static/"
STATIC_ROOT = STATIC_ROOT = BASE_DIR / "static"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

