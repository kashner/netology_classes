class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.all_grades = []
        self.average = None
    
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

    def get_average(self):
        """Get average grade for home tasks"""
        for value in self.grades.values():
            self.all_grades += value
        if self.all_grades:
            self.average = sum(self.all_grades) / len(self.all_grades)
        else:
            self.average = 0
        return self.average
    
    def __eq__(self, student):
        """Compare with '==' operand"""
        self.get_average()
        if isinstance(student, Student):
            student.get_average()
        else:
            print(f"{student} не студент")
            return False
        return self.average == student.average
    
    def __ne__(self, student):
        """Compare with '!=' operand"""
        self.get_average()
        if isinstance(student, Student):
            student.get_average()
        else:
            print(f"{student} не студент")
            return False
        return not self.average.__eq__(student.average)
    
    def __gt__(self, student):
        """Compare with '>' operand"""
        self.get_average()
        if isinstance(student, Student):
            student.get_average()
        else:
            print(f"{student} не студент")
            return False
        return self.average > student.average
    
    def __ge__(self, student):
        """Compare with '>=' operand"""
        self.get_average()
        if isinstance(student, Student):
            student.get_average()
        else:
            print(f"{student} не студент")
            return False
        return self.average.__ge__(student.average)
    
    def __lt__(self, student):
        """Compare with '<' operand"""
        self.get_average()
        if isinstance(student, Student):
            student.get_average()
        else:
            print(f"{student} не студент")
            return False
        return not self.average.__ge__(student.average)
    
    def __le__(self, student):
        """Compare with '<=' operand"""
        self.get_average()
        if isinstance(student, Student):
            student.get_average()
        else:
            print(f"{student} не студент")
            return False
        return not self.average.__gt__(student.average)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.all_grades = []
        self.average = None

    def get_average(self):
        """Get average grade for lections"""
        for value in self.grades.values():
            self.all_grades += value
        if self.all_grades:
            self.average = sum(self.all_grades) / len(self.all_grades)
        else:
            self.average = 0
        return self.average

    def __str__(self):
        text_part_1 = f"Имя: {self.name}\nФамилия: {self.surname}\n"
        text_part_2 = f"Средняя оценка за лекции: {self.get_average()}"
        return text_part_1 + text_part_2
    
    def __eq__(self, lecturer):
        """Compare with '==' operand"""
        self.get_average()
        if isinstance(lecturer, Lecturer):
            lecturer.get_average()
        else:
            print(f"{lecturer} не лектор")
            return False
        return self.average == lecturer.average
    
    def __ne__(self, lecturer):
        """Compare with '!=' operand"""
        self.get_average()
        if isinstance(lecturer, Lecturer):
            lecturer.get_average()
        else:
            print(f"{lecturer} не лектор")
            return False
        return not self.average.__eq__(lecturer.average)
    
    def __gt__(self, lecturer):
        """Compare with '>' operand"""
        self.get_average()
        if isinstance(lecturer, Lecturer):
            lecturer.get_average()
        else:
            print(f"{lecturer} не лектор")
            return False
        return self.average > lecturer.average
    
    def __ge__(self, lecturer):
        """Compare with '>=' operand"""
        self.get_average()
        if isinstance(lecturer, Lecturer):
            lecturer.get_average()
        else:
            print(f"{lecturer} не лектор")
            return False
        return self.average.__ge__(lecturer.average)
    
    def __lt__(self, lecturer):
        """Compare with '<' operand"""
        self.get_average()
        if isinstance(lecturer, Lecturer):
            lecturer.get_average()
        else:
            print(f"{lecturer} не лектор")
            return False
        return not self.average.__ge__(lecturer.average)
    
    def __le__(self, lecturer):
        """Compare with '<=' operand"""
        self.get_average()
        if isinstance(lecturer, Lecturer):
            lecturer.get_average()
        else:
            print(f"{lecturer} не лектор")
            return False
        return not self.average.__gt__(lecturer.average)


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


