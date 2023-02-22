from .base import *

DEBUG=  "0"


BATON = {
    'SITE_HEADER': '<a href="#"><img src="https://qnd41-staticfiles.sfo3.digitaloceanspaces.com/static/img/m2.png" height="26px"></a>',
    'SITE_TITLE': '',
    'INDEX_TITLE': 'TODO EN ORDEN CLEAN & BUILDING CIA. LTDA.- BUSINESS ANALITYCS CONSULTING',
    'SUPPORT_HREF': '#',
    'COPYRIGHT': '<a href="#"><img src="https://qnd41-staticfiles.sfo3.digitaloceanspaces.com/static/img/m2.png" height="18px"></a>&nbsp;&nbsp; copyright © 2022', # noqa
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
    'LOGIN_SPLASH': 'https://qnd41-staticfiles.sfo3.digitaloceanspaces.com/static/img/login_splash.jpg',
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



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3')
    }
}

DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_IS_AVIAL = all([
    DB_USERNAME,
    DB_PASSWORD,
    DB_DATABASE,
    DB_HOST,
    DB_PORT
])

POSTGRES_READY="1"
if DB_IS_AVIAL and POSTGRES_READY:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_DATABASE,
        "USER": DB_USERNAME,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    }
}

#Static files DevMod

MEDIA_URL = "/media/"
MEDIA_ROOT  = os.path.join(BASE_DIR, 'mediafiles')
#STATICFILES_DIRS = [BASE_DIR / "staticfiles"]  
#STATIC_ROOT = STATIC_ROOT = BASE_DIR / "static"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 #Deploy Project- Don`t touch 
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles-cdn"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

from .cdn.conf import * #noqa