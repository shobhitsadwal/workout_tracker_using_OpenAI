import requests
import datetime

now=datetime.datetime.now()

b=now.strftime("%x")

c=now.strftime('%X')

now.time()





app_id="93f36ecf"
app_key="638d21bc578c3a9b4f1ce21da2033ba9"


heads={
    "x-app-id":app_id,
    "x-app-key":app_key
}

#[ Base URL: trackapi.nutritioni x.com/ ]

#https://trackapi.nutritionix.com/v2/natural/exercise    #this is the excercise endpoints

base_url="https://trackapi.nutritionix.com/v2/natural/exercise"



imput=input("how much did you work out today ")
params={
    "query":imput,
    "gender":"male",
    "weight_kg":74,
    "height_cm":162.5,
    "age":25
}

request=requests.post(url=base_url,json=params,headers=heads)
a=request.json()
#
# print(a["exercises"][0]["nf_calories"])
# print(a["exercises"][0]["name"])

lister=[]
for i in range(len(a["exercises"])):
    p=a["exercises"][i]["nf_calories"]
    o=a["exercises"][i]["name"]
    d=a["exercises"][i]["duration_min"]
    aprams={
        "sheet1":{
            "date":b,
            "time":c,
            "excercise":o.title(),
            "duration":int(d),
            "calories":int(p)
        }
    }

    requests.post(url="https://api.sheety.co/0a32df7d8f89674c472b4c40993268e6/mySheets/sheet1",json=aprams)
    print(request.text)

