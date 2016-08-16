from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    #Main Menu url
    url(r'^$', views.IndexView.as_view(), name='index'),
    #Latest 5 Polls url(previously index)
    url(r'^lastPolls/$', views.LastPollsView.as_view(), name='lastPolls'),
    #Top 5 Voted url
    url(r'^mostVoted/$', views.MostVotedView.as_view(), name='mostVoted'),
    #Poll Form url
    url(r'^pollForm/$', views.CreateView.as_view(), name='pollForm'),
    #Successfull Poll Creation url
    url(r'^pollForm/createPoll/$', views.createPoll, name='createPoll'),
    #Failed Poll Creation url
    url(r'^pollForm/error/$', views.pollFormError, name='pollFormError'),
    #Poll details url
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #Poll with vote results url
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    #Vote url
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
