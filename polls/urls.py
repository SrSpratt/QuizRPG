from django.contrib import admin
from django.urls import path
from . import views

app_name = 'polls'


urlpatterns = [
        path('', views.index, name='index'),
        path('<int:question_id>/<int:maps_id>/', views.detail, name='detail'),
        path('<int:maps_id>/results/', views.results, name='results'),
        path('<int:question_id>/<int:maps_id>/vote/', views.vote, name='vote')
        ]
