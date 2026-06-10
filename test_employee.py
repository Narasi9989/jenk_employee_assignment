from employee import Employee


def test_add_employee():
    emp = Employee(101, "Narasimha", 50000)

    assert (
        emp.add_employee()
        == "Employee Narasimha added successfully"
    )


def test_update_salary():
    emp = Employee(101, "Narasimha", 50000)

    emp.update_salary(60000)

    assert emp.salary == 60000


def test_display_employee():
    emp = Employee(101, "Narasimha", 50000)

    expected = {
        "employee_id": 101,
        "employee_name": "Narasimha",
        "salary": 50000
    }

    assert emp.display_employee() == expected
