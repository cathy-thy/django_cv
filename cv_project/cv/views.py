from django.shortcuts import render
from .models import Skill, Education, Experience, Profile, Certification, Project

def cv_view(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    certifications = Certification.objects.all()
    projects = Project.objects.all()

    return render(request, 'cv_template.html', {
        'profile': profile,
        'skills': skills,
        'education': education,
        'experience': experience,
        'certifications': certifications,
        'projects': projects,
    })