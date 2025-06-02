class EmployeeSalary:
    hourly_payment = 400  # Почасовая оплата

    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment

employee = EmployeeSalary(name="Ivan", rest_days=2)

employee_with_hours = EmployeeSalary.get_hours(employee.name, employee.hours, employee.rest_days, employee.email)
print(f"Часы работы: {employee_with_hours.hours}")

employee_with_email = EmployeeSalary.get_email(employee.name, employee.hours, employee.rest_days, employee.email)
print(f"Email: {employee_with_email.email}")

print(f"Заработная плата: {employee_with_hours.salary()}")