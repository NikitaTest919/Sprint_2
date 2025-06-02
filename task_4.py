class EmployeeSalary:
    hourly_payment = 400  # Почасовая оплата

    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, hours, rest_days):
        if hours is None:
            hours = (7 - rest_days) * 8
        return hours

    @classmethod
    def get_email(cls, name, email):
        if email is None:
            email = f"{name}@email.com"
        return email

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        actual_hours = self.get_hours(self.hours, self.rest_days)
        return actual_hours * self.hourly_payment


employee = EmployeeSalary(name="Ivan", rest_days=2)

print(f"Часы работы: {EmployeeSalary.get_hours(employee.hours, employee.rest_days)}")
print(f"Email: {EmployeeSalary.get_email(employee.name, employee.email)}")
print(f"Заработная плата: {employee.salary()}")