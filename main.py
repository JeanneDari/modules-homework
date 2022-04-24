from Accounting.application.salary import calculate_salary
from Accounting.application.people import get_employees
from datetime import date

if __name__ == '__main__':
    calculate_salary()
    get_employees()


def get_cur_date():
    current_date = date.today()
    print(current_date)


get_cur_date()


