from django.db import models

# Model representing a user's profile
class Profile(models.Model):
    name = models.CharField(max_length=100, unique=True)
    linkedin = models.URLField(blank=True, null=True, unique=True)
    github = models.URLField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

# Model representing a skill
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    level = models.IntegerField()

    def __str__(self):
        return self.name

# Model representing an education entry
class Education(models.Model):
    degree = models.CharField(max_length=200, unique=True)  
    institution = models.CharField(max_length=200)
    dates = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

# Model representing a work experience entry
class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    dates = models.CharField(max_length=50)
    responsibilities = models.TextField()

    class Meta:
        unique_together = ('role', 'company', 'dates') 

    def get_responsibilities(self):
        return self.responsibilities.split("\n")

# Model representing a certificate entry
class Certification(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Model representing a project entry
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name