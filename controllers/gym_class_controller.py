from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import GymClass
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

gym_classes_blueprint = Blueprint("gym_classes", __name__)

@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/index.html", gym_classes=gym_classes)

@gym_classes_blueprint.route("/gym_classes/<id>")
def show(id):
    gym_class = gym_class_repository.select(id)
    members = member_repository.members_for_gym_class(gym_class)
    
    return render_template("gym_classes/show.html", gym_class=gym_class, members=members)

@gym_classes_blueprint.route("/gym_classes/new", methods=['GET'])
def new_gym_class():
    return render_template("gym_classes/new.html")

@gym_classes_blueprint.route("/gym_classes",  methods=['POST'])
def create_gym_class():
    class_name = request.form['class_name']
    description = request.form['description']
    gym_class = GymClass(class_name, description)
    gym_class_repository.save(gym_class)
    return redirect('/gym_classes')

@gym_classes_blueprint.route("/gym_classes/<id>/edit", methods=['GET'])
def edit_gym_class(id):
    gym_class = gym_class_repository.select(id)
    return render_template('gym_classes/edit.html', gym_class = gym_class)

@gym_classes_blueprint.route("/gym_classes/<id>", methods=['POST'])
def update_gym_class(id):
    class_name = request.form['class_name']
    description = request.form['description']
    gym_class = GymClass(class_name, description, id)
    gym_class_repository.update(gym_class)
    return redirect('/gym_classes')

@gym_classes_blueprint.route("/gym_classes/<id>/delete", methods=['POST'])
def delete_gym_class(id):
    gym_class_repository.delete(id)
    return redirect('/gym_classes')