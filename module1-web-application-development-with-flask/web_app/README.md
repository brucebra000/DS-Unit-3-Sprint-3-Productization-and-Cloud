$ FLASK_APP=app.py flask db init        #generates app/migrations dir
$ FLASK_APP=app.py flask db migrate     #creates the db
$ FLASK_APP=app.py flask db upgrade     #creates the tables