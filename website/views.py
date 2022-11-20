from flask import Blueprint, redirect, render_template, request, g, session, url_for
from decouple import config
import requests

news = Blueprint('news', __name__)
api_key = config('NEWS_API')

@news.route('/')
def home():
    if not session:
        return redirect(url_for('views.login'))
    url = "https://newsapi.org/v2/top-headlines?country=in&language=en&apikey="+api_key+""
    trending = "https://newsapi.org/v2/everything?q=trending&language=en&sortBy=publishedAt&apiKey="+api_key+""
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""

    url_request = requests.get(url).json()
    top_request = requests.get(top).json()
    trending_request = requests.get(trending).json()

    case = {
        'articles': url_request['articles']
    }
    top = {
        'articles': top_request['articles']
    }
    trending = {
        'articles': trending_request['articles']
    }
    return render_template('index.html', cases=case, tops=top, trendings=trending)

@news.route('/nav')
def nav():
    
    return render_template('nav.html')

@news.route('/search')
def search():
    g.q = request.args.get('q')
    
    trending = 'https://newsapi.org/v2/everything?q='+g.q+'&language=en&apiKey='+api_key+""
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""

    trending_request = requests.get(trending).json()
    top_request = requests.get(top).json()

    trending = {
        'articles': trending_request['articles']
    }
    top = {
        'articles': top_request['articles']
    }
    return render_template('/components/search.html',q= g.q, search = trending, tops = top)

# Routing for Top Cities:
# Chennai
@news.route('/chennai')
def chennai():
    if not session:
        return render_template('login.html')
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""
    chennai = "https://newsapi.org/v2/everything?q=chennai&language=en&sortBy=publishedAt&apiKey="+api_key+""
    chennai_request = requests.get(chennai).json()
    top_request = requests.get(top).json()
    top = {
        'articles': top_request['articles']
    }

    chennai = {
        'articles': chennai_request['articles']
    }
    return render_template('/cities/chennai.html', tops=top, news=chennai)

# Bengaluru


@news.route('/bangalore')
def bangalore():
    if not session:
        return render_template('login.html')
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""
    chennai = "https://newsapi.org/v2/everything?q=bangalore&language=en&sortBy=publishedAt&apiKey="+api_key+""
    chennai_request = requests.get(chennai).json()
    top_request = requests.get(top).json()
    top = {
        'articles': top_request['articles']
    }

    chennai = {
        'articles': chennai_request['articles']
    }
    return render_template('/cities/bangalore.html', tops=top, news=chennai)

# Mumbai


@news.route('/mumbai')
def mumbai():
    if not session:
        return render_template('login.html')
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""
    chennai = "https://newsapi.org/v2/everything?q=mumbai&language=en&sortBy=publishedAt&apiKey="+api_key+""
    chennai_request = requests.get(chennai).json()
    top_request = requests.get(top).json()
    top = {
        'articles': top_request['articles']
    }

    chennai = {
        'articles': chennai_request['articles']
    }
    return render_template('/cities/mumbai.html', tops=top, news=chennai)

# Kolkata


@news.route('/kolkata')
def kolkata():
    if not session:
        return render_template('login.html')
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""
    chennai = "https://newsapi.org/v2/everything?q=kolkata&language=en&sortBy=publishedAt&apiKey="+api_key+""
    chennai_request = requests.get(chennai).json()
    top_request = requests.get(top).json()
    top = {
        'articles': top_request['articles']
    }

    chennai = {
        'articles': chennai_request['articles']
    }
    return render_template('/cities/kolkata.html', tops=top, news=chennai)

# Hyderabad


@news.route('/hyderabad')
def hyderabad():
    if not session:
        return render_template('login.html')
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""
    chennai = "https://newsapi.org/v2/everything?q=hyderabad&language=en&sortBy=publishedAt&apiKey="+api_key+""
    chennai_request = requests.get(chennai).json()
    top_request = requests.get(top).json()
    top = {
        'articles': top_request['articles']
    }

    chennai = {
        'articles': chennai_request['articles']
    }
    return render_template('/cities/hyderabad.html', tops=top, news=chennai)

# Delhi


@news.route('/delhi')
def delhi():
    if not session:
        return render_template('login.html')
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""
    chennai = "https://newsapi.org/v2/everything?q=delhi&language=en&sortBy=publishedAt&apiKey="+api_key+""
    chennai_request = requests.get(chennai).json()
    top_request = requests.get(top).json()
    top = {
        'articles': top_request['articles']
    }

    chennai = {
        'articles': chennai_request['articles']
    }
    return render_template('/cities/delhi.html', tops=top, news=chennai)

# Lucknow


@news.route('/Lucknow')
def lucknow():
    if not session:
        return render_template('login.html')
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""
    chennai = "https://newsapi.org/v2/everything?q=lucknow&language=en&sortBy=publishedAt&apiKey="+api_key+""
    chennai_request = requests.get(chennai).json()
    top_request = requests.get(top).json()
    top = {
        'articles': top_request['articles']
    }

    chennai = {
        'articles': chennai_request['articles']
    }
    return render_template('/cities/lucknow.html', tops=top, news=chennai)

# Patna


@news.route('/patna')
def patna():
    if not session:
        return render_template('login.html')
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""
    chennai = "https://newsapi.org/v2/everything?q=patna&language=en&sortBy=publishedAt&apiKey="+api_key+""
    chennai_request = requests.get(chennai).json()
    top_request = requests.get(top).json()
    top = {
        'articles': top_request['articles']
    }

    chennai = {
        'articles': chennai_request['articles']
    }
    return render_template('/cities/patna.html', tops=top, news=chennai)

# Kochi


@news.route('/kochi')
def kochi():
    if not session:
        return render_template('login.html')
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""
    chennai = "https://newsapi.org/v2/everything?q=kochi&language=en&sortBy=publishedAt&apiKey="+api_key+""
    chennai_request = requests.get(chennai).json()
    top_request = requests.get(top).json()
    top = {
        'articles': top_request['articles']
    }

    chennai = {
        'articles': chennai_request['articles']
    }
    return render_template('/cities/kochi.html', tops=top, news=chennai)

# Ranchi


@news.route('/ranchi')
def ranchi():
    if not session:
        return render_template('login.html')
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""
    chennai = "https://newsapi.org/v2/everything?q=ranchi&language=en&sortBy=publishedAt&apiKey="+api_key+""
    chennai_request = requests.get(chennai).json()
    top_request = requests.get(top).json()
    top = {
        'articles': top_request['articles']
    }

    chennai = {
        'articles': chennai_request['articles']
    }
    return render_template('/cities/ranchi.html', tops=top, news=chennai)


@news.route('/tech')
def tech():
    if not session:
        return render_template('login.html')
    url = "https://newsapi.org/v2/top-headlines?category=technology&apikey="+api_key+""

    r = requests.get(url).json()
    headline = {
        'articles': r['articles']
    }
    return render_template('tech.html', headlines=headline)
