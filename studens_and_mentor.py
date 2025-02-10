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

 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

some_student = Student('Mike', 'Loui', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Java']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Nicky', 'Butt')
cool_lecturer.courses_attached += ['Python']

some_lecturer = Lecturer('Alessandro', 'Del Piero')
some_lecturer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(some_student, 'Python', 10)
cool_reviewer.rate_hw(some_student, 'Python', 9)
cool_reviewer.rate_hw(some_student, 'Python', 10)

best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 7)
best_student.rate_hw(cool_lecturer, 'Python', 9)

some_student.rate_hw(cool_lecturer, 'Python', 8)
some_student.rate_hw(cool_lecturer, 'Python', 7)

best_student.rate_hw(some_lecturer, 'Python', 10)
best_student.rate_hw(some_lecturer, 'Python', 7)
best_student.rate_hw(some_lecturer, 'Python', 9)

some_student.rate_hw(some_lecturer, 'Python', 8)
some_student.rate_hw(some_lecturer, 'Python', 7)
 
# print(best_student.grades)
# print(cool_lecturer.grades)
# print(cool_reviewer)
# print("--------------")
# print(cool_lecturer)
# print("--------------")
# print(some_student)
if best_student != some_student:
    print("Оценки не равны")
else:
    print("Оценки равны")

if best_student == some_student:
    print("Оценки равны")
else:
    print("Оценки не равны")

if best_student > some_student:
    print("Оценки больше")
else:
    print("Оценки не больше")

if best_student < some_student:
    print("Оценки меньше")
else:
    print("Оценки не меньше")