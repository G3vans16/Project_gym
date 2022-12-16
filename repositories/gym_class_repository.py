from db.run_sql import run_sql

from models.gym_class import GymClass
from models.member import Member

def save(gym_class):
    sql = "INSERT INTO gym_classes(class_name, description) VALUES (%s, %s) RETURNING id"
    values = [gym_class.class_name, gym_class.description]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

def select_all():
    gym_classes = []
    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)

    for row in results:
        gym_class = GymClass(row['class_name'], row['description'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def select(id):
    gym_class = None
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        gym_class = GymClass(result['class_name'], result['description'], result['id'])
    return gym_class

def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)

def gym_classes_for_member(member):
    gym_classes = []
    sql = "SELECT gym_classes.* FROM gym_classes INNER JOIN registers ON registers.gym_class_id = gym_classes.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        gym_class = GymClass(row['class_name'], row['description'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def gym_class_for_register(register):
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [register.gym_class.id]
    results = run_sql(sql,values)[0]
    gym_class = GymClass(results['class_name'], results['description'], results['id'])
    return gym_class