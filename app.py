from flask import Flask, render_template, url_for, request, session, redirect, flash

app = Flask(__name__)

app.secret_key = 'V6DyqvMPGeSe8a2E'

@app.route('/')
def home():
    return render_template('index.html')

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        if (request.form['username'] == 'alejo') and (request.form['password'] == 'alejo'):
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect(url_for('welcome'))
        else:
            flash('User and/or password incorrect.')
            return redirect(url_for('home'))
    else:
        return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/welcome')
def welcome():
    if 'logged_in' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('home'))


@app.route('/authfailed')
def authfailed():
    return render_template('authfailed.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
