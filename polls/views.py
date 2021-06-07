from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from polls.serializers.question import QuestionSerializer
from polls.models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_test for q in latest_question_list])
    # return HttpResponse(output)
    tempfile = loader.get_template('index.html')
    context = {
        'latest_question_list' : latest_question_list
    }
    return HttpResponse(tempfile.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'result.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def questionAPI(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    data = {"result": list(latest_question_list.values( "question_test", "pub_date" ))
            }

    return JsonResponse( data, safe=False)