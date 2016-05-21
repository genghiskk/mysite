from django.contrib import admin

from .models import Question, todo, person

admin.site.register(Question)
admin.site.register(todo)
admin.site.register(person)



# Register your models here.
