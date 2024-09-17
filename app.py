from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config
from models import db, Student

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])

@app.route('/student', methods=['POST'])
def add_student():
    data = request.json
    new_student = Student(name=data['name'], email=data['email'], age=data['age'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student.to_dict()), 201

@app.route('/student/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    student = Student.query.get(id)
    if not student:
        return jsonify({'message': 'Student not found'}), 404
    student.name = data['name']
    student.email = data['email']
    student.age = data['age']
    db.session.commit()
    return jsonify(student.to_dict())

@app.route('/student/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'message': 'Student not found'}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
