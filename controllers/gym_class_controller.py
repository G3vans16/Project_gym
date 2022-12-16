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

@gym_classes_blueprint.route("gym_classes/<id>")
def show(id):
    gym_class = gym_class_repository.select(id)
    members = member_repository.members_for_gym_class(gym_class)
    return render_template("gym_classes/show.html", gym_class=gym_class, members=members)