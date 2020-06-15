from django.shortcuts import render
import json

from django.views import View
from django.http  import JsonResponse
from django.http  import HttpResponse
from .models import Comment

class CommentView(View):

    def get(self, request):

        comment = Comment.objects.filter(id=1)

        data = {
            "nickname": comment[0].user.nickname,
            "comment" : comment[0].comment
        }

        return JsonResponse({'data':data}, status=200)


# Create your views here.
