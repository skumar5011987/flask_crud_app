from flask import Flask, jsonify, render_template, request, redirect, url_for
from models import db, Students
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:postgres@localhost:5433/flask_crud_app"
app.config['SQL_ALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_request
def create_table():
    db.create_all()

@app.route('/home',methods=['GET'])
def home():
    if request.method == 'GET':
        students = Students.query.all()
        return render_template('home.html', context=students)

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    elif request.method == 'POST':        
        name = request.form['sName']
        roll = request.form['sRoll']
        course = request.form['sCourse']
        email = request.form['sEmail']
        contact = request.form['sContact']        
        
        student = Students(
            name=name,
            roll=roll,
            course = course,
            email = email,
            contact= contact
        )
        db.session.add(student)
        db.session.commit()
        return redirect('/create')

@app.route('/<roll>/update/', methods=['GET','POST'])
def update(roll):
    if request.method == 'GET':
        try:
            student = Students.query.get(roll)
            return render_template('update.html', context=student)
        except Exception as e:
            print('Error:',e)
            return redirect('/home')
    elif request.method == 'POST':
        try:
            student = Students.query.get(roll)
            student.name = request.form['sName']
            student.roll = roll
            student.course = request.form['sCourse']
            student.email = request.form['sEmail']
            student.contact = request.form['sContact']
            db.session.commit()
            return redirect('/home')
        except Exception as e:
            print('Error:',e)
            return redirect('/home')

@app.route('/<roll>/delete', methods=['GET','POST'])
def delete(roll):
    if request.method == 'POST':
        try:   
            student = Students.query.get(roll)     
            db.session.delete(student)
            db.session.commit()
        except Exception as e:
                print('Error:',e)
    elif request.method == 'GET':
        return render_template('delete.html')
    
    return redirect('/home')

app.run(host='localhost',port=5000)