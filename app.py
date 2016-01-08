from flask import Flask, render_template
#import login_utils
application = Flask(__name__)


@application.route("/")#, methods=['GET','POST'])
def home():
#    if request.method=="GET":
    return render_template('home.html')

    '''  else:
        button = request.form['button']
        if button == "Create Account":
            newUser = request.form['newUser']
            newPass = request.form['newPass']
            newPassC = request.form['newPassC']
            #password match check
            if (newPass == newPassC):
                #username and password lengths check
                if len(newUser)<4:
                    return render_template('home.html',error2="Username must be longer than 4 characters")
                if len(newPass)<4:
                    return render_template('home.html',error2="Password must be longer than 4 characters")
                #account created successfully
                if  module.newUser(newUser,newPass):
                    return render_template('home.html',success="Account created!")
                #username taken error
                else:
                    return render_template('home.html',error2="Username taken")            
            else:
                return render_template('home.html',error2="Passwords do not match!")
        #Login
        #if credentials valid, log them in with session
        if button == "Login":
            uname = request.form['username']
            pword = request.form['password']
            if module.authenticate(uname,pword):
                if 'n' not in session:
                    session['n'] = uname
                    return redirect(url_for('home'))
                #else renders login w/ error message
            else:
                return render_template("home.html",error="Invalid Username or Password")'''    

@application.route("/logout")
def logout():
    session['user'] = "Anonymous"
    session['logged_in'] = False
    return redirect('/')

if __name__=="__main__":
    application.run(host='0.0.0.0')

