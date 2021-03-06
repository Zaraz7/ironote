from http.client import responses
from urllib import response
from flask import Flask, render_template, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class StatusApi(Resource):
    def get(self):
        return {"status" : "OK"}
api.add_resource(StatusApi, '/StatusApi')

class GetHelp(Resource):
    def get(self):
        return {"status" : "OK"}
    def post(self):
        return request.json
        
api.add_resource(GetHelp, '/help')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
