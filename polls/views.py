from django.shortcuts import HttpResponse
from .models import Question

# Create your views here.
def firstfun(request):
    qdatelist=Question.objects.order_by('-pub_date')[:5] #wow a list from 0-4 (an array of objects) made from the return o a function call!
    response=',\n'.join([pro.ques_text for pro in qdatelist] )  #notice this is a list inside the join function! the \n doesnt do anything, need to find replacement
    return HttpResponse(response) #in the pro.ques_text the obj pro can be anything for some reason O_O python is weird

def details(request,question_id):
    return HttpResponse("You're looking at question number %s" %question_id)

def results(request, question_id):
    response="You're looking at result of question %s"
    return HttpResponse(response % question_id)
    
def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
