import os
from bs4 import BeautifulSoup
import requests
import urllib.request
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')] 
urllib.request.install_opener(opener)
path_name=""
def get_image_url(s):
    url='http://pokemon.wikia.com/wiki/'+s
    u=requests.get(url)
    soup=BeautifulSoup(u.content,"html5lib")
    x=soup.findAll('a',attrs={'class':'image image-thumbnail'});sp=0;
    for i in x:
        i=i.find('img')
        if int(str(i['height']))>=200 and int(str(i['width']))>=200:
            sp=i
            break
    return str(sp['data-src'])
def get_images(arr):
    global path_name
    ctr=1
    for i in arr:
        i=i[:-1]
        try: 
            if not os.path.exists(path_name+i+".png"):
                url=get_image_url(i) 
                name=path_name+i+".png"
                urllib.request.urlretrieve(url,name)
            print("({0}) {1} Downloaded".format(ctr,i));ctr+=1
        except Exception:
            print("Error in {0}".format(i));ctr==1

def read_from_file(p):
    global path_name
    path_name=p+'Images\\'
    f=open(path_name[:-7]+"names.txt","r",encoding='utf-8')
    arr=f.readlines()
    f.close()
    get_images(arr)

