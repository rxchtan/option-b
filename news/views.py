import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline, History

def scrape(request):
  if request.method == "POST":
      topic = request.POST['topics']
  else:
      topic = ""

  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.straitstimes.com/singapore/" + topic

  content = session.get(url, verify=False).content
  soup = BSoup(content, "html.parser")
  article = soup.find('div', {"class":"view-content"})
  
  main = article.find('a')
  link = main['href']
  title = main.string
  if link: 
      article_link = "https://www.straitstimes.com" + link
      page = session.get(article_link, verify=False).content
      soup_article = BSoup(page, "html.parser")
      body = soup_article.find_all('div', {"class":"odd field-item"})
      if body:
          x = body[0].find_all('p')
          list_paragraphs = ""
          for p in x:
              paragraph = p.get_text()
              list_paragraphs = list_paragraphs + "\n" + paragraph
          headlines = Headline.objects.all()[::-1]
          if headlines:
              headlines[0].title = title
              headlines[0].url = link
              headlines[0].text = list_paragraphs
              headlines[0].save()
          else:
              new_headline = Headline()
              new_headline.title = title
              new_headline.url = link
              new_headline.text = list_paragraphs
              new_headline.save()
          history = History()
          history.title = title
          history.url = link
          history.text = list_paragraphs
          history.save()
  return redirect("../")

def news_list(request):
    history = History.objects.all()[::-1]
    context = {
        'object_list': history,
    }
    return render(request, "news/home.html", context)

def news(request):
    headline = Headline.objects.all()[::-1]
    context = {
        'news_article': headline,
    }
    return render(request, "news/home.html", context)