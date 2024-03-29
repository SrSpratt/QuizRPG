from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Question, Maps

def index(request):
    latest_question_list = Maps.objects.order_by('-difficulty')[:2]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)
# Create your views here.

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, maps_id):
    question = get_object_or_404(Question, pk=maps_id)
    return render(request, 'polls/results.html', {'question': maps})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice, DoesNotExist):
        return render(request, 'polls/detail.html', { 'question':question, 'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:detail', args=(question.id+1,)))
