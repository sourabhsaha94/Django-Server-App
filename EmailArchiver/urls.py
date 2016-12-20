from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.login,name='index'),
	url(r'^register/$', views.register, name ='register'),
    	url(r'^(?P<pk>[0-9]+)/$',views.details, name = 'details'),
]
