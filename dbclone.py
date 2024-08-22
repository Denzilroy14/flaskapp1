from flask import*
import sqlite3
app=Flask(__name__)
@app.route('/')
@app.route('/home')
def index():
    return render_template('clickpage.html')
connect=sqlite3.connect('database.db')
cur=connect.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS students(student_name TEXT,age INTEGER,college TEXT)')
@app.route('/welcome',methods=['GET','POST'])
def welcome():
    if request.method=='POST':
        name=request.form['studentname']
        age=request.form['age']
        college=request.form['previous college']
        with sqlite3.connect('database.db')as st:
            cur=st.cursor()
            cur.execute('INSERT INTO students(student_name,age,college)VALUES(?,?,?)',(name,age,college))
            st.commit()
        return render_template('clickpage.html')
    else:
        return render_template('adddetails.html')
@app.route('/viewing')
def viewing():
    with sqlite3.connect('database.db')as view:
        curr=view.cursor()
        curr.execute('SELECT * FROM students')
        values=curr.fetchall()
    return render_template('viewingfiles.html',data=values)
if __name__=='__main__':
    app.run()






        
