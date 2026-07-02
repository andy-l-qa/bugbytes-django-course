from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    # processing - db, cache, rendering HTML template
    # print(type(request))
    # print(request.method)
    # print(request.user)
    # return HttpResponse("Hi, world. You're at polls index.")

    # get 5 most recently added questions from the db
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # output = ', '.join([q.question_text for q in latest_question_list])
    # template = loader.get_template('polls/index.html')
    # context = {'latest_question_list': latest_question_list}
    # return HttpResponse(template.render(context, request))

    context = {
        'latest_question_list': latest_question_list,
        'numbers': [1,2,3,4,5]
        }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    respose = "You're looking at the results of question %s."
    return HttpResponse(respose % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)