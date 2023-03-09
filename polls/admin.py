from django.contrib import admin
from nested_admin import NestedModelAdmin, NestedTabularInline
from .models import Question, Choice, Maps

admin.site.site_header = "QuizRPG"
admin.site.site_title = "ADM QuizRPG"
admin.site.index_title = "Bem-vindo ao QuizRPG"

class ChoiceInLine(NestedTabularInline):
    model = Choice
    extra = 3
    classes = ['colllapse']

class QuestionInline(NestedTabularInline):
    model = Question
    extra = 0
    ordering = ("pub_date",)
    fieldsets = [(None, {'fields': ['question_text']}),
            ('Adicionado há', {'fields': ['pub_date'], 'classes':
                ['collapse']}), ]
    inlines = [ChoiceInLine]
    classes = ['collapse']

class MapsAdmin(NestedModelAdmin):
    #print(Maps.objects.exists())
    model = Maps
    classes = ['collapse']
    inlines =[QuestionInline]
    fieldsets = [(None, {'fields': ['maps_text']}),('Informação do mapa', {'fields':['accesses','difficulty'], 'classes':['collapse']}),]


admin.site.register(Maps, MapsAdmin)
#admin.site.register(
#admin.site.register(Question)
#admin.site.register(Choice)
# Register your models here.
