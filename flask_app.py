from flask import render_template
from surveyapi import create_app
from surveyapi.models import db
from flask_migrate import Migrate
from flask_cors import CORS

# Create the app
app = create_app.create_app()
CORS(app)

# Initialise DB
db.init_app(app)
with app.app_context():
    db.create_all()

# Initialise DB migrations
migrate = Migrate(app, db)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

















