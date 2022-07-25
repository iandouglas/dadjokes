# Serving Up Dad Jokes with Docker and CircleCI

---

Today we're going to build a quick Flask application to serve "dad jokes" from a Docker container


## Prior Knowledge / Installation

- comfort using a local terminal
- [Python 3.8 or newer](https://www.python.org/downloads/) installed (Mac OS X will have this already) and knowledge of "[virtual environments](https://docs.python.org/3/library/venv.html)"
- [CircleCI account](https://circleci.com) created and logged in

## Python Virtual Environment

Let's begin by setting up a virtual environment for our local work. Open your command-line terminal

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

At this point you should see the `(venv)` marker on your shell prompt.

Let's install the Flask framework to get started from the provided `requirements.txt` file:

```bash
(venv) $ pip3 install -r requirements.txt
```

This will install Flask v2.0.2 and its necessary dependencies.


## Python Code to get started

We're going to begin by writing a very simple Flask application that reads a file of data jokes in JSON format, and return a random joke from the file.

Let's store this in a filename called `dadjokes.py`:

```python
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


```

Let's run it locally to ensure this works in our browser:

```bash
(venv) $ export FLASK_APP=api
(venv) $ export FLASK_ENV=development
(venv) $ flask run

 * Serving Flask app 'api' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 192-481-024
```

Your IP address may differ, but the output is showing us the URL to hit in our browser. In this case, visiting `http://127.0.0.1:5000/` should show us a random "dad joke" and hitting refresh should load a different joke each time.

If we visit http://localhost:5000/hello we should see a JSON object with a key `hello` and a value of `world`.

## CircleCI Integration

