# -*- coding: utf-8 -*-
import random
import random
import time
from datetime import datetime
from workers.models import Worker, MARITAL_STATUS, WorkerLocation, WorkerChild, JobPosition
from department.models import Department, DepartmentJobPosition
from education.models import WorkerSecondaryEducation, WorkerHighEducation
from honors.models import Salary, Prize, Achievement


def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%d.%m.%Y', prop)
#
# wb = Workbook()
#
# ws = wb.active
#
# ws['A1'] = "Фамилия"
# ws['B1'] = "Имя"
# ws['C1'] = "Отчество"
# ws['D1'] = "Пол"
# ws['E1'] = "Дата рождения"
# ws['F1'] = "Должность"
# ws['G1'] = "Оклад"
# ws["H1"] = "Семейное положение"
# ws["I1"] = "Количество детей"
#
# last_names = open("last_name.txt", "rb").read().decode('UTF-8').split('\n')
# m_names = open("imena_m.txt", "rb").read().decode('UTF-8').split("\n")
# w_names = open("imena_g.txt", "rb").read().decode('UTF-8').split("\n")
#
# for i in range(80):
#     last_name = random.choice(last_names)
#     if last_name[-2] != "А":
#         name = random.choice(m_names)
#         while len(name) < 2:
#             name = random.choice(m_names)
#         patron = random.choice(m_names) + "ович"
#         sex = "м"
#         marital_status = random.choice(["холост", "женат", "разведен", "вдовец", ])
#     else:
#         name = random.choice(w_names)
#         while len(name) < 2:
#             name = random.choice(w_names)
#         patron = random.choice(m_names) + "овна"
#         sex = "ж"
#         marital_status = random.choice(["замужем", "не замужем", "разведена", "вдова"])
#     ws["A%s" % (i+1)] = last_name.lower().capitalize()
#     ws["B%s" % (i+1)] = name.lower().capitalize()
#     ws["C%s" % (i+1)] = patron.lower().capitalize()
#     ws["D%s" % (i+1)]X = sex
#     ws["E%s" % (i+1)] = randomDate("1.1.1980", "1.1.1995", random.random())
#     ws["F%s" % (i+1)] = random.choice(["Менеджер по подбору персонала",
#                                        "Продавец", "Инженер", "Старший инженер", "Младший инженер"])
#     ws["G%s" % (i+1)] = random.randint(10000, 40000)
#     ws["H%s" % (i+1)] = marital_status
#     ws["I%s" % (i+1)] = random.randrange(0, 3)
#
# wb.save("generated.xlsx")


def generate_people(count=1000):
    last_names = open("generator/dict/last_name.txt", "rb").read().decode("utf8").split('\n')
    m_names = open("generator/dict/imena_m.txt", "rb").read().decode("utf8").split("\n")
    w_names = open("generator/dict/imena_g.txt", "rb").read().decode("utf8").split("\n")
    cities  = open("generator/dict/cities.txt", "rb").read().decode("utf8").split("\n")
    street  = open("generator/dict/streetlist.txt", "rb").read().decode("utf8").split("\n")
    orgs    = open("generator/dict/organizations.txt", "rb").read().decode("utf8").split("\n")
    j_pos   = open("generator/dict/jobpositions.txt", "rb").read().decode("utf8").split("\n")
    hschools= open("generator/dict/highschools.txt", "rb").read().decode("utf8").split("\n")
    for i in range(count):
        # add man
        man = Worker()
        man.username = "user%s" % i
        last_name = random.choice(last_names)
        if last_name[-2] != "А" or last_name[-2] != "Я":
            name = random.choice(m_names)
            while len(name) < 2:
                name = random.choice(m_names)
            patron = random.choice(m_names) + "ович"
            sex = True
        else:
            name = random.choice(w_names)
            while len(name) < 2:
                name = random.choice(w_names)
            patron = random.choice(m_names) + "овна"
            sex = False
        man.last_name = last_name.lower().capitalize()
        man.first_name = name.lower().capitalize()
        man.patronymic = patron.lower().capitalize()
        man.sex = sex
        man.marital_status = random.choice(MARITAL_STATUS)
        man.set_password("user")
        man.user_type = "Stuff"
        man.birth_place = random.choice(cities)
        year = random.randint(1950, 1995)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        birth_date = datetime(year, month, day)
        man.birthday = birth_date
        man.save()
        # add location
        location = WorkerLocation()
        location.worker = man
        location.city = "Москва"
        location.street = random.choice(street)
        location.house = random.randint(1, 500)
        location.flat = random.randint(1, 200)
        location.save()
        # add child =)
        if random.randint(1, 20) == 5:
            child_count = random.randint(1, 4)
            for chi in range(child_count):
                child = WorkerChild()
                child.worker = man
                year = random.randint(man.birthday.year+18, 2015)
                month = random.randint(1, 12)
                day = random.randint(1, 28)
                birth_date = datetime(year, month, day)
                child.birthday = birth_date
                if random.randint(0, 1):
                    child.sex = True
                    child.name = random.choice(m_names).lower().capitalize()
                else:
                    child.sex = False
                    child.name = random.choice(w_names).lower().capitalize()
                child.save()

        # add secondary edu for worker
        sec_edu = WorkerSecondaryEducation()
        sec_edu.worker = man
        sec_edu.name = random.choice(["Гимназия", "Лицей", "Школа"]) + (" %s" % random.randint(1, 100))
        sec_edu.from_date = datetime(man.birthday.year+7, 9, 1)
        sec_edu.to_date = datetime(man.birthday.year+18, 6, 30)
        sec_edu.graduation_year = man.birthday.year+18
        sec_edu.save()

        # add high edu
        high_edu = WorkerHighEducation()
        high_edu.worker = man
        high_edu.name = random.choice(hschools)
        high_edu.from_date = datetime(man.birthday.year+18, 9, 1)
        high_edu.to_date = datetime(man.birthday.year+23, 6, 30)
        high_edu.graduation_year = man.birthday.year+23
        high_edu.education_type = "Высшее"
        high_edu.specialization = random.choice([
            "Корпоративное управление", "ИБАС", "ПО", "ВТ", "Бухгалтерия", "История", "Маркетинг"
        ])
        high_edu.save()

        # add JobPosition
        # last_jobs

        year = man.birthday.year+18 + random.randint(0, 5)
        while True and year < 2013:
            if year > 2012:
                break
            year = random.randint(year, 2015)
            if year > 2012:
                break
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            from_date = datetime(year, month, day)
            year = random.randint(year+1, 2013)
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            to_date = datetime(year, month, day)
            j_position = JobPosition()
            j_position.worker = man
            j_position.organization = random.choice(orgs)
            j_position.position = random.choice(j_pos)
            j_position.from_date = from_date
            j_position.to_date = to_date
            j_position.save()
        year = 2013
        # current job in our company
        j_position = JobPosition()
        j_position.worker = man
        j_position.organization = "Random Ltd"
        departments = Department.objects.filter()
        j_position.department = random.choice(departments)
        j_position.position_id = random.choice(DepartmentJobPosition.objects.filter(department=j_position.department))
        j_position.position = random.choice(j_pos)
        year = random.randint(year+1, 2014)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        j_position.from_date = datetime(year, month, day)
        j_position.save()

        # add salary
        salary = Salary()
        salary.worker = man
        salary.salary = random.randint(50000, 250000)
        salary.destination_day = j_position.from_date
        salary.save()
