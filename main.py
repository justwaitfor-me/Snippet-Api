from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
  return '<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Document</title> </head> <body> <h1>Homepage</h1> </body> </html>'

@app.route('/api')
def api():
  user_input = request.args.get('input')
  response = user_input
  
  json = {
    'input': user_input,
    'response': response,
    'author': 'JustWait'
  }
  
  return json

if __name__ == '__main__':
  app.run()