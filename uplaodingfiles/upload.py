from fileinput import filename
from flask import *
app=Flask(__name__)
@app.route('/')
def main():
    render_template('upload.html')
@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        f=request.files['file']
        f.save(f.filename)
        return render_template('successpage.html',name=f.filename)
if __name__=='__main__':
    app.run()
