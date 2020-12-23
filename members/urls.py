from django.conf.urls import url

from members import views

urlpatterns = [
    # api
    url(r'^api/v1/team-members$', views.team, name='team'),
    url(r'^api/v1/team-members/(?P<pk>[0-9]+)$', views.team_member, name='team_member')
]
