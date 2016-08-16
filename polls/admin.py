from django.contrib import admin

from .models import Question, Choice

#Question registered in admin site for Question Management
admin.site.register(Question)
#Choice registered in admin site for Choices Management
admin.site.register(Choice)
