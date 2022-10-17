from threading import Thread
from pyscope import pyscope as gs
import grade_calculator
from getpass import getpass
import os
import hashlib

from pyscope.account import GSAccount, GSCourse

if __name__ == "__main__":
    # get credentials
    email = input("Enter your email: ")
    pwd = getpass("Enter your password: ")
    # log in
    connection = gs.GSConnection()
    connection.login(email, pwd)
    account = connection.account

    name = input("Enter your name as it is on Gradescope: ")
    cs_course = GSCourse("415267", name, "CPCSi 220", "Fall 2022", account.session)
    cs_course.get_assignments_grades()
    grades = cs_course.assignments_grades
    gc = grade_calculator.GradeCalculator(grades)
    gc.calculate_subscores()

    print()
    print("Current subscores:")
    for i in gc.sub_scores:
        print(i, " : ", gc.sub_scores[i])
    print()
    print("Current grade is: ", gc.grade_for_class())

    print("For 93 in class you need", gc.needed_final_for(93), " on a final exam")
