from django.db import models


# Create your models here
class course(models.Model):
    course_name = models.CharField(max_length=148, blank=False)
    descrition = models.TextField(max_length=1100, blank=True)
    # student = models.ForeignKey(student, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class student(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    sur_name = models.CharField(max_length=200, blank=False)
    Date_of_Birth = models.DateField()
    picture = models.ImageField(upload_to="images/")
    course = models.ForeignKey(course, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.first_name


class result(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE, blank=False)
    score = models.PositiveIntegerField(max_length=100, blank=False)
    grade = models.CharField(max_length=2, blank=False)

    def __str__(self):
        return self.student.first_name