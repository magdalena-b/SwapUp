from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    subject_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    semester = models.IntegerField()
    path = models.CharField(max_length=30)
    mandatory = models.BooleanField()

    def __init__(self, subject_name, category, semester, path, mandatory, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subject_name = subject_name
        self.category = category
        self.semester = semester
        self.path = path
        self.mandatory = mandatory

    @property
    def subject_name(self):
        return self.subject_name

    @subject_name.setter
    def subject_name(self, name):
        self.subject_name = name

    @property
    def category(self):
        return self.category

    @category.setter
    def category(self, type):
        self.type = category

    @property
    def semester(self):
        return self.semester

    @semester.setter
    def semester(self, semester):
        self.semester = semester

    @property
    def path(self):
        return self.path

    @path.setter
    def path(self, path):
        self.path = path

    @property
    def mandatory(self):
        return self.mandatory

    @mandatory.setter
    def mandatory(self, mandatory):
        self.mandatory = mandatory


class Teacher(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)

    def __init__(self, first_name, last_name, title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.first_name = first_name
        self.last_name = last_name
        self.title = title

    @property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, name):
        self.first_name = name

    @property
    def last_name(self):
        return self.last_name

    @last_name.setter
    def last_name(self, name):
        self.last_name = name

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, title):
        self.title = title


class Class(models.Model):

    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day = models.DateField()
    time = models.TimeField()
    row = models.CharField(max_length=20)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __init__(self, day, time, row, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.day = day
        self.row = row
        self.time = time

    @property
    def day(self):
        return self.day

    @day.setter
    def day(self, day):
        self.day = day

    @property
    def time(self):
        return self.time

    @time.setter
    def time(self, time):
        self.time = time

    @property
    def row(self):
        return self.row

    @row.setter
    def row(self, row):
        self.row = row

    @property
    def subject_id(self):
        return self.subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        self.subject_id = subject_id


class Student(models.Model):
    index_number = models.IntegerField()
    semester = models.IntegerField()
    list_of_additional_subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)    # tutaj nie jestem pewien czy normalne settery
    list_of_classes = models.ForeignKey(Class, on_delete=models.CASCADE)                  # będą działały więc póki co zostawiam bez
    path = models.CharField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __init__(self, first_name, last_name, index_number, year, role, mail, path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.index_number = index_number
        self.role = role
        self.mail = mail
        self.path = path

    @property
    def index_number(self):
        return self.index_number

    @index_number.setter
    def index_number(self, number):
        self.index_number = number

    @property
    def semester(self):
        return self.semester

    @semester.setter
    def semester(self, semester):
        self.semester = semester

    @property
    def path(self):
        return self.path

    @path.setter
    def path(self, path):
        self.path = path


class Offer(models.Model):

    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    preferred_class_id_list = None
    additional_information = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    other_student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    other_offer_id = models.IntegerField()

    def __init__(self, info, state, other_student_id, other_exchange_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.additional_information = info
        self.state = state
        self.other_exchange_id = other_exchange_id
        self.other_student_id = other_student_id

    @property
    def additional_information(self):
        return self.additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        self.additional_information = additional_information

    @property
    def state(self):
        return self.state

    @state.setter
    def state(self, state):
        self.state = state

    @property
    def other_student_id(self):
        return self.other_student_id

    @other_student_id.setter
    def other_student_id(self, other_student_id):
        self.other_student_id = other_student_id

    @property
    def other_exchange_id(self):
        return self.other_exchange_id

    @other_exchange_id.setter
    def other_exchange_id(self, other_exchange_id):
        self.other_exchange_id = other_exchange_id

    @property
    def preferred_class_id_list(self):
        return self.preferred_class_id_list

    @preferred_class_id_list.setter
    def preferred_class_id_list(self,preferred_class_id_list):
        self.preferred_class_id_list=preferred_class_id_list

    @property
    def class_id(self):
        return self.class_id

    @class_id.setter
    def class_id(self, class_id):
        self.class_id=class_id
