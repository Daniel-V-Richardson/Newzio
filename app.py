from flask import Flask, render_template
import requests

app = Flask(__name__)
app.secret_key = "123456789"


@app.route('/nav')
def nav():
    return render_template('nav.html')

# https://newsapi.org/v2/top-headlines?country=in&category=general&apikey=04936e1d20cf4a7db857af7d646cb0a7


@app.route('/')
def index():

    url = "https://newsapi.org/v2/top-headlines?country=in&language=en&apikey=04936e1d20cf4a7db857af7d646cb0a7"
    trending = "https://newsapi.org/v2/everything?q=trending&language=en&sortBy=publishedAt&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey=04936e1d20cf4a7db857af7d646cb0a7"

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


@app.route('/signin')
def signin():
    return render_template('/components/signin.html')


@app.route('/register')
def register():
    return render_template('/components/register.html')


# Routing for Top Cities:
# Chennai
@app.route('/chennai')
def chennai():
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    chennai = "https://newsapi.org/v2/everything?q=chennai&language=en&sortBy=publishedAt&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
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


@app.route('/bangalore')
def bangalore():
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    chennai = "https://newsapi.org/v2/everything?q=bangalore&language=en&sortBy=publishedAt&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
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


@app.route('/mumbai')
def mumbai():
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    chennai = "https://newsapi.org/v2/everything?q=mumbai&language=en&sortBy=publishedAt&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
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


@app.route('/kolkata')
def kolkata():
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    chennai = "https://newsapi.org/v2/everything?q=kolkata&language=en&sortBy=publishedAt&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
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


@app.route('/hyderabad')
def hyderabad():
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    chennai = "https://newsapi.org/v2/everything?q=hyderabad&language=en&sortBy=publishedAt&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
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


@app.route('/delhi')
def delhi():
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    chennai = "https://newsapi.org/v2/everything?q=delhi&language=en&sortBy=publishedAt&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
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


@app.route('/Lucknow')
def lucknow():
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    chennai = "https://newsapi.org/v2/everything?q=lucknow&language=en&sortBy=publishedAt&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
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


@app.route('/patna')
def patna():
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    chennai = "https://newsapi.org/v2/everything?q=patna&language=en&sortBy=publishedAt&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
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


@app.route('/kochi')
def kochi():
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    chennai = "https://newsapi.org/v2/everything?q=kochi&language=en&sortBy=publishedAt&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
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


@app.route('/ranchi')
def ranchi():
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    chennai = "https://newsapi.org/v2/everything?q=ranchi&language=en&sortBy=publishedAt&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    chennai_request = requests.get(chennai).json()
    top_request = requests.get(top).json()
    top = {
        'articles': top_request['articles']
    }

    chennai = {
        'articles': chennai_request['articles']
    }
    return render_template('/cities/ranchi.html', tops=top, news=chennai)


@app.route('/tech')
def tech():
    url = "https://newsapi.org/v2/top-headlines?category=technology&apikey=04936e1d20cf4a7db857af7d646cb0a7"

    r = requests.get(url).json()
    headline = {
        'articles': r['articles']
    }
    return render_template('tech.html', headlines=headline)


if __name__ == '__main__':
    app.run(debug=True)
