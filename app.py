from flask import Flask, render_template, request
from constants import username, password
import sendgrid
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
    message = sendgrid.Message("sagnew92@gmail.com", "message subject", "plaintext message body",
                    "HTML message body")
    # add a recipient
    message.add_to("detox27@gmail.com", "John Doe")
    # use the Web API to send your message
    s.web.send(message)
    return "Fuck off I'm not searching for " + query


if __name__ == '__main__':
    app.run()
