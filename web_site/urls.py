from django.conf.urls import patterns, url

from web_site import views

urlpatterns = patterns('',
                       url('export_csv/$', views.CustomerExport.as_view(), name='customer_export')
                       )
