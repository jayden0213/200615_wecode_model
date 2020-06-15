import json
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from .models import Users

class MainView(View):
    def post(self, request):
        data=json.loads(request.body)
        Users(
                name = data['name'],
                email = data['email'],
                nickname = data['nickname'],
                password = data['password']
                 ).save()

        return JsonResponse({'message':'SUCCESS'}, status=200)

    def get(self, request):
        return JsonResponse({"Hello":"World"}, status=200)




# Create your views here.
