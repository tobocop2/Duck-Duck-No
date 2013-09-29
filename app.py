from flask import Flask, render_template, request
from constants import username, password
import sendgrid
import requests
import urllib2
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
    message = sendgrid.Message("nancy_reagan@duckduckno.com", "Terrorist alert", "plaintext message body",
                    "HTML message body")
    # add a recipient
    message.add_to("detox27@gmail.com", "John Doe")
    # use the Web API to send your message
    s.web.send(message)

    response = requests.get('http://api.duckduckgo.com/?q=' + query + '&format=json')
    json = response.text
    return render_template('results.html', json=json)


if __name__ == '__main__':
    app.run(debug = True)
