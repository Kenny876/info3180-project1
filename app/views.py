from app import app, db, login_manager
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from forms import SignUpForm
from models import *
import datetime
import os


@app.route('/')
def home():
	return render_template("home.html")


@app.route('/profile', methods= ["GET","POST"])
def signup():
	form = SignUpForm()
	file_folder = app.config["UPLOAD_FOLDER"]
	if request.method == "POST":
		if form.validate_on_submit():
			fname = form.fname.data
			lname = form.lname.data
			age = form.age.data
			biography = form.biography.data
			sex = form.sex.data

			
			profPic = request.files["file"]
			file_path = os.path.join(file_folder, profPic.filename)
			# profPic = form.profPic.data
			profPic.save(file_path)


			date = datetime.datetime.now()

			user =UserProfile(first_name=fname, last_name=lname, join_date= date,gender=sex,age=age,prof_pic = file_path)
			db.session.add(user)
			db.session.commit()

	return render_template("signup.html", form= form)


	@app.route("/profiles", methods=["GET","POST"])
	def show_profiles():
		users = UserProfile.query.all()
		if users:
			return render_template("profile_list.html")


	@app.route("/profile/<userid>", methods =["GET","POST"])
	def view_profile():
		pass