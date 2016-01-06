from flask import Flask, render_template
import login_utils
application = Flask(__name__)


@application.route("/")
def home():
    if 'logged_in' not in session:
        session['logged_in'] = False
    if 'user' not in session:
        session['user'] = 'Anonymous'
    if request.method=="GET":
        return render_template("home.html", log = "" )
    if request.method=="POST":
        button = request.form['button']
        username=request.form['username']
        password=request.form['password']
        if button=="Login":
            if utils.authenticate(username,password):
                currentUser = username
                session['user'] = username
                session['logged_in'] = True
                posts = utils.getPosts()
                return redirect("/posts")
            else:
                return render_template("index.html", log = "fail")
        else:
            return "bye"

@app.route("/logout")
def logout():
    session['user'] = "Anonymous"
    session['logged_in'] = False
    return redirect('/')

if __name__=="__main__":
    app.debug=True
    app.secret_key = "Wayez is awesome"
    application.run(host='0.0.0.0')

