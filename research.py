
import urllib.request
import math

def gettext(url:str):
    response=urllib.request.urlopen(url)
    text=response.read().decode(encoding = 'utf-8')

    return text

def getlist(s:str):
    l=s.split("\n")
    

    return list(i.rstrip() for i in l)[:-1]

def printTable(url:str):

    l=getlist(gettext(url))
    column_headers = [i for i in l[0].split(',')]+['cosine value']
    print("{:^15} {:^15} {:^15}".format(*column_headers))
    for i in l[1:]:
        n1,n2=i.split(',')
        row="{:^15} {:^15} {:^15.2f}".format(*[int(n1), int(n2), math.cos(int(n2)*math.pi/180)])
        print(row)
     

printTable("http://rapid-hub.org/data/angles_UCI_CS.csv")


    
