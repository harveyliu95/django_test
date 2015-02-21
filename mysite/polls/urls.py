from django.conf.urls import patterns, url

from polls import views

"""
### Tutorial 3 and before

urlpatterns = patterns('',
    #ex: /polls/
    url(r'^$', views.index, name='index'),
    #ex: /polls/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    #ex: /polls/5/results
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    #ex: /polls/5/vote
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)
"""

### tutorial 4, apply generic view
urlpatterns = patterns('',
    #ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #ex: /polls/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #ex: /polls/5/results
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #ex: /polls/5/vote
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)