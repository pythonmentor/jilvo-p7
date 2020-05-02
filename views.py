from flask import Flask,url_for

app = Flask(__name__)

# # Config options - Make sure you created a 'config.py' file.
# app.config.from_object('config')
# # To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
@app.route('/index')
def index():
        return("Hello world")
if __name__ == "__main__":
        app.run()

@app.route('/profil')
def profil():
        return('Bonjour vous avez')
if __name__ == "__main__":
        app.run()