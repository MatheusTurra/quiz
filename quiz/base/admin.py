from django.contrib import admin

# Register your models here.
from quiz.base.models import Questions

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("id", "enunciated", "available")