from db.run_sql import run_sql

from models.gym_class import GymClass
from models.member import Member

def save(gym_class):
    sql = "INSERT INTO gym_classes(class_name, description) VALUES (%s, %s) RETURNING id"
    values = [gym_class.class_name, gym_class.description]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class