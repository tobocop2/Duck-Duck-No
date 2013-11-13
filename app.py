from flask import Flask, render_template, request
from constants import username, password
import sendgrid
import requests
import urllib2
import os
s = sendgrid.Sendgrid(username, password, secure=True)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    # make a secure connection to SendGrid
    # make a message object
    message = sendgrid.Message("nancy_reagan@duckduckno.com", "Terrorist alert!", "plaintext message body",
            "This query was searched for " + query)
    # add a recipient
    message.add_to("customercare@nsa.gov", "John Doe")
    # use the Web API to send your message
    s.web.send(message)

    response = requests.get('http://api.duckduckgo.com/?q=' + query + '&format=json')
    json = response.text
    return render_template('results.html', json=json)


if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=port)
