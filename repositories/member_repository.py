from db.run_sql import run_sql

from models.gym_class import GymClass
from models.member import Member

def save(member):
    sql = "INSERT INTO members(first_name, last_name, age) VALUES (%s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.age]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member