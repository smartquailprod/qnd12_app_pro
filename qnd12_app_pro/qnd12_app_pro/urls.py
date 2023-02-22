
#from django.contrib import admin
from django.urls import path,re_path,include
from django.conf import settings
from baton.autodiscover import admin
#from courses.views import CourseListView
from django.contrib.auth import views as auth_views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from qr_code import urls as qr_code_urls
from django.conf.urls.i18n import i18n_patterns

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('ofertas/', include('comercial.urls', namespace='ofertas')),
    #path('Orders/', include('orders.urls', namespace='orders')),
    path('Contracts/', include('legal.urls', namespace='contracts')),
    #path('services/', include('services.urls', namespace="services")),
    path('qr-code/', include(qr_code_urls, namespace="qr_code")),
    #E-commerce-configs
    #path('coupons/', include('coupons.urls', namespace='coupons')),
    #path('cart/', include('cart.urls', namespace='cart')),
    #path('orders/', include('orders.urls', namespace='orders')),
    #path('payment/', include('payment.urls', namespace='payment')),
    #path('shop/', include('shop.urls', namespace='shop')),
    #Eduaction Platform
   # path('account/', include('account.urls')),
    #path('account/login/', auth_views.LoginView.as_view(), name='login'),
    #path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('course/', include('courses.urls')),
    #path('course_list', CourseListView.as_view(), name='course_list'),
    #path('students/', include('students.urls')),
    #path('api/', include('courses.api.urls', namespace='api')),
    #path('social-auth/', include('social_django.urls', namespace='social')),
    
     
   

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
urlpatterns += i18n_patterns(
     re_path(r'^smartbusinessmedia/', include(wagtailadmin_urls),name='wagtail'),
     re_path(r'^documents/', include(wagtaildocs_urls)),
     re_path(r'', include(wagtail_urls)),
     prefix_default_language=False,
)