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
		task_state = request.form.get('task_state')
		message = request.form.get('message')
		actual_fileName = request.form.get('actual_fileName')
		reminderDate = request.form.get('reminder_date')
		location = request.form.get('location')
		print(filename,category,task_state,message,actual_fileName,reminderDate,location)		
		return redirect(url_for('add'))	

	elif request.method =="GET":
		return render_template("FileAdd.html")	
	return render_template("FileAdd.html")	

#change this value in SQLITE as we need savedDate as well today's date or current date
class file(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    filename = db.Column(db.String)
    task_state = db.Column(db.String(20))
    message = db.Column(db.String)
    actual_name = db.Column(db.String)
    reminderDate = db.Column(db.String(11))
    location = db.Column(db.String)
    current_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)



@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html",error = e)





if __name__ =="__main__":
	app.run(debug=True)
	db.create_all()