import sys
import requests

url1="http://staff.elka.pw.edu.pl/~jwagner/tablica/new_message.php"
url2="http://staff.elka.pw.edu.pl/~jwagner/tablica/read_messages.php"

dict={}
dict["sender"]=sys.argv[2]
dict["message"]=sys.argv[3]
if sys.argv[1]=="post":
    p=requests.post(url1,json=dict)
    code=p.status_code
    if code==200:
        print("wiadomosc wyslana pomyslnie")
    else:
        print("kod: ",code)
        print(p.text)
elif sys.argv[1]=="get":
    g=requests.get(url2)
    print(g.text)
