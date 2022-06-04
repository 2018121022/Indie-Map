from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .keys import (
                            serviceId,
                            AUTH_SECRET_KEY,
                            AUTH_ACCESS_KEY,
                            SMS_SEND_PHONE_NUMBER,
)
import sys
import os
import hashlib
import hmac
import base64
import requests
import time
import json

def send_notification(concert_name, concert_date, concert_time, concert_address, concert_receiver):
        SMS_URL = 'https://sens.apigw.ntruss.com/sms/v2/services/' + f'{serviceId}' + '/messages'
        timestamp = str(int(time.time() * 1000))
        secret_key = bytes(AUTH_SECRET_KEY, 'utf-8')

        method = 'POST'
        uri = '/sms/v2/services/' + f'{serviceId}' + '/messages'
        message = method + ' ' + uri + '\n' + timestamp + '\n' + AUTH_ACCESS_KEY
        message = bytes(message, 'utf-8')
				
        # 알고리즘으로 암호화 후, base64로 인코딩
        signingKey = base64.b64encode(
            hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'x-ncp-apigw-timestamp': timestamp,
            'x-ncp-iam-access-key': AUTH_ACCESS_KEY,
            'x-ncp-apigw-signature-v2': signingKey,
        }

        #수신인 전화번호
        receiver = ''.join(concert_receiver.split('-'))
        # 공연 당일 날 오전 9시 문자 알린 전송
        notification_time = str(concert_date) + " " + "09:00" 
        #메세지 내용
        message = str(concert_name) + "님 오늘 " + str(concert_date) + " " + str(concert_time) + " " + str(concert_address) + "에서 라이브 공연할 예정입니다!"

        body = {
                "type": "SMS",
                "contentType": "COMM",
                "from": "01084366647",
                "subject": "공연 알림",
                "content": message,
                "messages": [{"to": receiver}],
                "reserveTime": notification_time,
                "reserveTimeZone": "Asia/Seoul"
        }

        # body를 json으로 변환
        encoded_data = json.dumps(body)
		
        # post 메서드로 데이터를 보냄
        res = requests.post(SMS_URL, headers=headers, data=encoded_data)
        return HttpResponse(res.status_code)
