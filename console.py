import pdb
from models.gym_class import GymClass
from models.member import Member
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
gym_class_repository.delete_all()
member_repository.delete_all()

member1 = Member("Shauna", "Alexander", 25)
member_repository.save(member1)

member2 = Member("Andrew", "Patterson", 33)
member_repository.save(member2)

member3 = Member("Jade", "Falconer", 26)
member_repository.save(member3)

gym_class1 = GymClass("Zumba", "ooooooh zumba")
gym_class_repository.save(gym_class1)

gym_class2 = GymClass("Yoga", "Stretch dem legs")
gym_class_repository.save(gym_class2)

gym_class3 = GymClass("Pilates", "literally don't know what this is")
gym_class_repository.save(gym_class3)

booking1 = Booking(member1, gym_class1)
booking_repository.save(booking1)

booking2 = Booking(member2, gym_class2)
booking_repository.save(booking2)

booking3 = Booking(member3, gym_class3)
booking_repository.save(booking3)

booking4 = Booking(member3, gym_class1)
booking_repository.save(booking4)