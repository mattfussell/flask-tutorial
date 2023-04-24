import os

baseDir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'a127d489fd2aae39ec24098525cbc426'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(baseDir,'site.db')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your email'
    MAIL_PASSWORD = 'your password'