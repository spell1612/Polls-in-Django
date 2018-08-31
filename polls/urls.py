from django.urls import path

from . import views

app_name='polls' #This is cause there might othher apps with same url name, so a common template should be able to recognize. This is called namespacing
urlpatterns = [
    # path('', views.firstfun,name='index'),
    path('', views.firstfun.as_view(), name='index'),
    # path('<int:question_id>/',views.details,name='details'), #question_id will have the question number, ie link will be polls/5 if its qno 5
    path('<int:pk>/', views.DetailView.as_view(), name='details'),
    # path('<int:question_id>/results/',views.results,name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),#return the primary key as pk as generic DetailView looks for pk as arg
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
