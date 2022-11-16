from flask import Flask, render_template
import requests

app = Flask(__name__)
app.secret_key = "123456789"


# https://newsapi.org/v2/top-headlines?country=in&category=general&apikey=04936e1d20cf4a7db857af7d646cb0a7
@app.route('/')
def index():
    
    url = "https://newsapi.org/v2/top-headlines?country=in&category=general&language=en&apikey=04936e1d20cf4a7db857af7d646cb0a7"
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    
    url_request = requests.get(url).json()
    top_request= requests.get(top).json()
    
    case = {
        'articles': url_request['articles']
    }
    top ={
       'articles': top_request['articles']
    }
   
    return render_template('index.html', cases = case, tops = top)
    
# Routing for Top Cities:
#Chennai
@app.route('/chennai')
def chennai():
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    chennai ="https://newsapi.org/v2/everything?q=chennai&language=en&sortBy=publishedAt&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    chennai_request= requests.get(chennai).json()
    top_request= requests.get(top).json()
    top ={
       'articles': top_request['articles']
    }
    
    chennai ={
        'articles': chennai_request['articles']
    }
    return render_template('chennai.html',tops = top ,news = chennai)

# Bengaluru
@app.route('/bangalore')
def bangalore():
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    chennai ="https://newsapi.org/v2/everything?q=bangalore&language=en&sortBy=publishedAt&apiKey=04936e1d20cf4a7db857af7d646cb0a7"
    chennai_request= requests.get(chennai).json()
    top_request= requests.get(top).json()
    top ={
       'articles': top_request['articles']
    }
    
    chennai ={
        'articles': chennai_request['articles']
    }
    return render_template('bangalore.html',tops = top ,news = chennai)


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
