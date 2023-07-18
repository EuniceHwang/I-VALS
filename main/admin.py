from django.contrib import admin
from .models import Type, Question, Choice

admin.site.register(Type)
admin.site.register(Question)
admin.site.register(Choice)