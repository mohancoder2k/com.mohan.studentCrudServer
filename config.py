class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345678@localhost/student_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
