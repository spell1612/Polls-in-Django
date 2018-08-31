from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice,Question

# Create your views here.
# def firstfun(request):
#     qdatelist=Question.objects.order_by('-pub_date')[:5] #wow a list from 0-4 (an array of objects) made from the return o a function call!
#     # response=',\n'.join([pro.ques_text for pro in qdatelist] )  #notice this is a list inside the join function! the \n doesnt do anything, need to find replacement
#     #in the pro.ques_text the obj "pro" can be anything for some reason. O_O python is weird
#     context={
#         'latestqlist':qdatelist,  #this is a dictionary
#         # 'debug':"nobugs"
#     }
#     return render(request,'polls/index.html',context) #render() for templates HttpResponse() for single line responses

class firstfun(generic.ListView):
    template_name='polls/index.html'
    context_object_name ='latestqlist'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

# def details(request,question_id):
#     # try:
#     #     q=Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("The requested page does not exist")
#     q=get_object_or_404(Question,pk=question_id) #this works instead of commented code
#     return render(request, 'polls/details.html',{'question':q}) #inline context
#     # There’s also a get_list_or_404() function, which works just as get_object_or_404() – except using filter() instead of get(). It raises Http404 if the list is empty.

class DetailView(generic.DetailView):
    model=Question
    template_name='polls/details.html'


# def results(request, question_id):
#     q=get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/results.html',{'question':q})

class ResultsView(generic.DetailView):
    model=Question
    template_name='polls/results.html'

# In generic.DetailView the context variable name is chosen by default as the model name with no first letter capitalization

def vote(request, question_id):
    q=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=q.choice_set.get(pk=request.POST['choice']) #request.POST['choice'] is same as using the name of the field in laravel (for comparison). Its value will be the choice.id that was clicked on
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html',{'question':q,'error_message': "You didn't select a choice."}) # Redisplay the question voting form.
    else:
        selected_choice.votes +=1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(q.id,))) #notice that args takes a 1 tuple, ie (q.id, <empty>) not an integer
