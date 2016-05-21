from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
	



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class todo(models.Model):
    todo_id = models.IntegerField(default=0)
    todo_desc = models.CharField(max_length=256)
    todo_updatetext = models.CharField(max_length=256, blank=True, null=True)
    todo_type = models.CharField(max_length=15)
    todo_assignee = models.IntegerField(default=0)
    todo_assigner = models.IntegerField(default=0)
    todoassign_date = models.DateTimeField(blank=True, null=True)
    todoupdate_date = models.DateTimeField(blank=True, null=True)
    todocomplete_date = models.DateTimeField(blank=True, null=True)

class person(models.Model):
    person_id = models.IntegerField(default=0)
    person_FName = models.CharField(max_length=25)
    person_LName = models.CharField(max_length=25)
    person_role = models.CharField(max_length=10)
    person_Phone = models.CharField(max_length=12, blank=True, null=True)
    person_Addr1 = models.CharField(max_length=40, blank=True, null=True)
    person_Addr2 = models.CharField(max_length=40, blank=True, null=True)
    person_City = models.CharField(max_length=25, blank=True, null=True)
    person_State = models.CharField(max_length=2, blank=True, null=True)
    person_Zip = models.CharField(max_length=5, blank=True, null=True)



# Create your models here.
