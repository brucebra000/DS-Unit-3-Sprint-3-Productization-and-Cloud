
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['CUSTOM_VAR'] = 5
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web_app.db'

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#Routing

@app.route('/')
def index():
    #return 'hello world'
    return render_template('homepage.html')

@app.route('/about')
def about():
    return 'about me'

@app.route('/users')
@app.route('/users.json')
def users():
    users = User.query.all()

    users_response = []
    for u in users:
        user_dict = u.__dict__
        del user_dict['_sa_instance_state']
        users_response.append(user_dict)

    return jsonify(users_response)

@app.route('/users/create', methods=['Post'])
def create_user():
    print('Creating a new user...')
    print('Form data:', dict(request.form))

    if 'name' in request.form:
        name = request.form['name']
        print(name)
        db.session.add(User(name=name))
        db.session.commit()
        return jsonify({'message': 'created ok', 'name': name})
    else:
        return jsonify({'message': 'oops please specify a name'})
    
@app.route('/hello')
def hello(name=None):
    print('Visiting the hello page')
    print('Request params:', dict(request.args))

    if 'name' in request.args:
        name = request.args['name']
        message = f'hello, {name}'
    else:
        message = 'hello world'

    return render_template('hello.html', message=message)
