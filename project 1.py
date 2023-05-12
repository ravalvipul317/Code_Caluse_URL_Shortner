from flask import Flask, redirect, request
import string
import random

app = Flask(__name__)
url_mapping = {}

def generate_short_url():
    """Generates a random 6-character string for use as a short URL."""
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for i in range(6))
    return short_url

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Creates a new short URL for a given long URL."""
    long_url = request.form['url']
    short_url = generate_short_url()
    url_mapping[short_url] = long_url
    return short_url

@app.route('/<short_url>')
def redirect_to_url(short_url):
    """Redirects a short URL to its corresponding long URL."""
    long_url = url_mapping.get(short_url)
    if long_url is None:
        return "Invalid URL"
    return redirect(long_url)

if __name__ == '__main__':
    app.run(debug=True)
