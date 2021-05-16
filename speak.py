import requests
import json


def speak(str):
     from win32com.client import Dispatch

     speak = Dispatch("SAPI.SpVoice")


     speak.Speak(str)
if __name__ == '__main__':


   speak("Live breaking news from Australia")

   url = "https://newsapi.org/v2/top-headlines?country=au&apiKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   news = requests.get(url).text

   news_parse = json.loads(news)

   print(news_parse)
   arts=news_parse['articles']

   for articles in arts:
       speak(articles['title'])
       speak("Today's Next Headline")
