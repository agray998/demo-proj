from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField
#blah2222
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