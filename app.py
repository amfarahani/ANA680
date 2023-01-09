from flask import Flask

app = Flask(__name__)  #Create the app class


@app.route('/', methods=['GET'])  #'/' root or starting page, the python function helloANA680 is called
def helloANA680( ):
  return 'Hello class'


@app.route('/results')
def output():
  return "Here are the resuts"
 

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=105) # default localhost or 127.0.0.1, port = 5000