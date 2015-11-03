from flask import Flask, render_template 
from flask.ext.login import login_required, current_user

app = Flask(__name__)





@app.route('/dashboard')
@login_required
def account():
    return "Hello World!"





if __name__ == '__main__':
	app.run()