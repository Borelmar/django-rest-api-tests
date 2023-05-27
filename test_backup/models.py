from django.db import models
from users.models import User

class Test(models.Model):
    # русскому языку, анализу информации, компьютерной грамотности.
    SUBJECTS_CHOICES = [
        ("russian_language", "русский язык"),
        ("information_analysis", "анализ информации"),
        ("computer_literacy", "компьютерная грамотность"),
    ]
    subject = models.CharField(max_length=128, null=False, blank=False, choices=SUBJECTS_CHOICES)
    name = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField()
    tasks_count = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)


class Task(models.Model):
    test = models.ForeignKey(to=Test, on_delete=models.DO_NOTHING, null=True)
    text = models.TextField()
    options_count = models.PositiveIntegerField(default=0)
    correct_option = models.ForeignKey(to=Test, on_delete=models.CASCADE, null=True)


class TaskOption(models.Model):
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE, related_name='options', null=True)
    text = models.TextField()
    #ordinal_num = models.PositiveIntegerField(default=0)


class UserTest(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, null=True)
    test = models.ForeignKey(to=Test, on_delete=models.DO_NOTHING, null=True)
    test_name = models.CharField(max_length=128, null=False, blank=False)
    correct_count = models.PositiveIntegerField(default=0)
    incorrect_count = models.PositiveIntegerField(default=0)

