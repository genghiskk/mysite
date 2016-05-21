from .models import Question, todo, person

from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ('todo_id', 'todo_desc', 'todo_updatetext', 'todo_type', 'todo_assignee', 'todo_assigner', 'todoassign_date', 'todoupdate_date', 'todocomplete_date')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = person
        fields = ('person_id', 'person_FName', 'person_LName', 'person_role', 'person_Phone','person_Addr1', 'person_Addr2', 'person_City', 'person_State', 'person_Zip')
              