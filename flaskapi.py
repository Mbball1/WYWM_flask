from flask import Flask, json
import data

print(data.employees)

companies = [
  {"id": 1, "name": "Company One"}, 
  {"id": 2, "name": "Company Two"}, 
  {"id": 3, "name": "Company Three"},
  {"id": 4, "name": "Company Four"},
  {"id": 5, "name": "Company Five"},
  {"id": 6, "name": "Company Six"},
  {"id": 7, "name": "Company Seven"},
  {"id": 8, "name": "Company Eight"},
  {"id": 9, "name": "Company Nine"},
]

api = Flask(__name__)

@api.route('/', methods=['GET'])
def show_home_message():
  message = ("This is the home page.")
  return json.dumps(message)

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)


@api.route('/companies/<int:idNumber>', methods=['GET'])
def get_specific_company(idNumber):
  """Will return the company if it matches idNumber"""
  id = idNumber
  for company in companies:
    if id == company["id"]:
      return json.dumps(company)

@api.route('/companies/employees/<int:company>', methods=['GET'])
def get_company_employees(company):
  """will return the employees who have the same number as the
  company"""
  companyNumber = company 
  for employee in data.employees:
    if companyNumber == employee["company"]:
        return json.dumps(employee)

@api.route('/employees', methods=['GET'])
def get_all_employees():
  return json.dumps(data.employees)

@api.route('/companies', methods=['POST'])
def post_companies():
  return json.dumps({"success": True}), 201 

@api.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
  """This will see if the data given matches that of an employee in the system. If it does
  it will replace the data and return XXXXXX else it will create a new entry and return XXXXX """
  employeeUpdate = {"id":id}
  # for employee in data.employees:
  #   if employeeUpdate == employee.id:
  #     employee = employeeUpdate
  #     return status.HTTP_204_NO_CONTENT
  #   else:
  #     data.employees.append(employeeUpdate)
  #     message = "Employee has been added."
  #     return message, status.HTPP_201_CREATED

if __name__ == '__main__':
    api.run()
