from flask import Flask, render_template
#import login_utils
application = Flask(__name__)


@application.route("/")
def home():
    return render_template('home2.html')
    

@application.route("/logout")
def logout():
    session['user'] = "Anonymous"
    session['logged_in'] = False
    return redirect('/')

if __name__=="__main__":
    application.run(host='0.0.0.0')

