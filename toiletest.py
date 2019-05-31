import urllib.request
import xml.etree.cElementTree as et
import pandas as pd
from htmltag import title
from htmltag import a
from htmltag import span

class GetData: # API에서 자료 불러오기
    url = "http://data.ulsan.go.kr/rest/ulsantoilet/getUlsantoiletList?authApiKey=" \
          "DEjz18TCYogpRgTo7XL5cAGOmLWhnd30DiWD%2BP2cqkUNMP%2F8%2FBNM4jxZ72gKpNNPG6XOA" \
          "ZzXcmg5kXATmq499g%3D%3D&numOfRows=9999"
    def main(self):
        data = urllib.request.urlopen(self.url).read()
        f = open("testoftoiletz.xml","wb")
        f.write(data)
        f.close()

getData = GetData()
getData.main()

def getvalueofnode(node):
    return node.text if node is not None else None

parsed_xml = et.parse("testoftoiletz.xml")
root=parsed_xml.getroot()
dfcols = ['화장실명', '화장실주소', '경도', '위도'] #pandas 작성부분
df_xml = pd.DataFrame(columns=dfcols)

fh = open("result.html", "w") #html 작성부분

def htmlwrite1():
    fh.write("<html>")
    #fh.write('<meta charset="utf-8">') # LOCAL과 SERVER에 올렸을때 글자 깨짐 차이
    fh.write('<meta name="viewport" content="width=device-width">')
    fh.write('<meta name="viewport" content="width=device-width, initial-scale=1">')
    tit = title("울산광역시 공중화장실 정보")
    fh.write(tit)
    fh.write(str('<link rel="stylesheet" href="styletoilet.css">'))  # css 도입
    fh.write(str('<script async src="https://www.googletagmanager.com/gtag/js?id=UA-118438750-1"></script>'))
    fh.write(str('<script>'))
    fh.write(str('window.dataLayer = window.dataLayer || [];'))
    fh.write(str('function gtag(){dataLayer.push(arguments);}'))
    fh.write(str("gtag('js', new Date());"))
    fh.write(str("gtag('config', 'UA-118438750-1');"))
    fh.write(str('</script>'))
    fh.write(str('<h1><a href="index.html"><font color="yellow">GLOOMYDUMBER</font></a></h1>'))
    fh.write(str('<div id="grid">'))
    fh.write(str('<ul>'))
    fh.write(str('<li><a href="1.html">memes</a></li>'))
    fh.write(str('<li><a href="2.html">CB</a></ll>'))
    fh.write(str('<li><a href="3.html">hguitar</a></li>'))
    fh.write(str('<li><a href="result.html"><font size="2px">울산화장실정보</font></a></li>'))
    fh.write(str('</ul>'))
    fh.write(str('<div id="article">'))
    fh.write(str('<br>'))
    fh.write(span(str('화장실이름'),id="ix"))
    fh.write('\n')
    fh.write(span(str('도로명주소'),id="ix"))
    fh.write('\n')
    fh.write(span(str('개방시간'),id="ix"))
    fh.write('\n')
    fh.write(span(str(''), id="ix2")) # 해상도 반응형 그리드
    fh.write(span(str(''), id="ix2"))
    fh.write(span(str(''), id="ix2"))

def htmlwrite2():
    fh.write(str('<div id="disqus_thread"></div>'))
    fh.write(str('<script>'))
    fh.write(str('var disqus_config = function () {'))
    fh.write(str('this.page.url = PAGE_URL;'))
    fh.write(str('this.page.identifier = PAGE_IDENTIFIER;'))
    fh.write(str('(function()'))
    fh.write(str("var d = document, s = d.createElement('script');"))
    fh.write(str("s.src = 'https://rypl.disqus.com/embed.js';"))
    fh.write(str("s.setAttribute('data-timestamp', +new Date());"))
    fh.write(str('(d.head || d.body).appendChild(s);'))
    fh.write(str('})();'))
    fh.write(str('</script>'))
    fh.write(str('<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>'))
    fh.write(str('<script type="text/javascript">'))
    fh.write(str('var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();'))
    fh.write(str('(function(){'))
    fh.write(str('var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];'))
    fh.write(str('s1.async=true;'))
    fh.write(str("s1.src='https://embed.tawk.to/5ae78c61227d3d7edc24d9f3/default';"))
    fh.write(str("s1.charset='UTF-8';"))
    fh.write(str("s1.setAttribute('crossorigin','*');"))
    fh.write(str('s0.parentNode.insertBefore(s1,s0);'))
    fh.write(str('})();'))
    fh.write(str('</script>'))
    fh.write("</html>")

htmlwrite1()

for node in root.iter(): #API에서 받은자료를 pandas작성과 동시에 html에 작성
    toiletName = node.find('toiletName')
    if toiletName != None:
        n=(span(str(getvalueofnode(toiletName))))
        fh.write(n)
        fh.write("\n")
    toiletNewAddr = node.find('toiletNewAddr')
    if toiletNewAddr != None:
        na = (span(str(getvalueofnode(toiletNewAddr))))
    toiletXpos = node.find('toiletXpos')
    if toiletXpos != None:
        x = ((str(getvalueofnode(toiletXpos))))
    toiletYpos = node.find('toiletYpos')
    if toiletYpos != None:
        y = ((str(getvalueofnode(toiletYpos))))
        lk = str("https://www.google.co.kr/maps/place/"+y+" "+x)
        c = (span(a(na, href=lk, target="_blank")))
        fh.write(c)
        fh.write("\n")
    toiletUnisexCheck = node.find('toiletUnisexCheck')
    ''' # 전부 남녀개별 화장실이므로 생략
    if toiletUnisexCheck != None:
        tus = (span(str(getvalueofnode(toiletUnisexCheck))))
        if tus=="Y":
            fh.write(span(str("남녀공용")))
            fh.write("<br>")
        else:
                fh.write(span(str("남녀개별")))
                fh.write("<br>")
    '''
    toiletOpenTime = node.find('toiletOpenTime')
    if toiletOpenTime != None:
        tot = (span(str(getvalueofnode(toiletOpenTime))))
        fh.write(tot)
        fh.write("<br>")
    if toiletName != None :
        df_xml = df_xml.append(pd.Series([getvalueofnode(toiletName), getvalueofnode(toiletNewAddr), getvalueofnode(toiletXpos),getvalueofnode(toiletYpos)],index=dfcols),ignore_index=True)

htmlwrite2()

print(df_xml) # pandas python ide console에 출력

fh.close()


