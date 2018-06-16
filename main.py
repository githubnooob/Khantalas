from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///file.db'
db= SQLAlchemy(app)

@app.route("/search/")
def search():
	return render_template("Search.html")



@app.route("/add",methods=['GET','POST'])
def add():

	if request.method == "POST":
		filename = request.form.get('filename')
		category  = request.form.get('category')
		print(filename,category)		
		postInDatabase()
	elif request.method =="GET":
		pass

	return render_template("FileAdd.html")	



def postInDatabase():
	return redirect(url_for('add'))


class file(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    filename = db.Column(db.String)
    task_state = db.Column(db.String(20))
    message = db.Column(db.String)
    actual_name = db.Column(db.String)
    reminderDate = db.Column(db.String(11))
    location = db.Column(db.String)









if __name__ =="__main__":
	app.run(debug=True)
	db.create_all()