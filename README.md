# workout_tracker_using_OpenAI
tracking workouts by sending the text over information in the GPT-3 Deep Learning model

![open_ai](https://openai.com/content/images/2021/08/openai-cover.png)
![gpt-3](https://crowdbotics.ghost.io/content/images/2020/07/GPT-3-2.jpg)

# Aim and objective of this project 
the primary aim of this project is to track down the calories burned and the food intake required when we input the information and to recieve the exact information from a deep-learning model which is 
also called as **GPT-3**.

# files and important refrences -
- ```main.py``` for the base applicaiton and the working code of the project 
- ```openAI.text``` for information about the working principals
- ```GPT-3.txt``` for information about the the working algorithm and deeplearning model 
- ```summary_Deep_Learning.txt``` for more information about deep-learning and neural networks 

## note: This project is heavily built on API  methods which include all **POST,GET,DELETE,PUT & UPDATE**. If you are not aware with the working of APIS AND Restful functons , please refer to the following 
- https://www.dataquest.io/blog/python-api-tutorial/
- https://realpython.com/python-api/
- https://docs.python.org/3/c-api/index.html
- https://www.redhat.com/en/topics/api/what-is-a-rest-api
- https://www.baeldung.com/rest-http-put-vs-post#:~:text=Another%20important%20difference%20between%20the,the%20same%20resource%20multiple%20times.
- https://stackoverflow.com/questions/630453/what-is-the-difference-between-post-and-put-in-http

## API ethics references
- https://blogs.mulesoft.com/api-integration/strategy/ethics-of-apis/
- https://www.plektonlabs.com/api-and-ethics-what-are-the-ambiguities/
- https://apievangelist.com/2017/05/31/an-example-of-api-ethics-out-of-cambridge-university/

# code-flow 
The initial concept of making a workout tracaker was to record the workout and add the entry to the database . For obvious reasons many people do not know how to enter the values in the database and make the correct
prediction of the calories burnt during the workout . 

This project is solely based on the concept of running the application and just entering the details like the duration and the type of the workout the user has done , it automatically detects the calories burnt and the food options
to eat depending on the wokout and the best part is to simply write the input in **Plain Human Manner**
```python
your_workout=input("today i worked out and that included umm, cycling ,some running , i dont know the time but it was like something for 60 to 70 minutes.")
```
you can see how we have managed to write a simple statement  in human langauage without emphasizing on the workouts we did, the surprising part is that, the Open-Ai's GPT-3 converts this langauage and forms a table that contains the number of the workouts, the exact timing that the workout should be accomplished by taking the users mean time and the universal mean time .

here is an example 

<a href="https://ibb.co/JndHf6G"><img src="https://i.ibb.co/0qXrg46/Screenshot-27.png" alt="Screenshot-27" border="0"></a>

this is the power of Deep-learning models which here is the Gpt-3 from OpenAI which has been slightly modified by the nutritionix.com for using this technology in the field of health and services .

here is the main.py file and let us follow the code along with some important concepts- 
```python
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
```

we have imported necessary libraries to perform this program , datetime has been imported because the date and time will be used when making the tables for keeping track of the workout . AN encryption key with the app Id key has been set to perform the post operation when the user inputs the workout ,
the base url for track.api and nutritionix is https://www.nutritionix.com/business/api. Also we have kept the important credentials inside teh dictioinary object because nutritioninx requires the header files in the post for Authentication. 


### creation of sheety to work with the google sheets
we are storing the information in the google sheets because the information is directly reached to the google sheets and also there are many API's to directly communicate with google sheets online. One such api poster and getter to googgle sheets is sheety . Sheety provides continious integration with our google sheets for storing the information , to read more about sheety refer to 
- https://sheety.co/
- https://sheety.co/docs


we have already made a google sheet and linked it to sheety , the columns that are inside our google sheets are *date,time,duration and calories * . When the input is given the request get posted in the sheety application and in turns 
it modifies the table . Thus whenver we input the information we can say that there is an automatic process of updation of the table and we dont have to have to manually update the sheets . 


# excerpts from ```summary_Deep_Learning.txt```
Deep Learning uses a Neural Network to imitate animal intelligence.
There are three types of layers of neurons in a neural network: the Input Layer, the Hidden Layer(s), and the Output Layer.
Connections between neurons are associated with a weight, dictating the importance of the input value.
Neurons apply an Activation Function on the data to “standardize” the output coming out of the neuron.
To train a Neural Network, you need a large data set.
Iterating through the data set and comparing the outputs will produce a Cost Function, indicating how much the AI is off from the real outputs.
After every iteration through the data set, the weights between neurons are adjusted using Gradient Descent to reduce the cost function.

# openAI api ethics 


OpenAI API
We’re releasing an API for accessing new AI models developed by OpenAI. Unlike most AI systems which are designed for one use-case, the API today provides a general-purpose “text in, text out” interface, allowing users to try it on virtually any English language task. You can now request access in order to integrate the API into your product, develop an entirely new application, or help us explore the strengths and limits of this technology.

Given any text prompt, the API will return a text completion, attempting to match the pattern you gave it. You can “program” it by showing it just a few examples of what you’d like it to do; its success generally varies depending on how complex the task is. The API also allows you to hone performance on specific tasks by training on a dataset (small or large) of examples you provide, or by learning from human feedback provided by users or labelers.

We’ve designed the API to be both simple for anyone to use but also flexible enough to make machine learning teams more productive. In fact, many of our teams are now using the API so that they can focus on machine learning research rather than distributed systems problems. Today the API runs models with weights from the GPT-3 family with many speed and throughput improvements. Machine learning is moving very fast, and we’re constantly upgrading our technology so that our users stay up to date.

The field’s pace of progress means that there are frequently surprising new applications of AI, both positive and negative. We will terminate API access for obviously harmful use-cases, such as harassment, spam, radicalization, or astroturfing. But we also know we can’t anticipate all of the possible consequences of this technology, so we are launching today in a private beta rather than general availability, building tools to help users better control the content our API returns, and researching safety-relevant aspects of language technology (such as analyzing, mitigating, and intervening on harmful bias). We’ll share what we learn so that our users and the broader community can build more human-positive AI systems.
In addition to being a revenue source to help us cover costs in pursuit of our mission, the API has pushed us to sharpen our focus on general-purpose AI technology—advancing the technology, making it usable, and considering its impacts in the real world. We hope that the API will greatly lower the barrier to producing beneficial AI-powered products, resulting in tools and services that are hard to imagine today.













