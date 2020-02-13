from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    #return 'Hello World'
    return render_template('')

@app.route('/')
def about():
    return 'About me'

@app.route('/users')
@app.route('/users.json')
def users():
    users = [
        {'id':1, 'name': 'First User'},
        {'id':2, 'name': 'Second User'},
        {'id':3, 'name': 'Third User'}
    ]
    return jsonify(users)

@app.route('/users/create', methods = ['POST'])
def create_user():
    print('Creating a new user...')
    print('FORM DATA:', dict(request.form))

    return jsonify({'message': 'Created OK (TODO)'})
