from django.shortcuts import render
from django.http import HttpResponse
# from .models import Question

# Create your views here.


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
     return render(request, 'patients/test.html')
