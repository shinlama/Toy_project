from django.shortcuts import render
import requests
import random

# Create your views here.
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

