from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("bookings")