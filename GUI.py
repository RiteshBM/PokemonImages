
import os
import getnames
import PIL.Image
import shutil
from tkinter import *
import PIL
from PIL import ImageTk
class node:
    def __init__(self,val):
        self.val=val
        self.child={}
        self.wordend="-"
        
def addword(s,head):
    for i in s:
        if i in head.child:
            head=head.child[i]
        else:
            temp=node(i)
            head.child[i]=temp
            head=head.child[i]
    head.wordend=s
        
def ctrie(arr):
    head=node('-')
    for i in arr:
        addword(i,head)
    return head

def get_all(head):
    arr=[head]
    rar=[]
    while len(arr)!=0:
        t=arr.pop(0)
        if t.wordend!='-':
            rar.append(t.wordend)
        for i in t.child:
            arr.append(t.child[i])
    return rar
def grw(s,head):
    for i in s:
        if i in head.child:
            head=head.child[i]
        else:
            break
    if head.wordend!=s:
        t=get_all(head);t.sort()
        return 1,t
    else:
        return -1,head.wordend
    
    

path_name=str(os.getcwd())+"\\"
while True:
    x=int(input('''Number of Pokemon Entries To Be Created
                (-1)All(807)
                (-2)Clear All Previous
                (-3)Search With what is stored
                (X) X Entries
                '''))
    if x==-2:
        if os.path.exists(path_name+"Images"):
            shutil.rmtree(path_name+"Images")
        if os.path.exists(path_name+"names.txt"):
            os.remove(path_name+"names.txt")
        print("Cleared")
    elif x>=-1:
        if not os.path.exists(path_name+"Images"):
            os.makedirs(path_name+"Images")
        getnames.main(path_name,x)
    elif x==-3:
        if not os.path.exists(path_name+"Images"):
             os.makedirs(path_name+"Images")
        if not os.path.exists(path_name+"names.txt"):
            f=open(path_name+"names.txt","w+",encoding='utf-8')
            f.close()
        break
print("Catch 'em all!!!")
f=open(path_name+"names.txt","r",encoding='utf-8')
arr=f.readlines();
f.close()
for i in range(len(arr)):
    arr[i]=arr[i][:-1]
search_index=ctrie(arr)


def ent(x):
    global sva;global search_index
    s=sva[5].get();term=""
    if x.keycode==8:
        term=s[:-1]    
    else:
        term=s+x.char
    a,b=grw(term,search_index)
    #print(term,x)
    if a==-1:
        sva[0].set(b);sva[1].set('Match');sva[2].set('Match');sva[3].set('Match');sva[4].set('Match');
    elif a==1:
        for i in range(min(5,len(b))):
            sva[i].set(b[i])
        if len(b)<5:
            for i in range(len(b),5):
                sva[i].set('No More Matches')
def btn_pre(x):
    global sva
    #print("option {0} selected".format(x))
    t=sva[x].get()
    if t!="No More Matches":
        loc=path_name+"Images\\"+t+'.png'
        img = PIL.Image.open(loc)
        img.show()
        
       
        
root=Tk()
root.title("Pokemon")
sva=[]
for i in range(10):
    t1=StringVar();t1.set("Pokemon")
    sva.append(t1)
e=Entry(root,textvariable=sva[5]);e.pack(side='top');e.bind("<Key>",ent)
l4=Button(root,textvariable=sva[4],command=lambda:btn_pre(4));l4.pack(side='bottom')
l3=Button(root,textvariable=sva[3],command=lambda:btn_pre(3));l3.pack(side='bottom')
l2=Button(root,textvariable=sva[2],command=lambda:btn_pre(2));l2.pack(side='bottom')
l1=Button(root,textvariable=sva[1],command=lambda:btn_pre(1));l1.pack(side='bottom')
l0=Button(root,textvariable=sva[0],command=lambda:btn_pre(0));l0.pack(side='bottom')

root.mainloop()
