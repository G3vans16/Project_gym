import pdb
from models.gym_class import GymClass
from models.member import Member
from models.register import Register

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.register_repository as register_repository

register_repository.delete_all()
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

register1 = Register(member1, gym_class1)
register_repository.save(register1)

register2 = Register(member2, gym_class2)
register_repository.save(register2)

register3 = Register(member3, gym_class3)
register_repository.save(register3)

register4 = Register(member3, gym_class1)
register_repository.save(register4)