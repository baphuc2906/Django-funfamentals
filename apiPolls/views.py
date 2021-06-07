from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import Question
from .serializers import QuestionSerializer


class QuestionList(APIView):

    permission_classes = [IsAuthenticated]
    def get(self, request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        serializer = QuestionSerializer(latest_question_list, many= True)
        return Response(serializer.data)