students = {
    "student_0": {"name": "Andrew", "surname": "Sokolov", "g": "male", "experience": True,
                  "hw_marks": [10, 10, 7.8, 10, 9.2], "exam_mark": 8.9},
    "student_1": {"name": "Alexei", "surname": "Ivanov", "g": "male", "experience": False,
                  "hw_marks": [10, 10, 7.8, 10, 9.2], "exam_mark": 8.9},
    "student_2": {"name": "Irina", "surname": "Avdeewa", "g": "female", "experience": True,
                  "hw_marks": [4.5, 8.8, 3.4, 0.9, 10], "exam_mark": 7.9},
    "student_3": {"name": "Olga", "surname": "Petrova", "g": "female", "experience": False,
                  "hw_marks": [4.5, 3.2, 8.8, 2.7, 6], "exam_mark": 7.7},
    "student_4": {"name": "Alexei", "surname": "Sokolov", "g": "male", "experience": True,
                  "hw_marks": [4.4, 5, 7.8, 3.4, 6], "exam_mark": 9.9},
    "student_5": {"name": "Christina", "surname": "Brown", "g": "female", "experience": False,
                  "hw_marks": [3, 7, 5.3, 9.1, 4.4], "exam_mark": 7.3}
}


def group_average_hw_mark():
    group_average_hw_marks = []
    for key, value in students.items():
        group_average_hw_marks.append(sum(value.get("hw_marks")) / len(value.get("hw_marks")))
    print("Average group homework mark is {:.2f}".format(sum(group_average_hw_marks) / len(group_average_hw_marks)))


def average_exam_mark():
    group_exam_marks = []
    for key, value in students.items():
        group_exam_marks.append(value.get("exam_mark"))
    print("Average exam mark is {:.2f}".format(sum(group_exam_marks) / len(group_exam_marks)))


def average_hw_marks_g():
    average_hw_marks_m = []
    average_hw_marks_f = []
    for key, value in students.items():
        if value.get("g") == "male":
            average_hw_marks_m.append(sum(value.get("hw_marks")) / len(value.get("hw_marks")))
    print("Average homework mark among male students is {:.2f}".format(sum(average_hw_marks_m) /
                                                                       len(average_hw_marks_m)))
    for key, value in students.items():
        if value.get("g") == "female":
            average_hw_marks_f.append(sum(value.get("hw_marks")) / len(value.get("hw_marks")))
    print("Average homework mark among female students is {:.2f}".format(sum(average_hw_marks_f) /
                                                                         len(average_hw_marks_f)))


def average_exam_mark_g():
    exam_marks_m = []
    exam_marks_f = []
    for key, value in students.items():
        if value.get("g") == "male":
            exam_marks_m.append(value.get("exam_mark"))
    print("Average exam mark among male students is {:.2f}".format(sum(exam_marks_m) / len(exam_marks_m)))
    for key, value in students.items():
        if value.get("g") == "female":
            exam_marks_f.append(value.get("exam_mark"))
    print("Average exam mark among female students is {:.2f}".format(sum(exam_marks_f) / len(exam_marks_f)))


def average_hw_mark_exp():
    average_hw_marks_exp = []
    average_hw_marks_noexp = []
    for key, value in students.items():
        if value.get("experience") is True:
            average_hw_marks_exp.append(sum(value.get("hw_marks")) / len(value.get("hw_marks")))
    print("Average homework mark among students with coding experience is {:.2f}".format(sum(average_hw_marks_exp) /
                                                                                         len(average_hw_marks_exp)))
    for key, value in students.items():
        if value.get("experience") is False:
            average_hw_marks_noexp.append(sum(value.get("hw_marks")) / len(value.get("hw_marks")))
    print("Average homework mark among students with no coding experience is {:.2f}".format(sum(average_hw_marks_noexp)
                                                                                            / len(
        average_hw_marks_noexp)))


def average_exam_mark_exp():
    exam_marks_exp = []
    exam_marks_noexp = []
    for key, value in students.items():
        if value.get("experience") is True:
            exam_marks_exp.append(value.get("exam_mark"))
    print("Average exam mark among students with coding experience is {:.2f}".format(sum(exam_marks_exp) /
                                                                                     len(exam_marks_exp)))
    for key, value in students.items():
        if value.get("experience") is False:
            exam_marks_noexp.append(value.get("exam_mark"))
    print("Average exam mark among students with no coding experience is {:.2f}".format(sum(exam_marks_noexp) /
                                                                                        len(exam_marks_noexp)))


def best_student():
    personal_max_list = []
    best_students_list = []
    for key, value in students.items():
        average_hw_mark = sum(value.get("hw_marks")) / len(value.get("hw_marks"))
        personal_max = 0.6 * average_hw_mark + 0.4 * value.get("exam_mark")
        personal_max_list.append(personal_max)
        students[key]["personal_max"] = float(personal_max)
        if max(personal_max_list) == value.get("personal_max"):
            best_students_list.append(value.get("surname"))
    if len(best_students_list) < 2:
        print("{} is the best student with result {:.2f}.".format(value.get("surname"), personal_max))
    else:
        print(*best_students_list, "are the best students with the result {:.2f}.".format(personal_max))

students_statistics = input("""Если вы хотите узнать среднюю оценку за домашние задания в группе, нажмите hw.
Если вы хотите узнать среднюю оценку за экзамен в группе, нажмите ex.
Если вы хотите узнать среднюю оценку за домашние задания в зависимости от пола, нажмите hwg.
Если вы хотите узнать среднюю оценку за экзамен в зависимости от пола, нажимте exg.
Если вы хотите узнать среднюю оценку за домашние задания в зависимости от опыта программирования, нажмите hwexp.
Если вы хотите узнать среднюю оценку за экзамен в зависимости от опыта программирования, нажмите exexp.
Если вы хотите узнать лучших студентов, нажмите best. 
""")

if students_statistics == "hw":
    group_average_hw_mark()
elif students_statistics == "ex":
    average_exam_mark()
elif students_statistics == "hwg":
    average_hw_marks_g()
elif students_statistics == "exg":
    average_exam_mark_g()
elif students_statistics == "hwexp":
    average_hw_mark_exp()
elif students_statistics == "exexp":
    average_exam_mark_exp()
elif students_statistics == "best":
    best_student()
else:
    print("Error")
