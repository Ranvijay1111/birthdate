from ast import arg
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import  JsonResponse
from django.core import serializers
from django.conf import settings
import json
from datetime import date

@api_view(['POST'])
def calculateAge(birthDate):
    try:
        days_in_year = 365.2425   
        age = int((date.today() - birthDate).days / days_in_year)
        return JsonResponse(calculateAge(date(1993,2,3),"years")
    except: ValueError as e:
        return Response(e.arg[0],status.HTTP_400_BAD_REQUEST)

