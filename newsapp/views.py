from django.shortcuts import render, HttpResponse, redirect
from newsapi import NewsApiClient
from .models import Contact
from django.contrib import messages
from .models import *
import requests
from bs4 import BeautifulSoup
from .models import newslist
from .models import Contact
from .models import Newscatwise
from .models import Newscountrywise
import datetime


def index(request):
    newsapi = NewsApiClient(api_key='f2d21efaf1e4456db37ccaefbb14a4c2')
    top = newsapi.get_top_headlines(sources='the-times-of-india')

    l = top['articles']

    for i in range(len(l)):
        f = l[i]
        f['publishedAt'] = f['publishedAt'][0:10]
        if not newslist.objects.filter(title=f['title']).exists():
            newslist(title=f['title'], description=f['description'], image=f['urlToImage'],
                     author=f['author'], url=f['url'],
                     publishedAt=f['publishedAt'], content=f['content']).save()

    # mylist = zip(title, description, image, author, publishedAt, content)
    mylist = newslist.objects.all().order_by('-post_id')
    # mylist = newslist.objects.latest("date")

    extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
    URL = 'https://www.mohfw.gov.in/'

    SHORT_HEADERS = ['SNo', 'State', 'Indian_Confirmed',
                     'Foreign_Confirmed', 'Cured', 'Death']

    response = requests.get(URL).content
    soup = BeautifulSoup(response, 'html.parser')
    header = extract_contents(soup.tr.find_all('th'))

    stats = []
    all_rows = soup.find_all('tr')

    for row in all_rows:
        stat = extract_contents(row.find_all('td'))
        c = 0
        tc = 0
        d = 0
        if stat:
            if len(stat) == 5:
                # last row
                stat = ['', *stat]
                stats.append(stat)
            elif len(stat) == 6:
                stats.append(stat)
    return render(request, 'newsapp/index.html', {"mylist": mylist, "stats": stats})


def about(request):
    return render(request, 'newsapp/about.html')


def contact(request):
    messages.success(request, 'Welcome to contact')
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(desc) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            messages.success(request, "Your message has been delivered")
    return render(request, 'newsapp/contact.html')


def blogpost(request, title):
    post = (newslist.objects.filter(title=title).first() or Newscatwise.objects.filter(title=title).first() or Newscountrywise.objects.filter(title=title).first())
    context = {'post': post}
    return render(request, 'newsapp/blogpost.html', context)


def india(request):
    newsapi = NewsApiClient(api_key='f2d21efaf1e4456db37ccaefbb14a4c2')
    top = newsapi.get_top_headlines(country='in', language='en')

    l = top['articles']

    for i in range(len(l)):
        f = l[i]
        f['publishedAt'] = f['publishedAt'][0:10]
        if not Newscountrywise.objects.filter(title=f['title']).exists():
            Newscountrywise(title=f['title'], description=f['description'], image=f['urlToImage'],
                            author=f['author'], url=f['url'], country='india',
                            publishedAt=f['publishedAt'], content=f['content']).save()
    countrydata = Newscountrywise.objects.filter(country='india').order_by('-post_id')
    contextcountry = {'countrydata': countrydata}
    return render(request, 'newsapp/india.html', contextcountry)


def usa(request):
    newsapi = NewsApiClient(api_key='f2d21efaf1e4456db37ccaefbb14a4c2')
    top = newsapi.get_top_headlines(country='us',language='en')

    l = top['articles']

    for i in range(len(l)):
        f = l[i]
        f['publishedAt'] = f['publishedAt'][0:10]
        if not Newscountrywise.objects.filter(title=f['title']).exists():
            Newscountrywise(title=f['title'], description=f['description'], image=f['urlToImage'],
                            author=f['author'], url=f['url'], country='usa',
                            publishedAt=f['publishedAt'], content=f['content']).save()
    countrydata = Newscountrywise.objects.filter(country='usa').order_by('-post_id')
    contextcountry = {'countrydata': countrydata}
    return render(request, 'newsapp/usa.html', contextcountry)


