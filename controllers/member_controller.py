from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    gym_classes = gym_class_repository.gym_classes_for_member(member)
    return render_template("members/show.html", member=member, gym_classes=gym_classes)

@members_blueprint.route("/members/new", methods=['GET'])
def new_member():
    return render_template("members/new.html")

@members_blueprint.route("/members",  methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age   = request.form['age']
    member = Member(first_name, last_name, age)
    member_repository.save(member)
    return redirect('/members')