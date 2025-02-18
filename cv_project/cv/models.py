from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100, unique=True)
    linkedin = models.URLField(blank=True, null=True, unique=True)
    github = models.URLField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    level = models.IntegerField()

    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=200, unique=True)  
    institution = models.CharField(max_length=200)
    dates = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    dates = models.CharField(max_length=50)
    responsibilities = models.TextField()

    class Meta:
        unique_together = ('role', 'company', 'dates') 

    def get_responsibilities(self):
        return self.responsibilities.split("\n")

class Certification(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name