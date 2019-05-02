from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from data_service.settings import BASE_DIR

@api_view(["GET"])
def codeToState(request):
    try:
        code = request.GET['code']
        f = open(BASE_DIR+'/json_reader/resources/states_hash.json')
        json_string = f.read()
        f.close()
        data = json.loads(json_string)

        result = 'No result'

        for key, value in data.items():
            if(key == code):
                result = value

        return JsonResponse(result,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def stateToCode(request):
    try:
        state = request.GET['state']
        f = open(BASE_DIR+'/json_reader/resources/states_titlecase.json')
        json_string = f.read()
        f.close()
        data = json.loads(json_string)

        result = 'No result'

        for i in range(len(data)):
            if(data[i]['name'] == state):
                result = data[i]['abbreviation']

        return JsonResponse(result,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)