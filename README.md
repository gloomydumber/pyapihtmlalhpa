# 화장실 API 활용

학과 | 학번 | 성명
---- | ---- | ---- 
정보컴퓨터공학전공 |201661701 |강동민


## 프로젝트 개요
공공데이터포털(data.go.kr)에서 OPEN API로 제공되고, 실생활에 활용가능성이 높은 공중 화장실 정보를 다루어 본다.
차후에 웹, ANDROID 및 iOS 어플리케이션, GUI 관련 툴 등을 학습하여 연계할 수 있을 것으로 생각하여 선택하였고,
실제로 공부해둔 간단한 html 및 css와 연계함.

처음에 부산광역시 공중화장실 정보를 이용하려고 하였으나, 다음과 같은 문제가 발생함.
![qna](./readmeimg/qna.PNG)
따라서 부산광역시 공중화장실 정보와 오퍼레이션이 매우 유사한 울산광역시 공중화장실 정보를 이용함.


## 사용한 공공데이터 
[데이터보기](http://data.ulsan.go.kr/rest/ulsantoilet/getUlsantoiletList?authApiKey=DEjz18TCYogpRgTo7XL5cAGOmLWhnd30DiWD%2BP2cqkUNMP%2F8%2FBNM4jxZ72gKpNNPG6XOAZzXcmg5kXATmq499g%3D%3D&numOfRows=9999)
(새창으로 열기 : Ctrl + Click)
## HTML 결과물
[웹사이트](https://gloomydumber.github.io/pyapihtmlalhpa/result.html)
(새창으로 열기 : Ctrl + Click)
## 소스
* [링크로 소스 내용 보기](https://github.com/gloomydumber/pyapihtmlalhpa/blob/master/toiletest.py) 
(새창으로 열기 : Ctrl + Click)
* 코드 삽입
~~~python
items = list(range(1,11))

for i in items:
    print(i)
~~~
