from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('secretkey')

db = SQLAlchemy(app)

class Employee(db.Model):
    empno = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    salary = db.Column(db.Integer)
    marks = db.Column(db.Integer)
    subject = db.Column(db.String(50))
    dept = db.Column(db.String(50))

db.drop_all()
db.create_all()

class AddEmp(FlaskForm):
    emp_name = StringField("Name")
    salary = IntegerField("Salary")
    marks = IntegerField("Marks")
    subject = SelectField("Subject", choices=[('python', 'Python'), ('java', 'Java'), ('php', 'PHP'), ('sql', 'SQL')])
    department = SelectField('Department', choices=[('IT', 'Information technology'), ('HR', 'Human Resources'), ('sales', 'Sales'), ('training', 'Training')])
    submit = SubmitField('Add Employee')

class UpdateEmp(FlaskForm):
    emp_name = StringField("Name")
    salary = IntegerField("Salary")
    marks = IntegerField("Marks")
    subject = SelectField("Subject", choices=[('python', 'Python'), ('java', 'Java'), ('php', 'PHP'), ('sql', 'SQL')])
    department = SelectField('Department', choices=[('IT', 'Information technology'), ('HR', 'Human Resources'), ('sales', 'Sales'), ('training', 'Training')])
    submit = SubmitField('Update Employee')

@app.route('/')
def home():
    emps = Employee.query.all()
    return render_template('homepage.html', records=emps)

@app.route('/editRecord/<int:empno>', methods=['GET', 'POST'])
def editRecordForm(empno):
    form = UpdateEmp()
    emp = Employee.query.filter_by(empno=empno).first()
    if request.method == 'POST':
        emp.name = form.emp_name.data
        emp.salary = form.salary.data
        emp.dept = form.department.data
        emp.subject = form.subject.data
        emp.marks = form.marks.data
        db.session.commit()
        return redirect("/")
    return render_template('EditForm.html', form=form)

@app.route("/filterrecords",methods=["POST"])
def filterrecords():
    if request.form["dept"]=="all":
        return redirect("/")
    else:
        data = Employee.query.filter_by(dept=request.form["dept"]).all()
        return render_template("Homepage.html",records=data)

@app.route("/saveRecord",methods=["GET","POST"])
def saveRecord():
    form = AddEmp()
    if request.method == 'POST':
        name=form.emp_name.data
        department=form.department.data
        salary=form.salary.data
        subject=form.subject.data
        marks=form.marks.data
        newemp = Employee(name=name, dept=department, salary=salary, subject=subject, marks=marks)
        db.session.add(newemp)
        db.session.commit()
        return redirect("/")
    return render_template("inputform.html", form=form)

@app.route("/personaldetails/<int:empno>")
def personalInformation(empno):
	data = Employee.query.filter_by(empno=empno).first()
	return render_template("personalinforamtion.html",record=data)

@app.route("/deleteEmployee/<int:empno>")
def deleteEmployee(empno):
    emp = Employee.query.filter_by(empno=empno).first()
    db.session.delete(emp)
    db.session.commit()
    return redirect("/")

app.run(debug=True)