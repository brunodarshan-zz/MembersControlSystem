from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
	url(r'^members/members_list/$', views.members_list, name='members_list'),
	url(r'^instituitions/instituitions_list/$', views.instituitions_list, name='instituitions_list'),
	url(r'^positions/positions_list/$', views.positions_list, name='positions_list'),
	url(r'^actuations/actuations_list/$', views.actuations_list, name='actuations_list'),
	url(r'^specialties/specialties_list/$', views.specialties_list, name='specialties_list'),
	url(r'^members/add_member/$', views.add_member, name='add_member'),
	url(r'^instituitions/add_instituition/$', views.add_instituition, name='add_instituition'),
	url(r'^positions/add_position/$', views.add_position, name='add_position'),
	url(r'^actuations/add_actuation/$', views.add_actuation, name='add_actuation'),
	url(r'^specialties/add_specialty/$', views.add_specialty, name='add_specialty'),
	url(r'^about/$', views.about, name='about'),
]