def get_course_avg_st(studets_list, corse_names):
        """Get average grade for home tasks per course"""
        course_avg = {}
        for student in studets_list:
            if isinstance(student, Student):
                course_avg[student.surname] = {}
                for course in corse_names:
                    for crs, gr in student.grades.items():
                        if crs == course:
                            if gr:
                                avg = sum(gr) / len(gr)
                                course_avg[student.surname][course] = round(avg,2)
        return course_avg


def get_course_avg_lc(lecturers_list, corse_names):
        """Get average grade for lectures per course"""
        course_avg = {}
        for lecturer in lecturers_list:
            if isinstance(lecturer, Lecturer):
                course_avg[lecturer.surname] = {}
                for course in corse_names:
                    for crs, gr in lecturer.grades.items():
                        if crs == course:
                            if gr:
                                avg = sum(gr) / len(gr)
                                course_avg[lecturer.surname][course] = round(avg,2)
        return course_avg

 
student1 = Student('Andrea', 'Pirlo', 'male')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Alisha', 'Lemman', 'female')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Java']
student2.finished_courses += ['HTML', 'CSS']
 
reviewer1 = Reviewer('Alex', 'Sandro')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Java']

reviewer2 = Reviewer('Alex', 'Sandro')
reviewer2.courses_attached += ['Python']
reviewer2.courses_attached += ['Git']

lecturer1 = Lecturer('Nicky', 'Butt')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Java']

lecturer2 = Lecturer('Alessandro', 'Del Piero')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['Git']
 
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 8)

reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Java', 10)

reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student1, 'Git', 10)

reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 10)

student1.rate_hw(lecturer1, 'Python', 10)
student1.rate_hw(lecturer1, 'Python', 7)
student1.rate_hw(lecturer2, 'Python', 9)
student1.rate_hw(lecturer2, 'Git', 8)

student2.rate_hw(lecturer1, 'Python', 10)
student2.rate_hw(lecturer1, 'Java', 7)
student2.rate_hw(lecturer2, 'Python', 9)
student2.rate_hw(lecturer2, 'Python', 8)
 
# print(student1.grades)
# print(lecturer1.grades)
print(reviewer1)
print("--------------")
print(lecturer2)
print("--------------")
print(student2)
print("--------------")
print("--------------")

compare1 = "Оценки лучше" if student1 > student2 else "Оценки не лучше"
compare2 = "Оценки не хуже" if student1 >= student2 else "Оценки хуже"
compare3 = "Оценки равны" if student1 == student2 else "Оценки не равны"
compare4 = "Оценки не лучше" if student1 <= student2 else "Оценки лучше"
compare5 = "Оценки хуже" if student1 < student2 else "Оценки не хуже"
compare6 = "Оценки не равны" if student1 != student2 else "Оценки равны"
print(compare1)
print(compare2)
print(compare3)
print(compare4)
print(compare5)
print(compare6)
print("--------------")
print("--------------")

compare1 = "Оценки лучше" if lecturer1 > lecturer2 else "Оценки не лучше"
compare2 = "Оценки не хуже" if lecturer1 >= lecturer2 else "Оценки хуже"
compare3 = "Оценки равны" if lecturer1 == lecturer2 else "Оценки не равны"
compare4 = "Оценки не лучше" if lecturer1 <= lecturer2 else "Оценки лучше"
compare5 = "Оценки хуже" if lecturer1 < lecturer2 else "Оценки не хуже"
compare6 = "Оценки не равны" if lecturer1 != lecturer2 else "Оценки равны"
print(compare1)
print(compare2)
print(compare3)
print(compare4)
print(compare5)
print(compare6)
print("--------------")
print("--------------")

studets_list = [student1,student2,"student3"]
corse_names = ["Git","Java","Python"]
print(get_course_avg_st(studets_list, corse_names))
print("--------------")

lecturers_list = [lecturer1,lecturer2,"lecturer3"]
corse_names = ["Git","Java","Python"]
print(get_course_avg_lc(lecturers_list, corse_names))