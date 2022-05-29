from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .api import send_notification
from .keys import (
                            serviceId,
                            AUTH_SECRET_KEY,
                            AUTH_ACCESS_KEY,
                            SMS_SEND_PHONE_NUMBER,
)
import json

def sms(request):
    return render(request, 'sms.html')
    
def alarm_sms(request):
        try:
            #data = json.loads(request.body)
            send_notification()
            return JsonResponse({'message': 'SUCCESS'}, status=201)

        except KeyError as e:
            return JsonResponse({'message': f'KEY_ERROR: =>  {e}'}, status=400) 
