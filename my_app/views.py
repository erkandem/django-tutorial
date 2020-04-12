from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from  .models import Question

def index(request):
    """shows the first five questions by default"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'my_app/index.html', context)

def detail(request, question_id):
    return HttpResponse(
        "Your're looking at question `%s`." % question_id
    )
def results(request, question_id):
    return HttpResponse(
        "Your're looking at results of question `%s`." % question_id
    )
def vote(requset, question_id):
    return HttpResponse(
        "You're voting on question `%s`." % question_id
    )
