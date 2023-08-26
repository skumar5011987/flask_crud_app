from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Students(db.Model):
    __tablename__ = 'students'
    
    name = db.Column(db.String())
    roll = db.Column(db.String(6), primary_key=True,nullable=False,unique=True)
    course = db.Column(db.String())
    email = db.Column(db.String())
    contact = db.Column(db.String(10),nullable=False)
    
    
    def __init__(self,name,roll,course,email,contact):
        self.name = name
        self.roll = roll
        self.course = course
        self.email = email
        self.contact = contact
        
        def __repr__(self):
            return f"{self.name}"
