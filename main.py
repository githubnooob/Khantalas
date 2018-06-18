from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
import os
import uploadFile
from DateConverter import DateConverter


app = Flask(__name__)

FILE_PATH = os.getcwd()+"/file.db"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+FILE_PATH
app.config['UPLOAD_FOLDER'] = uploadFile.UPLOAD_FOLDER
app.config['SECRET_KEY']= "siasdjasiodjldsj(S*u293719312.,12391u37912739723901/.,';][;][2209526510"

#initialize database
db= SQLAlchemy(app)

#dateConvertor
converter = DateConverter()


@app.route("/searchFile",methods=['GET','POST'])
def search():
	return render_template("Search.html")



@app.route("/addFile",methods=['GET','POST'])
def add():

	if request.method == "POST":

		# filename = request.form.get('filename')
		# category  = request.form.get('category')
		# category = change_into_string(category)
		# task_state = request.form.get('task_state')
		# task_state = change_into_string(task_state)
		# message = request.form.get('message')
		# message =change_into_string(message)
		# actual_fileName = request.form.get('actual_filename')
		# actual_fileName = change_into_string(actual_fileName)
		reminderDate = request.form.get('reminder_date')
		reminderDate=	change_into_string(reminderDate)

		#YearDate for checking 
		yearDate = reminderDate[0:4]
		print (check_date(yearDate))
		

		# location = request.form.get('location')
		# location = change_into_string(location)
		# print(filename,category,task_state,message,actual_fileName,reminderDate,location)
  #       if 'file' in request.files:	
  #       	print ("I am in this section")
	 #        file = request.files['file']
	 #        if filename =="":
	 #        	filename = change_into_string(file.filename)
	 #        else:
	 #        	filename = change_into_string(filename)	
	 #        print file.filename
	 #        if not file.filename == '' and uploadFile.allowed_file(file.filename):
	 #        	file.save(os.path.join(os.getcwd()+"/static/js/ViewerJS/Files", filename))	
	 #        newDataFileAdded = File(filename=filename,category=category,task_state=task_state,message= message,actual_name = actual_fileName,location =location,reminderDate=reminderDate)
	 #        db.session.add(newDataFileAdded)
	 #        db.session.commit()
		return redirect(url_for('add'))	

	elif request.method =="GET":
		return render_template("FileAdd.html")	
	return render_template("FileAdd.html")	


#change this value in SQLITE as we need savedDate as well today's date or current date

def change_into_string(value):
	return value.encode("utf-8")

def check_date(year):
	year_integer = int(year)
	current_date = datetime.datetime.now()
	current_year = current_date.year 
	return current_year , year_integer

def convert_to_English(year,month,date):
	converter.setNepaliDate(year, month, date)
	print(str(converter.getEnglishYear())+"/"+str(converter.getEnglishMonth())+"/"+str(converter.getEnglishDate()))



class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    filename = db.Column(db.String)
    task_state = db.Column(db.String(20))
    message = db.Column(db.String)
    actual_name = db.Column(db.String)
    reminderDate = db.Column(db.String(11))
    location = db.Column(db.String)
    current_date = db.Column(db.DateTime(), default=datetime.datetime.now)



@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html",error = e)





if __name__ =="__main__":
	app.run(debug=True)
	db.create_all()