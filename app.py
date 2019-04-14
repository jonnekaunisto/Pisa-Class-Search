import json
from flask import Flask 
from flask import request
from flask import Response

app = Flask(__name__)

def html(content):  # Also allows you to set your own <head></head> etc
   return '<html><head>SlugSearch Results</head><br /><body>' + content + '</body></html>'

@app.route('/')
def index():
    return('Welcome to SlugSearch!')

@app.route('/search/<string:className>')
def search(className):
    res = classdic[className]
    buildStr = ""
    for key, value in res.items():
        buildStr += key + ': ' + str(value) + '<br />'
    return html(buildStr)

if __name__ == '__main__': #Create class dictionary
    with open('classdata.json','r', encoding='utf8') as file:
        dic = file.read()
    dic = json.loads(dic)['classes']

    classdic = {}
    for nbr,data in dic.items():
        classdic[data['name']] = data
    app.run(debug=True,host='0.0.0.0',port=8081)


