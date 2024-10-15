
from enum_1 import YEARS, DEPARTMENTS
class MenuClass:

    def add_data(self):
        from student import StudentClass
        from teacher import TeacherClass
        print('1. Add new student')
        print('2. Add new teacher')
        choice = input('Enter your choice: ')
        if choice == '1':
            all_teacher = TeacherClass.get_all_teacher()
            if len(all_teacher) == 0:
                print('There is no teacher. Please add teacher first')
                return
            try:
                student_id = int(input('Enter student id: '))
                name = input('Enter student name: ')
                print('All year:'+ f"{YEARS}")
                year = int(input('Enter student year: '))
                print('All department:'+ f"{DEPARTMENTS}")
                department = input('Enter student department: ')
                print('All teacher:')
                for teacher in range(len(all_teacher)):
                    print(f'{teacher + 1}. {all_teacher[teacher].name}')
                teacher_number = int(input('Enter teacher number: '))
            except ValueError:
                print('Invalid input')
                return
            if teacher_number < 1 or teacher_number > len(all_teacher):
                print('Invalid teacher number')
                return
            teacher_id = all_teacher[teacher_number - 1].teacher_id
            student = StudentClass(student_id, name, year, department, teacher_id)
            print("..Adding student..")
            student.add_student()

        elif choice == '2':
            try:
                teacher_id = int(input('Enter teacher id: '))
                name = input('Enter teacher name: ')
            except ValueError:
                print('Invalid input')
                return
            teacher = TeacherClass(teacher_id, name)
            print("..Adding teacher..")
            teacher.add_teacher()
        else:
            print('Invalid choice')

    def show_data(self):
        from student import StudentClass
        from teacher import TeacherClass
        students = StudentClass.get_all_student()
        if len(students) == 0:
            print('There is no student')
        else:
            print('--Student data--')
            for student in students:
                print("No.", students.index(student) + 1)
                print(f'\t ID: {student.student_id}\n\t Name: {student.name}\n\t Year: {student.year}\n\t Department: {student.department}\n\t Teacher ID: {student.teacher_id}')
                print('\t'+ '_'*30)
        teachers = TeacherClass.get_all_teacher()
        if len(teachers) == 0:
            print('There is no teacher')
        else:
            print('--Teacher data--')
            for teacher in teachers:
                print("No.", teachers.index(teacher) + 1)
                print(f'\t ID: {teacher.teacher_id}\n\t Name: {teacher.name}')
                print('\t'+ '_'*30)

    def get_specific_data(self):
        from student import StudentClass
        from teacher import TeacherClass
        print('1. Get student')
        print('2. Get teacher')
        choice = input('Enter your choice: ')
        print('-----------------')
        if choice == '1':
            print('1. Get student by id')
            print('2. Get student by name')
            print('3. Get student by year')
            print('4. Get student by department')
            print('5. Get student by teacher id')
            choice = input('Enter your choice: ')
            if choice == '1':
                try:
                    student_id = int(input('Enter student id: '))
                except ValueError:
                    print('Invalid input')
                    return
                student = StudentClass.get_student_by_id(student_id)
                if student:
                    print("Student found:")
                    print(f'\t ID: {student.student_id}\n\t Name: {student.name}\n\t Year: {student.year}\n\t Department: {student.department}\n\t Teacher ID: {student.teacher_id}')
                else:
                    print('Student not found')
            elif choice == '2':
                try:
                    student_name = input('Enter student name: ')
                except:
                    print('Invalid input')
                    return
                student = StudentClass.get_student_by_name(student_name)
                if student:
                    print("Student found:")
                    print(f'\t ID: {student.student_id}\n\t Name: {student.name}\n\t Year: {student.year}\n\t Department: {student.department}\n\t Teacher ID: {student.teacher_id}')
                else:
                    print('Student not found')
            elif choice == '3':
                print("All year:"+ f"{YEARS}")
                try:
                    student_year = int(input('Enter student year: '))
                except:
                    print('Invalid input')
                    return
                students = StudentClass.get_student_by_year(student_year)
                if students:
                    for student in students:
                        print("students found:")
                        print(f'\t ID: {student.student_id}\n\t Name: {student.name}\n\t Year: {student.year}\n\t Department: {student.department}\n\t Teacher ID: {student.teacher_id}')
                else:
                    print('Student not found')
            elif choice == '4':
                print("All department:"+ f"{DEPARTMENTS}")
                try:
                    student_department = input('Enter student department: ')
                except:
                    print('Invalid input')
                    return
                students = StudentClass.get_student_by_department(student_department)
                if students:
                    for student in students:
                        print("students found:")
                        print(f'\t ID: {student.student_id}\n\t Name: {student.name}\n\t Year: {student.year}\n\t Department: {student.department}\n\t Teacher ID: {student.teacher_id}')
                else:
                    print('Student not found')
            elif choice == '5':
                all_teacher = TeacherClass.get_all_teacher()
                print('All teacher:')
                for teacher in range(len(all_teacher)):
                    print(f'{teacher + 1}. {all_teacher[teacher].name}')
                try:
                    teacher_number = int(input('Enter teacher number: '))
                except:
                    print('Invalid input')
                    return
                if teacher_number < 1 or teacher_number > len(all_teacher):
                    print('Invalid teacher number')
                    return
                teacher_id = all_teacher[teacher_number - 1].teacher_id
                students = StudentClass.get_student_by_teacher_id(teacher_id)
                if students:
                    for student in students:
                        print("students found:")
                        print(f'\t ID: {student.student_id}\n\t Name: {student.name}\n\t Year: {student.year}\n\t Department: {student.department}\n\t Teacher ID: {student.teacher_id}')
                else:
                    print('Student not found')
            else:
                print('Invalid choice')
        elif choice == '2':
            print('1. Get teacher by id')
            print('2. Get teacher by name')
            choice = input('Enter your choice: ')
            if choice == '1':
                try:
                    teacher_id = int(input('Enter teacher id: '))
                except ValueError:
                    print('Invalid input')
                    return
                teacher = TeacherClass.get_teacher_by_id(teacher_id)
                if teacher:
                    print("Teacher found:")
                    print(f'\t ID: {teacher.teacher_id}\n\t Name: {teacher.name}')
                else:
                    print('Teacher not found')
            elif choice == '2':
                try:
                    teacher_name = input('Enter teacher name: ')
                except:
                    print('Invalid input')
                    return
                teacher = TeacherClass.get_teacher_by_name(teacher_name)
                if teacher:
                    print("Teacher found:")
                    print(f'\t ID: {teacher.teacher_id}\n\t Name: {teacher.name}')
                else:
                    print('Teacher not found')
            else:
                print('Invalid choice')
        else:
            print('Invalid choice')


    def update_data(self):
        from student import StudentClass
        from teacher import TeacherClass
        print('1. Update student')
        print('2. Update teacher')
        choice = input('Enter your choice: ')
        print('-----------------')
        if choice == '1':
            students = StudentClass.get_all_student()
            if len(students) == 0:
                print('There is no student')
                return
            try:
                for student in range(len(students)):
                    print(f'{student + 1}. {students[student].name}')
                student_number = int(input('Enter student number: '))
                if student_number < 1 or student_number > len(students):
                    print('Invalid student number')
                    return
                student_id = students[student_number - 1].student_id
                student = StudentClass.get_student_by_id(student_id)
                print("Note: If you skip a field, it will not be updated")
                name = input('Enter student name: ')
                if name:
                    student.name = name
                print('All year:'+ f"{YEARS}")
                year = input('Enter student year: ')
                if year:
                    student.year = int(year)
                print('All department:'+ f"{DEPARTMENTS}")
                department = input('Enter student department: ')
                if department:
                    student.department = department
                all_teacher = TeacherClass.get_all_teacher()
                print('All teacher:')
                for teacher in range(len(all_teacher)):
                    print(f'{teacher + 1}. {all_teacher[teacher].name}')
                teacher_number = input('Enter teacher number: ')
                if teacher_number:
                    if teacher_number and int(teacher_number) < 1 or int(teacher_number) > len(all_teacher):
                        print('Invalid teacher number')
                        return
                    teacher_id = all_teacher[int(teacher_number) - 1].teacher_id
                    student.teacher_id = teacher_id
                print("..Updating student..")
                student.update_student()
            except ValueError:
                print('Invalid input')
        elif choice == '2':
            teachers = TeacherClass.get_all_teacher()
            if len(teachers) == 0:
                print('There is no teacher')
                return
            try:
                for teacher in range(len(teachers)):
                    print(f'{teacher + 1}. {teachers[teacher].name}')
                teacher_number = int(input('Enter teacher number: '))
                if teacher_number < 1 or teacher_number > len(teachers):
                    print('Invalid teacher number')
                    return
                teacher_id = teachers[teacher_number - 1].teacher_id
                teacher = TeacherClass.get_teacher_by_id(teacher_id)
                print("Note: If you skip a field, it will not be updated")
                name = input('Enter teacher name: ')
                if name:
                    teacher.name = name
                print("..Updating teacher..")
                teacher.update_teacher()
            except ValueError:
                print('Invalid input')
        else:
            print('Invalid choice')

    def delete_data(self):
        from student import StudentClass
        from teacher import TeacherClass
        print('1. Delete student')
        print('2. Delete teacher')
        choice = input('Enter your choice: ')
        print('-----------------')
        try:
            if choice == '1':
                students = StudentClass.get_all_student()
                if len(students) == 0:
                    print('There is no student')
                    return
                else:
                    for student in range(len(students)):
                        print(f'{student + 1}. {students[student].name}')
                try:
                    student_number = int(input('Enter student number: '))
                except ValueError:
                    print('Invalid input')
                    return
                if student_number < 1 or student_number > len(students):
                    print('Invalid student number')
                    return
                student_id = students[student_number - 1].student_id
                student = StudentClass(0, '', 0, '', 0)
                student.remove_student(student_id)
            elif choice == '2':
                print("Note: If you delete a teacher, all students that this teacher has will be deleted")
                teachers = TeacherClass.get_all_teacher()
                if len(teachers) == 0:
                    print('There is no teacher')
                    return
                else:
                    for teacher in range(len(teachers)):
                        print(f'{teacher + 1}. {teachers[teacher].name}')
                try:
                    teacher_number = int(input('Enter teacher number: '))
                except ValueError:
                    print('Invalid input')
                    return
                if teacher_number < 1 or teacher_number > len(teachers):
                    print('Invalid teacher number')
                    return
                teacher_id = teachers[teacher_number - 1].teacher_id
                teacher = TeacherClass(0, '')
                teacher.remove_teacher(teacher_id)
            else:
                print('Invalid choice')
        except ValueError:
            print('Invalid input')

    def create_report(self):
        from report import ReportClass
        self.report = ReportClass()
        self.report.save_report()



