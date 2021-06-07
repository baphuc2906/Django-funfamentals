from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.QuestionList.as_view(), name='index'),
]