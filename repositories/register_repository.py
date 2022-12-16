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

def select_all():
    registers = []
    sql = "SELECT * FROM registers"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        gym_class = gym_class_repository.select(row['gym_class_id'])
        register = Register(member, gym_class, row['id'])
        registers.append(register)
    return registers

def delete_all():
    sql = "DELETE FROM registers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM registers WHERE id = %s"
    values = [id]
    run_sql(sql, values)