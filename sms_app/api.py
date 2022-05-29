from django.http import HttpResponse
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

def send_notification():
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

        name = "이무진"
        place = "신촌역 2번 출구"
        showtime = "25/05/2022 22:30"
        receiver = "01084366647"
        alert_timing = '30분 전'
        send_date = (showtime.split()[0]).split('/')
        year = send_date[2]
        month = send_date[1]
        day = send_date[0]
        send_time = showtime.split()[1]

        if alert_timing == '1일 전':
            day = int(day) - 1
            notification_time = year + "-" + month + "-" + str(day) + " " + send_time
            message = name + "님 내일 " + showtime + place + "에서 라이브 공연할 예정입니다!"

        elif alert_timing == '30분 전':
            send_time = send_time.split(':')
            hour = send_time[0]
            minute = send_time[1]
            minute = int(minute) - 30
            if minute < 0:
                minute = 60 + minute
                hour = int(hour) - 1
                if hour < 0:
                    hour = 24 + hour
                    day = int(day) - 1
            hour = str(hour)
            minute = str(minute)
            if minute == '0':
                minute = "00"
            if hour == '0':
                hour = "00"
            send_time = hour + ":" + minute
            notification_time = year + "-" + month + "-" + str(day) + " " + send_time
            message = name + "님 30분 후 " + showtime + " " + place + "에서 라이브 공연할 예정입니다!"
        
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