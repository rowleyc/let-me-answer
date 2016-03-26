"""urls file for answer_app"""

from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^success$', views.success, name='success'),
]
