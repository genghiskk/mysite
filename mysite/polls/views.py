from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Question, todo, person


from django.http import Http404

from polls.serializers import TodoSerializer
from polls.serializers import QuestionSerializer
from polls.serializers import  PersonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import mysql.connector
from mysql.connector import MySQLConnection, Error
import logging, sys


@api_view()
def ToDoList(request):
        
        parm1 = request.GET.get('todo_id')
        Todoobj = todo.objects.filter(todo_id=parm1)
        serializer = TodoSerializer(Todoobj, many=True)
        return Response(serializer.data)

class QuestionList(APIView):

# List all users, or create a new user.

    def get(self, request, format=None):
      
        Questions = Question.objects.all()
        serializer = QuestionSerializer(Questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class PersonList(APIView):

# List all users, or create a new user.

    def get(self, request, format=None):
        Personobj = person.objects.all()
        serializer = PersonSerializer(Personobj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'details.html', {'question': question})




# Create your views here.


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

