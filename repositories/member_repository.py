from db.run_sql import run_sql

from models.gym_class import GymClass
from models.member import Member

def save(member):
    sql = "INSERT INTO members(first_name, last_name, age) VALUES (%s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.age]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['age'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        member = Member(result['first_name'], result['last_name'], result['age'], result ['id'])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def members_for_gym_class(gym_class):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE gym_class_id = %s"
    values = [gym_class.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['age'], row['id'])
        members.append(member)
    return members

def member_for_booking(booking):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [booking.member.id]
    results = run_sql(sql, values)[0]
    member = Member(results['first_name'], results['last_name'], results['age'], results['id'])
    return member

def update(member):
    sql = "UPDATE members SET (first_name, last_name, age) = (%s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.age, member.id]
    run_sql(sql, values)