from django.shortcuts import HttpResponse
from .models import Answer
from .models import Question
from django.shortcuts import render

# Create your views here.
def index(request):
    latest_question_list = Answer.objects.order_by('question_id')
    output = ', '.join([q.choice_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def llista(request):
    items = None
    if request.GET.get("qid"):
        items = Answer.objects.filter( question__id=request.GET["qid"] )
    else:
        items = Answer.objects.all()
    return render( request, "llista.html",
                    {
                        "tipus":"coses",
                        "elements":items
                    }
                )