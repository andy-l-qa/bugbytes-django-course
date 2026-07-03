from django.db.models import F
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Question, Choice

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

    # return HttpResponse("You're looking at question %s." % question_id)

    # try:
    #     question = Question.objects.get(id=question_id)
    # except:
    #     raise Http404("Question does not exist")

    questions = get_list_or_404(Question, id__in=[1,2,3])
    print(questions)

    question = get_object_or_404(Question, id=question_id)

    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    # respose = "You're looking at the results of question %s."
    # return HttpResponse(respose % question_id)

    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)

    print(request.POST)

    question = get_object_or_404(Question, id=question_id)

    try:
        choice_pk = request.POST['choice']
        selected_choice = question.choice_set.get(pk=choice_pk)
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            "error_message": "You didn't select a choice." 
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes = F("votes") + 1 
        # F does the update DIRECTLY on the server, preventing two users to send same value at the same time
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))