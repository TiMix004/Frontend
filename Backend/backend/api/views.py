import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .Scripts import DMS

@csrf_exempt
def add_User(request):
    print(request.method)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)

            first_name = data["firstname"]
            last_name = data["lastname"]
            username = data["username"]
            email = data["email"]
            password = data["password"]
            date_of_birth = data["date_of_birth"]

            answer = DMS.add_User(first_name, last_name, username, email, password, date_of_birth)
            return JsonResponse(answer, safe = False)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status = 400)
    
    return JsonResponse({'error': 'Invalid reqeust method'}, status = 405)
