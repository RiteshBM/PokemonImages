
from bs4 import BeautifulSoup
import requests
import get_images
import urllib.request
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')] 
urllib.request.install_opener(opener)
path_name="E:\\PythonProjects\\Pokemon Stuff\\"
poke_names=[]
def get_names():
    global poke_names
    url='https://pokemondb.net/pokedex/national'
    u=requests.get(url)
    soup=BeautifulSoup(u.content,"html5lib")
    poke=soup.findAll('span',attrs={'class':'infocard-lg-data text-muted'})
    for i in poke:
        x=i.find('a',attrs={'class':'ent-name'})
        poke_names.append(str(x.text))
def writetofile(x):
    global poke_names
    global path_name
    f=open(path_name+"names.txt","w+",encoding='utf-8')
    if x==-1:
        t=len(poke_names)
    else:
        t=x
    for i in range(t):
        f.write(poke_names[i]+'\n')
    f.close()


def main(p,x):
    global path_name
    path_name=p
    get_names()
    writetofile(x)
    get_images.read_from_file(path_name)