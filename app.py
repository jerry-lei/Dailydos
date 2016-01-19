from flask import Flask, render_template, request
import login_utils
application = Flask(__name__)


@application.route("/", methods=['GET','POST'])
def home():
#    return render_template('home.html')
    if request.method=="GET":
        return render_template('home.html')
    else:
        button = request.form['button']
        if button == "Create Account":
            user = request.form['new_username']
            password = request.form['new_password']
            confirm = request.form['new_confirm_password']
            #password match check
            if (password == confirm):
                #username and password lengths check
                if len(user)<4:
                    return render_template('home.html',errorC="Username must be longer than 4 characters")
                if len(password)<8:
                    return render_template('home.html',errorC="Password must be longer than 8 characters")
                #account created successfully
                if  login_utils.create_user(user,password):
                    return render_template('home.html',successC="Account successfully created! Login to access DailyDos.")
                #username taken error
                else:
                    return render_template('home.html',errorC="Username already in use. Please chose a different username")            
            else:
                return render_template('home.html',errorC="Passwords do not match")
        #Login
        #if credentials valid, log them in with session
        if button == "Login":
            user = request.form['login_username']
            password = request.form['login_password']
            if login_utils.authenticate(user,password):
                if 'n' not in session:
                    session['n'] = uname
                    return "hello"#redirect(url_for('home'))
                #else renders login w/ error message
            else:
                return render_template("home.html",errorL="Invalid Username or Password")



if __name__=="__main__":    
    application.run(host='0.0.0.0')
    """
    application.debug = True
    application.secret_key = "onetwothreefour"
    application.run(host='0.0.0.0', port = 5000)
    """
