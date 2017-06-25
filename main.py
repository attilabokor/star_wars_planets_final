import queries
from flask import Flask, session, redirect, url_for, escape, request, render_template, flash

app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/', methods=['GET'])
def load_index():
    if 'username' in session:
        login_name = 'Logged in as ' + session['username']
        login_button = 'Log Out'
        login_url = '/logout'
        return render_template('index.html', login_name=login_name,
                                             login_button=login_button,
                                             login_url=login_url)
    else:
        login_name = ''
        login_button = 'Log in'
        login_url = '/login'
        return render_template('index.html', login_name=login_name,
                                             login_button=login_button,
                                             login_url=login_url)


@app.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == 'POST':
            username = request.form['usrname']
            password = request.form['pass']
            user_check = queries.check_user(username, password)
            if user_check[0][0] == username:
                session['username'] = request.form['usrname']
                return redirect('/')

    except:
        return redirect('/login')
    return render_template('/login.html')


@app.route('/register', methods=["POST", "GET"])
def registration():
    """
    When user data sent from the website, it creates a new database row in users table.
    """
    if request.method == 'POST':
        user_name = request.form["usrname"]
        password = request.form["pass"]
        queries.register_new_user(user_name, password)
        return redirect('/')
    else:
        return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=None)    