def health(request):
    newsapi = NewsApiClient(api_key='f2d21efaf1e4456db37ccaefbb14a4c2')
    top = newsapi.get_top_headlines(category='health', language='en')

    l = top['articles']

    for i in range(len(l)):
        f = l[i]
        f['publishedAt'] = f['publishedAt'][0:10]
        if not Newscatwise.objects.filter(title=f['title']).exists():
            Newscatwise(title=f['title'], description=f['description'], image=f['urlToImage'],
                        author=f['author'], url=f['url'], category='health',
                        publishedAt=f['publishedAt'], content=f['content']).save()
    catdata = Newscatwise.objects.filter(category='health').order_by('-post_id')
    context = {'catdata': catdata}
    return render(request, 'newsapp/health.html', context)


def business(request):
    newsapi = NewsApiClient(api_key='f2d21efaf1e4456db37ccaefbb14a4c2')
    top = newsapi.get_top_headlines(category='business', language='en')

    l = top['articles']
    for i in range(len(l)):
        f = l[i]
        f['publishedAt'] = f['publishedAt'][0:10]
        if not Newscatwise.objects.filter(title=f['title']).exists():
            Newscatwise(title=f['title'], description=f['description'], image=f['urlToImage'],
                        author=f['author'], url=f['url'], category='business',
                        publishedAt=f['publishedAt'], content=f['content']).save()
    catdata = Newscatwise.objects.filter(category='business').order_by('-post_id')
    context = {'catdata': catdata}
    return render(request, 'newsapp/business.html', context)


def entertainment(request):
    newsapi = NewsApiClient(api_key='f2d21efaf1e4456db37ccaefbb14a4c2')
    top = newsapi.get_top_headlines(category='entertainment', language='en')

    l = top['articles']

    for i in range(len(l)):
        f = l[i]
        f['publishedAt'] = f['publishedAt'][0:10]
        if not Newscatwise.objects.filter(title=f['title']).exists():
            Newscatwise(title=f['title'], description=f['description'], image=f['urlToImage'],
                        author=f['author'], url=f['url'], category='entertainment',
                        publishedAt=f['publishedAt'], content=f['content']).save()
    catdata = Newscatwise.objects.filter(category='entertainment').order_by('-post_id')
    context = {'catdata': catdata}
    return render(request, 'newsapp/entertainment.html', context)


def general(request):
    newsapi = NewsApiClient(api_key='f2d21efaf1e4456db37ccaefbb14a4c2')
    top = newsapi.get_top_headlines(category='general', language='en')

    l = top['articles']

    for i in range(len(l)):
        f = l[i]
        f['publishedAt'] = f['publishedAt'][0:10]
        if not Newscatwise.objects.filter(title=f['title']).exists():
            Newscatwise(title=f['title'], description=f['description'], image=f['urlToImage'],
                        author=f['author'], url=f['url'], category='general',
                        publishedAt=f['publishedAt'], content=f['content']).save()
    catdata = Newscatwise.objects.filter(category='general').order_by('-post_id')
    context = {'catdata': catdata}
    return render(request, 'newsapp/general.html', context)


def science(request):
    newsapi = NewsApiClient(api_key='f2d21efaf1e4456db37ccaefbb14a4c2')
    top = newsapi.get_top_headlines(category='science', language='en')

    l = top['articles']

    for i in range(len(l)):
        f = l[i]
        f['publishedAt'] = f['publishedAt'][0:10]
        if not Newscatwise.objects.filter(title=f['title']).exists():
            Newscatwise(title=f['title'], description=f['description'], image=f['urlToImage'],
                        author=f['author'], url=f['url'], category='science',
                        publishedAt=f['publishedAt'], content=f['content']).save()
    catdata = Newscatwise.objects.filter(category='science').order_by('-post_id')
    context = {'catdata': catdata}
    return render(request, 'newsapp/science.html', context)


