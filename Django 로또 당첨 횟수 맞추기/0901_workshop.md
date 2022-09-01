## Django Projext - lotto

### 1. views.py

"""
from django.shortcuts import render
import requests
import random

def lotto(request):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1'
    req_result = requests.get(url)
    json_result = req_result.json()

    val_1 = json_result.get('drwtNo1')
    val_2 = json_result.get('drwtNo2')
    val_3 = json_result.get('drwtNo3')
    val_4 = json_result.get('drwtNo4')
    val_5 = json_result.get('drwtNo5')
    val_6 = json_result.get('drwtNo6')
    bnus = json_result.get('bnusNo')
    lotto_list = [val_1, val_2, val_3, val_4, val_5, val_6]

    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    ng = 0
    for n in range(1,1001):
        rdm = random.sample(range(1,46),6)
        cnt = 0
        for i in rdm:
            if i in lotto_list:
                cnt += 1
        if cnt == 6:
            n1 += 1
        if (cnt == 5) and (bnus in rdm):
            n2 += 1
        elif cnt == 5:
            n3 += 1
        elif cnt == 4:
            n4 += 1
        elif cnt == 3:
            n5 += 1
        else:
            ng += 1
    
    context = {
        'val_1':val_1,
        'val_2':val_2,
        'val_3':val_3,
        'val_4':val_4,
        'val_5':val_5,
        'val_6':val_6,
        'bnus':bnus,
        'n1':n1,
        'n2':n2,
        'n3':n3,
        'n4':n4,
        'n5':n5,
        'ng':ng,
    }


    return render(request, 'lotto.html', context)
"""

### 2. urls.py
"""
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', views.lotto),
]
"""

### 3. lotto.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>로또 당첨 횟수를 알아보자. </h1>
    <hr>
    <h3>이번 회차 당첨 번호: [{{ val_1 }}, {{ val_2 }}, {{ val_3 }}, {{ val_4 }}, {{ val_5 }}, {{ val_6 }}] + {{ bnus }}</h3>
    <ul>
        <p>1등: {{ n1 }}</p> 
        <p>2등: {{ n2 }}</p>
        <p>3등: {{ n3 }}</p>
        <p>4등: {{ n4 }}</p>
        <p>5등: {{ n5 }}</p>
        <p>꽝: {{ ng }}</p>
    </ul>
</body>
</html>
"""