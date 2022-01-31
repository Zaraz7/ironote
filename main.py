from flask import Flask, render_template, request, session
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Login(Resource):
    def get(self):
        return {"test GET": "OK"}

    def post(self): # take {login:str, password:str}
        respons_ = request.json
        
        respons_["login"]
        respons_["password"]

        return {"rederect": "ok", "url" : "./"}

api.add_resource(Login, '/Login')

class StatusApi(Resource):
    def get(self):
        return {"status" : "ok"}

api.add_resource(StatusApi, '/StatusApi')

class GetHelp(Resource):
    def get(self):
        return {"status" : "OK"}

    def post(self):
        print(request.json)
        return request.json

api.add_resource(GetHelp, '/help')

# -- -==- -- | -- -==- -- 

@app.route('/TestRequests')
def TestRequests():
    return render_template('TestRequests.html')

@app.route('/')
def LoginUp():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5005)
