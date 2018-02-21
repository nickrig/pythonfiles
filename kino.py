import urllib2
import json
import datetime

cur_date=datetime.datetime.now()

def compare_lists(l1,l2):
    s=0
    for i in l1:
        if i in l2:
            s+=1
    return s
memo=[] 
for i in range (10):
    x=int(input("enter number: \n")) 
    memo.insert(i,x)
    i+=1
print(memo)
MegHmeras=[] #pinakas pou perilamvanei gia kathe imera ton arithmo twn epituxiwn
Hmer=[] #pinakas pou krataei kathe hmerominia
for i in range(31):
    cur_date= cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    Hmer.insert(i,date_str)
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']
    r=[]
    for k in klhrwseis:
        tmp=k["results"]
        r.append(compare_lists(memo,tmp))
    MegHmeras.insert(i,0)
    for j in range(180): #180 einai oi klirwseis pou ginontai kathimerina
        if r[j] > 4: #elegxw an uparxei epituxia
            MegHmeras[i] = MegHmeras[i] + 1
megisto = 0
for i in range(30):
    if MegHmeras[i] > MegHmeras[i+1]:
        megisto = MegHmeras[i]
        thesimegistou = i
print 10*"-"
print("Oi perissoteres epituxies pou simeiwthikan me authn thn epilogi arithmwn einai: "),megisto
print("kai simeiwthikan stis: "),Hmer[thesimegistou]
    
   
        
    
