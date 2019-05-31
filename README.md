# 공중 화장실 API 활용

학과 | 학번 | 성명
---- | ---- | ---- 
정보컴퓨터공학전공 |201661701 |강동민


## 프로젝트 개요
<strong>프로젝트 계획</strong>

<strong>[공공데이터포털](https://data.go.kr)</strong>에서 OPEN API로 제공되고, 실생활에 활용가능성이 높은 공중 화장실 정보를 다루어 본다.

차후에 웹, ANDROID 및 iOS 어플리케이션, GUI 관련 툴 등을 학습하여 연계할 수 있을 것으로 생각하여 선택하였고,
실제로 공부해둔 간단한 html 및 css와 연계함.

<strong>프로젝트 최종 목표</strong>

<em>파이썬을 통해, OPEN API로 부터 몇 가지 유용한 항목을 전달받아 HTML 파일을 출력하는 코드 작성.</em>

<strong>프로젝트 진행 과정</strong>

처음에 부산광역시 공중화장실 정보를 이용하려고 하였으나, 다음과 같은 문제가 발생함.
![qna](./readmeimg/qna.PNG)
따라서 부산광역시 공중화장실 정보와 오퍼레이션이 매우 유사한 울산광역시 공중화장실 정보를 이용함.

파이썬으로 HTML을 출력하는 파일을 코딩할 시, 다음과 같은 비경제성 발생
  
    >>> f.write('<a href="http://pusan.ac.kr/">부산대</a>') # 라고 작성해야,
    <a href="http://pusan.ac.kr/">부산대</a> # html파일에서 html 문법에 맞게 출력


즉, 쉽게 작성 할 수 있는 마크업언어인 html을 파이썬의 file.write()로 한줄씩 입력해야함.
따라서 부분적으로 [htmltag](https://github.com/LiftoffSoftware/htmltag) 라는 파이썬 모듈을 도입하여 비경제성을 미약하게나마 해결 시도함.



<strong>프로젝트 한계</strong>

javascript를 통한 Open API 반응형 웹을 구축하면, API상의 정보가 변할 때마다 python을 통한 HTML 출력 후, 서버에 업로드 해야하는 비경제적이고 불합리한 문제 해결 가능.

프로젝트의 의의를 <strong><em>python</em></strong>으로 OPEN API를 활용한 것에 두기로 한다.

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
