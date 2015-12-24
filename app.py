from flask import Flask
application = Flask(__name__)

@application.route("/")
def home():
    return "1:24AM"

if __name__=="__main__":
    application.run(host='0.0.0.0')

