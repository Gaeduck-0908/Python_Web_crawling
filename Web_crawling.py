import requests #HTTP요청 라이브러리
from bs4 import BeautifulSoup #데이터 받을때 사용하는 라이브러리
import datetime #날짜 라이브러리

#학교 입력
while True:
    print("학교 검색기록 넣어주십쇼")
    Urlinput = input()

#기본설정
    food = []
    Url = requests.get(Urlinput)
    Bsoup = BeautifulSoup(Url.content, "html.parser")
    menu = Bsoup.select(".menu_info")
    to = datetime.datetime.now()

#타이틀제거
    setup = Bsoup.find('title').getText().rstrip(": 네이버 통합검색")
    print(setup +"의 급식정보")

#급식표시 설정
    print("1.전체급식 2.오늘급식")
    a = int(input())

#실행

    if(a == 1): #전체급식
        for food in menu:
            print(food.text)

    elif(a == 2): #오늘급식
        today = " " +str(to.month)+"월 "+str(to.day)+"일 "
        print(today+"급식")
        for food in menu:
            foodTo = food.text[:food.text.find('[')]
            if foodTo == today :
                print(food.text)
    
    #재실행 여부
    print("\n 다시 검색하시겠습니까? \n Y를 입력시 재실행 됩니다.")
    check = input()
    if(check == "Y" or check == "y"):
        continue
    else:
        break
        