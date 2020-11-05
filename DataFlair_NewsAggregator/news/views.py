import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

requests.packages.urllib3.disable_warnings()

def scrape(request): # scrape news articles from theonion.com
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.theonion.com/"
  content = session.get(url, verify=False).content
  soup = BSoup(content, "html.parser") # create a soup object
  News = soup.find_all('div', {"class":"curation-module__item"})
  for artcile in News: # to iterate over soup objects
    main = artcile.find_all('a')[0]
    link = main['href']
    image_src = str(main.find('img')['srcset']).split(" ")[-4]
    title = main['title']
    new_headline = Headline()
    new_headline.title = title
    new_headline.url = link
    new_headline.image = image_src
    new_headline.save()
  return redirect("../")


def news_list(request):
    headlines = Headline.objects.all()[::-1] # reverse the list to have latest info on top
    context = {
        'object_list': headlines,
    }
    return render(request, "news/home.html", context) # give our context to our html page