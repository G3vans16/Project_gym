from flask import Flask, render_template

from controllers.booking_controller import bookings_blueprint
from controllers.gym_class_controller import gym_classes_blueprint
from controllers.member_controller import members_blueprint

import repositories.gym_class_repository as gym_class_repository

app = Flask(__name__)

app.register_blueprint(bookings_blueprint)
app.register_blueprint(gym_classes_blueprint)
app.register_blueprint(members_blueprint)

@app.route('/')
def home():
    gym_classes = gym_class_repository.select_all()
    return render_template('index.html', gym_classes=gym_classes)

if __name__ == '__main__':
    app.run(debug=True)