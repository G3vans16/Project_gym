from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.register_repository as register_repository

registers_blueprint = Blueprint("registers", __name__)
