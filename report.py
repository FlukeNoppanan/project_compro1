

class ReportClass:

    def __init__(self):
        self.students = []
        self.teachers = []

    def load_data(self):
        from student import StudentClass
        from teacher import TeacherClass
        with open('student.bin', 'rb') as file:
            data = file.read()
        while data:
            student = StudentClass(0, '', 0, '', 0)
            student.unpack(data[:92])
            self.students.append(student)
            data = data[92:]
        with open('teacher.bin', 'rb') as file:
            data = file.read()
        while data:
            teacher = TeacherClass(0, '')
            teacher.unpack(data[:63])
            self.teachers.append(teacher)
            data = data[63:]
    
    def report_teacher(self):
        report_text = ''
        report_text += 'The teacher has students:\n'
        for teacher in self.teachers:
            count = 0
            for student in self.students:
                if student.teacher_id == teacher.teacher_id:
                    count += 1
            report_text += f'\t{teacher.name}: {count}\n'
        return report_text

    def report_year(self):
        report_text = ''
        years = {}
        for student in self.students:
            if student.year not in years:
                years[student.year] = 1
            else:
                years[student.year] += 1
        report_text += 'Number of students in each year:\n'
        for year in years:
            report_text += f'\tYear {year}: {years[year]}\n'
        return report_text

    def report_department(self):
        report_text = ''
        departments = {}
        for student in self.students:
            if student.department not in departments:
                departments[student.department] = 1
            else:
                departments[student.department] += 1
        report_text += 'Number of students in each department:\n'
        for department in departments:
            report_text += f'\t{department}: {departments[department]}\n'
        return report_text

    def report_total(self):
        return f'Total number of students:\t{len(self.students)}'

    def save_report(self):
        with open('report.txt', 'w') as file:
            self.load_data()
            file.write("Student Survey Report\n")
            file.write(self.report_teacher())
            file.write(self.report_year())
            file.write(self.report_department())
            file.write(self.report_total())
            print("Report saved to report.txt")
