"""
config.py
- settings for the flask application object
"""

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="mediabias",
    password="Tools4bias*Detection",
    hostname="mediabias.mysql.pythonanywhere-services.com",
    databasename="mediabias$survey"
)

class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 299
    SECRET_KEY = 'key'
