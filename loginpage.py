from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('main.html')

database={"surya":"488","yashaswini":"545","shreya":"439","vamshi":"525"}

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    
    if username in database:
        if database[username]==password:
            return render_template('success.html',name=username)
        else:
            return render_template('main.html',invalid="Wrong password")
    else:
        return render_template('main.html',invalid='Invalid username')

if __name__ == '__main__':
    app.run(debug=True)