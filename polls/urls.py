from django.urls import path

from . import views

urlpatterns = [
    path('', views.firstfun,name='index'),
    path('<int:question_id>',views.details), #question_id will have the question number, ie link will be polls/5 if its qno 5
    path('<int:question_id>/results',views.results),
    path('<int:question_id>/vote',views.vote),
]
