import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgres://sligvgaxcuplpn:9e8446c8f5f25489a9b91f8566987ac7472fcb4b06bd2400e9d6575f965d46f2@ec2-35-174-127-63.compute-1.amazonaws.com:5432/d8mq86ue2m3lah')

    MAIL_SERVER = 'aluiza.primo@gmail.com'
    MAIL_PORT = 5432
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('sligvgaxcuplpn')
    MAIL_PASSWORD = os.environ.get('9e8446c8f5f25489a9b91f8566987ac7472fcb4b06bd2400e9d6575f965d46f2')