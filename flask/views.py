from flask import Flask,render_template,jsonify,make_response
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app=app)
@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')


@app.route('/api_google')
def grandpy():
    return_data = requests.get("https://world.openfoodfacts.org/api/v0/product/737628064502.json")
    return_data = return_data.json()
    
    response = app.response_class(
        response=json.dumps(return_data, ensure_ascii=False), status=200, mimetype="application/json"
    )
    return response

if __name__ == "__main__":
    app.run(debug=False)