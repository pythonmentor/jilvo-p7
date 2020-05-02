from flask import Flask

web_name = Flask(__name__)

@web_name.route('/')
def index():
    return "Hello world !"

if __name__ == "__main__":
    web_name.run()