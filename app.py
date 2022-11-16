from flask import Flask, render_template
import requests
from sqlalchemy import case

app = Flask(__name__)
app.secret_key = "123456789"


# https://newsapi.org/v2/top-headlines?country=in&category=general&apikey=04936e1d20cf4a7db857af7d646cb0a7
@app.route('/')
def index():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=general&apikey=04936e1d20cf4a7db857af7d646cb0a7"
    r = requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('news.html', cases = case)

@app.route('/tech')
def tech():
    url= "https://newsapi.org/v2/top-headlines?category=technology&apikey=04936e1d20cf4a7db857af7d646cb0a7"
    r = requests.get(url).json()
    headline = {
        'articles': r['articles']
    }
    return render_template('tech.html',headlines = headline)

if __name__ == '__main__':
    app.run(debug=True)
