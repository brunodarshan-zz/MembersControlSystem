from django.conf.urls import url
from . import views
from namespaces import members

urlpatterns = [
	url(r'^dashboard/$', views.dashboard, name='dashboard'),

	url(r'^actuations/actuations_list/$', views.actuations_list, name='actuations_list'),
	url(r'^actuations/add_actuation/$', views.add_actuation, name='add_actuation'),

	url(r'members/$', members)

	url(r'^instituitions/instituitions_list/$', views.instituitions_list, name='instituitions_list'),
	url(r'^instituitions/add_instituition/$', views.add_instituition, name='add_instituition'),
	url(r'^instituitions/(?P<pk>\d+)/instituition_remove/$', views.instituition_remove, name='instituition_remove'),
	url(r'^instituitions/(?P<pk>\d+)/instituition_edit/$', views.instituition_edit, name='instituition_edit'),

	url(r'^positions/add_position/$', views.add_position, name='add_position'),
	url(r'^positions/positions_list/$', views.positions_list, name='positions_list'),
	url(r'^positions/(?P<pk>\d+)/position_remove/$', views.position_remove, name='position_remove'),
	url(r'^positions/(?P<pk>\d+)/position_edit/$', views.position_edit, name='position_edit'),

	url(r'^actuations/(?P<pk>\d+)/actuation_remove/$', views.actuation_remove, name='actuation_remove'),
	url(r'^actuations/(?P<pk>\d+)/actuation_edit/$', views.actuation_edit, name='actuation_edit'),

	url(r'^specialties/specialties_list/$', views.specialties_list, name='specialties_list'),
	url(r'^specialties/(?P<pk>\d+)/specialty_remove/$', views.specialty_remove, name='specialty_remove'),
	url(r'^specialties/(?P<pk>\d+)/specialty_edit/$', views.specialty_edit, name='specialty_edit'),
	url(r'^specialties/add_specialty/$', views.add_specialty, name='add_specialty'),

	url(r'^extras/add_extras/$', views.add_extras, name='add_extras'),
	url(r'^extras/view_extras/$', views.view_extras, name='view_extras'),

	url(r'^about/$', views.about, name='about'),
]
