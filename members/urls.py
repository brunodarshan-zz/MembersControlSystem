from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^dashboard/$', views.dashboard, name='dashboard'),

	url(r'^actuations/$', views.actuations_list, name='actuations_list'),
	url(r'^actuations/add/$', views.add_actuation, name='add_actuation'),

	url(r'^members/$', views.members_list, name='members_list'),
	url(r'^members/add/$', views.add_member, name='add_member'),
	url(r'^members/(?P<pk>[0-9]+)/$',views.member_detail, name='member_detail'),
	url(r'^members/(?P<pk>\d+)/remove/$', views.member_remove, name='member_remove'),
	url(r'^members/(?P<pk>\d+)/edit/$', views.member_edit, name='member_edit'),

	url(r'^instituitions/$', views.instituitions_list, name='instituitions_list'),
	url(r'^instituitions/add/$', views.add_instituition, name='add_instituition'),
	url(r'^instituitions/(?P<pk>\d+)/remove/$', views.instituition_remove, name='instituition_remove'),
	url(r'^instituitions/(?P<pk>\d+)/edit/$', views.instituition_edit, name='instituition_edit'),

	url(r'^positions/add/$', views.add_position, name='add_position'),
	url(r'^positions/$', views.positions_list, name='positions_list'),
	url(r'^positions/(?P<pk>\d+)/remove/$', views.position_remove, name='position_remove'),
	url(r'^positions/(?P<pk>\d+)/edit/$', views.position_edit, name='position_edit'),

	url(r'^actuations/(?P<pk>\d+)/remove/$', views.actuation_remove, name='actuation_remove'),
	url(r'^actuations/(?P<pk>\d+)/edit/$', views.actuation_edit, name='actuation_edit'),

	url(r'^specialties/$', views.specialties_list, name='specialties_list'),
	url(r'^specialties/(?P<pk>\d+)/remove/$', views.specialty_remove, name='specialty_remove'),
	url(r'^specialties/(?P<pk>\d+)/edit/$', views.specialty_edit, name='specialty_edit'),
	url(r'^specialties/add/$', views.add_specialty, name='add_specialty'),

	url(r'^extras/add/$', views.add_extras, name='add_extras'),
	url(r'^extras/$', views.view_extras, name='view_extras'),

	url(r'^about/$', views.about, name='about'),
]
