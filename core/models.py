from django.db import models


class University(models.Model):
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Speciality(models.Model):
    title = models.CharField(max_length=200)
    university = models.ManyToManyField(University)

    def __str__(self):
        return self.title


class Psychotype(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    speciality = models.ManyToManyField(Speciality)

    def __str__(self):
        return self.title


class Subject(models.Model):
    title = models.CharField(max_length=200)
    rate = models.CharField(max_length=200)
    speciality = models.ManyToManyField(Speciality)

    def __str__(self):
        return self.title
