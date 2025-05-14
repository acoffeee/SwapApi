from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {'id': 1, 'name': 'Ashley'},
    {'id': 2, 'name': 'Kate'},
    {'id': 3, 'name': 'Joe'}
]

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = next((emp for emp in employees if emp['id'] == employee_id), None)
    if employee:
        return jsonify(employee)
    return jsonify({'message': 'Employee not found'}), 404

@app.route('/employees', methods=['POST'])
def create_employee():
    new_employee = request.get_json()
    new_employee['id'] = len(employees) + 1
    employees.append(new_employee)
    return jsonify(new_employee), 201

@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    updated_employee = request.get_json()
    for index, employee in enumerate(employees):
        if employee['id'] == employee_id:
            employees[index] = updated_employee
            updated_employee['id'] = employee_id
            return jsonify(updated_employee)
    return jsonify({'message': 'Employee not found'}), 404
    
@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    for index, employee in enumerate(employees):
        if employee['id'] == employee_id:
            del employees[index]
            return jsonify({'message': 'Employee deleted'})
    return jsonify({'message': 'Employee not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
