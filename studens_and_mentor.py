class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and \
            course in self.courses_in_progress and \
            course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        self.all_grades = []
        for value in self.grades.values():
            self.all_grades += value
        if self.all_grades:
            average = sum(self.all_grades) / len(self.all_grades)
        else:
            average = 0
        text_part_1 = f"Имя: {self.name}\nФамилия: {self.surname}\n"
        text_part_2 = f"Средняя оценка за домашние задания: {average}\n"
        text_part_3 = f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
        text_part_4 = f"Завершенные курсы: {', '.join(self.finished_courses)}"
        return text_part_1 + text_part_2 + text_part_3 + text_part_4
        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        self.all_grades = []
        for value in self.grades.values():
            self.all_grades += value
        if self.all_grades:
            average = sum(self.all_grades) / len(self.all_grades)
        else:
            average = 0
        text_part_1 = f"Имя: {self.name}\nФамилия: {self.surname}\n"
        text_part_2 = f"Средняя оценка за лекции: {average}"
        return text_part_1 + text_part_2


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and \
            course in self.courses_attached and \
            course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

some_student = Student('Mike', 'Loui', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Java']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 7)
best_student.rate_hw(cool_lecturer, 'Python', 9)

some_student.rate_hw(cool_lecturer, 'Python', 8)
some_student.rate_hw(cool_lecturer, 'Python', 7)
 
# print(best_student.grades)
# print(cool_lecturer.grades)
print(cool_reviewer)
print("--------------")
print(cool_lecturer)
print("--------------")
print(some_student)