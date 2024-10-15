import struct
import os

class TeacherClass:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name

    def pack(self):
        return struct.pack('13s50s', str(self.teacher_id).encode(), self.name.encode())
    
    def unpack(self, data):
        unpacked = struct.unpack('13s50s', data)
        self.teacher_id = int(unpacked[0].decode().strip('\x00'))
        self.name = unpacked[1].decode().strip('\x00')

    def validation(self, is_update=False):
        messages = []
        if len(self.name) > 50:
            messages.append('Teacher name must be less than 50 characters')
        if self.teacher_id < 0:
            messages.append('Teacher ID must be greater than 0')
        with open('teacher.bin', 'rb') as file:
            data = file.read()
        if is_update:
            return True
        while data:
            if len(data) < 63:
                print("File is corrupted")
                break
            teacher = TeacherClass(0, '')
            teacher.unpack(data[:63])
            if teacher.teacher_id == self.teacher_id:
                messages.append('Teacher ID existed')
            if teacher.name == self.name:
                messages.append('Teacher name existed')
            data = data[63:]
        if messages:
            print('\n'.join(messages))
            return False
        return True
    
    def add_teacher(self):
        if not self.validation():
            return False
        if os.path.exists('teacher.bin'):
            with open('teacher.bin', 'ab') as file:
                file.write(self.pack())
        else:
            with open('teacher.bin', 'wb') as file:
                file.write(self.pack())
        print('-----------------Add teacher successfully-----------------')
        return True
    
    def remove_teacher(self, teacher_id):
        with open('teacher.bin', 'rb') as file:
            data = file.read()
        if not data:
            print('There is no teacher')
            return True
        with open('teacher.bin', 'wb') as file:
            while data:
                if len(data) < 63:
                    print("File is corrupted")
                    break
                teacher = TeacherClass(0, '')
                teacher.unpack(data[:63])
                if teacher.teacher_id != teacher_id:
                    file.write(data[:63])
                data = data[63:]
        # remove student that has teacher_id
        with open('student.bin', 'rb') as file:
            data = file.read()
        if not data:
            return True
        with open('student.bin', 'wb') as file:
            while data:
                if len(data) < 92:
                    print("File is corrupted")
                    break
                from student import StudentClass
                student = StudentClass(0, '', 0, '', 0)
                student.unpack(data[:92])
                if student.teacher_id != teacher_id:
                    file.write(data[:92])
                data = data[92:]
        print('-----------------Remove teacher successfully-----------------')
        return True
    
    def update_teacher(self):
        if not self.validation(is_update=True):
            return False
        with open('teacher.bin', 'rb') as file:
            data = file.read()
        if not data:
            print('There is no teacher')
            return False
        with open('teacher.bin', 'wb') as file:
            while data:
                if len(data) < 63:
                    print("File is corrupted")
                    break
                teacher = TeacherClass(0, '')
                teacher.unpack(data[:63])
                if teacher.teacher_id != self.teacher_id:
                    file.write(data[:63])
                else:
                    file.write(self.pack())
                data = data[63:]
        print('-----------------Update teacher successfully-----------------')
        return True
    
    @staticmethod
    def get_teacher_by_id(teacher_id):
        with open('teacher.bin', 'rb') as file:
            data = file.read()
        if not data:
            return None
        while data:
            if len(data) < 63:
                print("File is corrupted")
                break
            teacher = TeacherClass(0, '')
            teacher.unpack(data[:63])
            if teacher.teacher_id == teacher_id:
                return teacher
            data = data[63:]
        return None
    
    @staticmethod
    def get_teacher_by_name(name):
        with open('teacher.bin', 'rb') as file:
            data = file.read()
        if not data:
            return None
        while data:
            if len(data) < 63:
                print("File is corrupted")
                break
            teacher = TeacherClass(0, '')
            teacher.unpack(data[:63])
            if teacher.name.lower() == name.lower():
                return teacher
            data = data[63:]
        return None

    @staticmethod
    def get_all_teacher():
        teachers = []
        with open('teacher.bin', 'rb') as file:
            data = file.read()
        if not data:
            return teachers
        while data:
            if len(data) < 63:
                print("File is corrupted")
                break
            teacher = TeacherClass(0, '')
            teacher.unpack(data[:63])
            teachers.append(teacher)
            data = data[63:]
        return teachers
