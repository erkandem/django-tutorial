from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from  .models import Question

def index(request):
    """shows the first five questions by default"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('my_app/index.html')
    context = {'latest_question_list': latest_question_list}
    return HttpResponse(
        template.render(context, request)
    )

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
