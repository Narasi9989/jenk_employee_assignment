class Employee:
    def __init__(self, employee_id, employee_name, salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.salary = salary

    def add_employee(self):
        return (
            f"Employee {self.employee_name} "
            f"added successfully"
        )

    def update_salary(self, new_salary):
        self.salary = new_salary
        return self.salary

    def display_employee(self):
        return {
            "employee_id": self.employee_id,
            "employee_name": self.employee_name,
            "salary": self.salary
        }
