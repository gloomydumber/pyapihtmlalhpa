from htmltag import h1
from htmltag import h2
from htmltag import a


b=(h2("testda zz"))
c=(a('awesome software', href='http://liftoffsoftware.com/'))

ft = open("htmljaksungtest.html","w")
ft.write(b)
ft.write(c)
ft.close()
