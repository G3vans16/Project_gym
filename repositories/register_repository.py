from db.run_sql import run_sql

from models.gym_class import GymClass
from models.member import Member
from models.register import Register
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository

def save(register):
    sql = "INSERT INTO registers (member_id, gym_class_id) VALUES (%s, %s) RETURNING id"
    values = [register.member.id, register.gym_class.id]
    results = run_sql(sql, values)
    register.id = results[0]['id']
    return register