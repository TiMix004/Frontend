import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .Scripts.DMS import *

@csrf_exempt
def get_items(request):
    if request.mthod == 'GET':
        print(request.method)

@csrf_exempt
def create_item(request):
    print(request.method)
    if request.mthod == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            name = data['name']
            answer = main(name)
            print (answer)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status = 400)
    
    return JsonResponse({'error': 'Invalid reqeust method'}, status = 405)