def sports(request):
    newsapi = NewsApiClient(api_key='f2d21efaf1e4456db37ccaefbb14a4c2')
    top = newsapi.get_top_headlines(category='sports', language='en')

    l = top['articles']

    for i in range(len(l)):
        f = l[i]
        f['publishedAt'] = f['publishedAt'][0:10]
        if not Newscatwise.objects.filter(title=f['title']).exists():
            Newscatwise(title=f['title'], description=f['description'], image=f['urlToImage'],
                        author=f['author'], url=f['url'], category='sports',
                        publishedAt=f['publishedAt'], content=f['content']).save()
    catdata = Newscatwise.objects.filter(category='sports').order_by('-post_id')
    context = {'catdata': catdata}
    return render(request, 'newsapp/sports.html', context)


def technology(request):
    newsapi = NewsApiClient(api_key='f2d21efaf1e4456db37ccaefbb14a4c2')
    top = newsapi.get_top_headlines(category='technology', language='en')

    l = top['articles']

    for i in range(len(l)):
        f = l[i]
        f['publishedAt'] = f['publishedAt'][0:10]
        if not Newscatwise.objects.filter(title=f['title']).exists():
            Newscatwise(title=f['title'], description=f['description'], image=f['urlToImage'],
                        author=f['author'], url=f['url'], category='technology',
                        publishedAt=f['publishedAt'], content=f['content']).save()
    catdata = Newscatwise.objects.filter(category='technology').order_by('-post_id')
    context = {'catdata': catdata}
    return render(request, 'newsapp/technology.html', context)


# def countryblogpost(request, id):
#     post = Newscountrywise.objects.filter(post_id=id).first()
#     context = {'post': post}
#     return render(request, 'newsapp/blogpost.html', context)
#
#
# def catblogpost(request, id):
#     post = Newscatwise.objects.filter(post_id=id).first()
#     context = {'post': post}
#     return render(request, 'newsapp/blogpost.html', context)


def search(request):
    query = request.GET['query']
    newsapi = NewsApiClient(api_key='f2d21efaf1e4456db37ccaefbb14a4c2')
    top = newsapi.get_top_headlines(q=(str(query)), language='en')

    l = top['articles']

    for i in range(len(l)):
        f = l[i]
        f['publishedAt'] = f['publishedAt'][0:10]
        if not newslist.objects.filter(title=f['title']).exists():
            newslist(title=f['title'], description=f['description'], image=f['urlToImage'],
                        author=f['author'], url=f['url'],
                        publishedAt=f['publishedAt'], content=f['content']).save()
    if len(query) > 100:
        allPosts = []
    else:
        allPosts = (newslist.objects.filter(title__icontains=query).order_by('-post_id') or Newscountrywise.objects.filter(title__icontains=query).order_by('-post_id') or Newscatwise.objects.filter(title__icontains=query).order_by('-post_id'))
    if not allPosts:
        messages.error(request, "Please enter valid search")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'newsapp/search.html', params)


def corona(request):
    newsapi = NewsApiClient(api_key='f2d21efaf1e4456db37ccaefbb14a4c2')
    top = newsapi.get_top_headlines(q='corona')

    l = top['articles']

    for i in range(len(l)):
        f = l[i]
        f['publishedAt'] = f['publishedAt'][0:10]
        if not Newscatwise.objects.filter(title=f['title']).exists():
            Newscatwise(title=f['title'], description=f['description'], image=f['urlToImage'],
                     author=f['author'], url=f['url'],category='corona',
                     publishedAt=f['publishedAt'], content=f['content']).save()

    mylist = Newscatwise.objects.filter(category='corona').order_by('-post_id')

    extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
    URL = 'https://www.mohfw.gov.in/'

    SHORT_HEADERS = ['SNo', 'State', 'Indian_Confirmed',
                     'Foreign_Confirmed', 'Cured', 'Death']

    response = requests.get(URL).content
    soup = BeautifulSoup(response, 'html.parser')
    header = extract_contents(soup.tr.find_all('th'))

    stats = []
    all_rows = soup.find_all('tr')

    for row in all_rows:
        stat = extract_contents(row.find_all('td'))
        c = 0
        tc = 0
        d = 0
        if stat:
            if len(stat) == 5:
                # last row
                stat = ['', *stat]
                stats.append(stat)
            elif len(stat) == 6:
                stats.append(stat)
    return render(request, 'newsapp/corona.html', {"mylist": mylist, "stats": stats})



