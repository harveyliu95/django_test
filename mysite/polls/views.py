
from django.shortcuts import render
from django.http import HttpResponse
#from django.template import RequestContext, loader

from polls.models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
#    template = loader.get_template('polls/index.html')
#    context = RequestContext(request, {
#        'latest_question_list' : latest_question_list,
#        })
    return render(request, 'polls/index.html', context)
#    return HttpResponse(template.render(context))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)

def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


###Raising a 404 error
#from django.http import Http404
from django.shortcuts import get_object_or_404, render

from polls.models import Question

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'polls/detail.html', {'question' = question})

    return render(request, 'polls/detail.html', {'question':question})
