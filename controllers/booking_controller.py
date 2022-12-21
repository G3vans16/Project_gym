from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.booking_repository as booking_repository

import pdb

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)

@bookings_blueprint.route("/bookings/new", methods = ['GET'])
def new_booking():
    members = member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    return render_template("bookings/new.html", members=members, gym_classes=gym_classes)

@bookings_blueprint.route("/bookings", methods = ['POST'])
def create_booking():
    members = member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    member_id = request.form['member_id']
    gym_class_id = request.form['gym_class_id']
    member = member_repository.select(member_id)
    gym_class = gym_class_repository.select(gym_class_id)
    new_booking = Booking(member, gym_class)
    
    current_bookings = booking_repository.select_all()
    for booking in current_bookings:
        if booking.member.id == int(member_id) and booking.gym_class.id == int(gym_class_id):
            return render_template("bookings/new.html", members=members, gym_classes=gym_classes, duplicate_error=True)

    booking_repository.save(new_booking)
    
    return redirect('/bookings')

@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect('/bookings')