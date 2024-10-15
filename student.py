import struct
import os
from enum_1 import YEARS, DEPARTMENTS

class StudentClass:
    def __init__(self, student_id, name, year, department, teacher_id):
        self.student_id = student_id
        self.name = name
        self.year = year
        self.department = department
        self.teacher_id = teacher_id

    def pack(self):
        return struct.pack('13s50s4s12s13s', str(self.student_id).encode(), self.name.encode(), str(self.year).encode(), self.department.encode(), str(self.teacher_id).encode())

    def unpack(self, data):
        unpacked = struct.unpack('13s50s4s12s13s', data)
        self.student_id = int(unpacked[0].decode().strip('\x00'))
        self.name = unpacked[1].decode().strip('\x00')
        self.year = int(unpacked[2].decode().strip('\x00'))
        self.department = unpacked[3].decode().strip('\x00')
        self.teacher_id = int(unpacked[4].decode().strip('\x00'))

    def validation(self, is_update=False):
        self.department = self.department.upper()
        messages = []
        from teacher import TeacherClass
        all_teacher = TeacherClass.get_all_teacher()
        if len(all_teacher) == 0:
            messages.append('There is no teacher(Student must have teacher)')
        else:
            teacher_ids = [teacher.teacher_id for teacher in all_teacher]
            if self.teacher_id not in teacher_ids:
                messages.append('Teacher ID not found')
        if len(self.name) > 50 or len(self.department) > 12:
            messages.append('Student name must be less than 50 characters and department must be less than 12 characters')
        if self.student_id < 0 or self.teacher_id < 0:
            messages.append('Student ID and teacher ID must be greater than 0')
        if self.year not in YEARS:
            messages.append('Invalid year')
        if self.department not in DEPARTMENTS:
            messages.append('Invalid department')
        if is_update == False:
            with open('student.bin', 'rb') as file:
                data = file.read()
            while data:
                if len(data) < 92:
                    print("File is corrupted")
                    break
                student = StudentClass(0, '', 0, '', 0)
                student.unpack(data[:92])
                if student.student_id == self.student_id:
                    messages.append('Student ID existed')
                if student.name == self.name:
                    messages.append('Student name existed')
                data = data[92:]
        if messages:
            print('\n'.join(messages))
            return False
        return True

    def add_student(self):
        if not self.validation():
            return False
        if os.path.exists('student.bin'):
            with open('student.bin', 'ab') as file:
                file.write(self.pack())
        else:
            with open('student.bin', 'wb') as file:
                file.write(self.pack())
        print('-----------------Add student successfully-----------------')
        return True
    
    def remove_student(self, student_id):
        with open('student.bin', 'rb') as file:
            data = file.read()
        if not data:
            print('There is no student')
            return True
        with open('student.bin', 'wb') as file:
            while data:
                if len(data) < 92:
                    print("File is corrupted")
                    break
                student = StudentClass(0, '', 0, '', 0)
                student.unpack(data[:92])
                if student.student_id != student_id:
                    file.write(data[:92])
                data = data[92:]
        print('-----------------Remove student successfully-----------------')
        return True
    
    def update_student(self):
        if not self.validation(is_update=True):
            return False
        with open('student.bin', 'rb') as file:
            data = file.read()
        if not data:
            print('There is no student')
            return False
        with open('student.bin', 'wb') as file:
            while data:
                if len(data) < 92:
                    print("File is corrupted")
                    break
                student = StudentClass(0, '', 0, '', 0)
                student.unpack(data[:92])
                if student.student_id != self.student_id:
                    file.write(data[:92])
                else:
                    file.write(self.pack())
                    print('-----------------Update student successfully-----------------')
                data = data[92:]
        return False
    
    @staticmethod
    def get_student_by_id(student_id):
        with open('student.bin', 'rb') as file:
            data = file.read()
        if not data:
            return None
        while data:
            if len(data) < 92:
                print("File is corrupted")
                break
            student = StudentClass(0, '', 0, '', 0)
            student.unpack(data[:92])
            if student.student_id == student_id:
                return student
            data = data[92:]
        return None
    
    @staticmethod
    def get_student_by_name(name):
        with open('student.bin', 'rb') as file:
            data = file.read()
        if not data:
            return None
        while data:
            if len(data) < 92:
                print("File is corrupted")
                break
            student = StudentClass(0, '', 0, '', 0)
            student.unpack(data[:92])
            if student.name.lower() == name.lower():
                return student
            data = data[92:]
        return None
    
    @staticmethod
    def get_student_by_year(year):
        students = []
        with open('student.bin', 'rb') as file:
            data = file.read()
        if not data:
            return students
        while data:
            if len(data) < 92:
                print("File is corrupted")
                break
            student = StudentClass(0, '', 0, '', 0)
            student.unpack(data[:92])
            if student.year == year:
                students.append(student)
            data = data[92:]
        return students
    
    @staticmethod
    def get_student_by_department(department):
        students = []
        with open('student.bin', 'rb') as file:
            data = file.read()
        if not data:
            return students
        while data:
            if len(data) < 92:
                print("File is corrupted")
                break
            student = StudentClass(0, '', 0, '', 0)
            student.unpack(data[:92])
            if student.department.lower() == department.lower():
                students.append(student)
            data = data[92:]
        return students
    
    @staticmethod
    def get_student_by_teacher_id(teacher_id):
        students = []
        with open('student.bin', 'rb') as file:
            data = file.read()
        if not data:
            return students
        while data:
            if len(data) < 92:
                print("File is corrupted")
                break
            student = StudentClass(0, '', 0, '', 0)
            student.unpack(data[:92])
            if student.teacher_id == teacher_id:
                students.append(student)
            data = data[92:]
        return students
    
    @staticmethod
    def get_all_student():
        students = []
        with open('student.bin', 'rb') as file:
            data = file.read()
        if not data:
            return students
        while data:
            if len(data) < 92:
                print("File is corrupted")
                break
            student = StudentClass(0, '', 0, '', 0)
            student.unpack(data[:92])
            students.append(student)
            data = data[92:]
        return students