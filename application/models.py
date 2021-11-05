from application import db

class Employee(db.Model):
    empno = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    salary = db.Column(db.Integer)
    marks = db.Column(db.Integer)
    subject = db.Column(db.String(50))
    dept = db.Column(db.String(50))