from flask import Flask, render_template, request, redirect

newzio = Flask(__name__)

@newzio.route('/')
def home():
    return render_template('main.html')


@newzio.route('/about')
def about():
    return render_template('about.html')


@newzio.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@newzio.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


if __name__ == "__main__":
    newzio.run(debug=True)
