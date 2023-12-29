from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from ad.models import Question
from django.template import loader


def index(request):
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('ad/index.html')
    context = {
        "last_question_list": last_question_list
    }
    return  HttpResponse(template.render(context,request))

def detail(request,question_id):
    return HttpResponse("Your question id is %d" % question_id)

def results(request,question_id):
    response = "You're looking at question id %s"
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question id %d" % question_id)
