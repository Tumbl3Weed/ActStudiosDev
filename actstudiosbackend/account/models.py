import email
from email.policy import default
import profile
from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.forms import BooleanField


class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, name, surname, password=None):
        if not email:
            raise ValueError("Users must have an email address.")
        if not username:
            raise ValueError("Users must have a username.")
        if not name:
            raise ValueError("Users must have a name.")
        if not surname:
            raise ValueError("Users must have a surname.")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,
            surname=surname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email=self.normalize_email(email),
                                username=username,
                                password=password,
                                name="super", surname="user")
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_profile_image_filepath(self):
    return f'profile_images/{str(self.pk)}/{"profile_image.png"}'


def get_default_profile_image():
    return "actstudiosbackend/defaultIcon.png"


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(unique=True, max_length=30)
    name = models.CharField(unique=True, max_length=30)
    surname = models.CharField(unique=True, max_length=30)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath,
                                      null=True, blank=True, default=get_default_profile_image)
    hide_email = models.BooleanField(default=False)

    # objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]  # 'name','surname']

    def __str__(self) -> str:
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True


class School(models.Model):
    name = models.CharField(unique=True, max_length=30)
    teachersAtSchool = models.ManyToManyField('Teacher')


class Teacher(models.Model):
    account = models.ForeignKey(Account, required=True)
    schoolsTeachingAt = models.ManyToManyField('School')
    studentsTeaching = models.ManyToManyField('Student')


class Note (models.Model):
    text = models.CharField(required=False, blank=True)
    date = models.DateTimeField(
        verbose_name="date attended", auto_now_add=True)


class Attendance (models.Model):
    date = models.DateTimeField(
        verbose_name="date attended", auto_now_add=True)
    present = models.BooleanField(default=False)
    note = models.CharField(required=False, blank=True)


class Student(models.Model):
    account = models.ForeignKey(Account, required=False, blank=True)
    teachers = models.ManyToManyField('Teacher')
    parents = models.ManyToManyField('Account')
    grade = models.CharField(required=True, max_length=8)
    age = models.IntegerField(required=False, blank=True)
    attendance = models.ManyToManyField('Attendance')
    notes = models.ForeignKey('Note', required=False, blank=True)
