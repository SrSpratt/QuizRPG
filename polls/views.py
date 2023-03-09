from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Question, Maps, Choice
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    latest_question_list = Maps.objects.order_by('-difficulty')[:2]
    context = {'question':1, 'latest_question_list':latest_question_list,}    
    return render(request, 'polls/index.html', context)

def detail(request, question_id, maps_id):
    try:
        maps = Maps.objects.get(pk=maps_id)
#        for q in Maps.objects.all().question_set.all():
#            if q:
#                question_id = q.pk
        question = Maps.objects.get(pk=maps_id).question_set.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question, 'maps':maps})

def results(request, maps_id):
    maps = get_object_or_404(Maps, pk=maps_id)
    return render(request, 'polls/results.html', {'maps': maps})

def vote(request, question_id, maps_id):
    question = get_object_or_404(Question, pk=question_id)
    maps = get_object_or_404(Maps, pk=maps_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', { 'question':question, 'maps':maps, 'error_message': "You didn't select a choice.",})
    else:
        a = False
        for q in Maps.objects.get(pk=maps_id).question_set.all()[:question_id]:
            if (q.pk > question_id):
                print("entrou no lugar certo")
                question = q
                print(question.id)
                a = True
                break
            
        if (a == False):
            selected_choice.votes +=1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results',kwargs={'maps_id':maps.id}))
        else:
            selected_choice.votes +=1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:detail', kwargs={'question_id':question.id, 'maps_id':maps.id,}))


