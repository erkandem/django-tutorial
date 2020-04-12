from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import  get_object_or_404
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Question
from .models import Choice


class IndexView(generic.ListView):
    """shows the first five questions by default"""
    template_name = 'my_app/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'my_app/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'my_app/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            'my_app/detail.html',
            {'question': question, 'error_message': 'Nothing selected'}
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('my_app:results', args=(question.id,)))
