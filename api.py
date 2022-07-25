from flask import Flask, jsonify, abort, make_response, request
import json
import random

jokes = []
with open('jokes.json', 'r') as joke_data:
  jokes = json.load(joke_data)

app = Flask(__name__)

    
@app.route("/")
def get_joke():
  jokes_index = random.randint(0,len(jokes)-1)
  random_joke = jokes[jokes_index]
  return jsonify({'joke': random_joke})

    
# get and jsonify the data
@app.route("/hello")
def get_greeting():
    return jsonify({'hello': 'world'})


if __name__ == "__main__":
  print(f'loaded {len(jokes)} jokes')
  app.run(debug=True, host='0.0.0.0')
