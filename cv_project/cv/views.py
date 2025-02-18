from django.shortcuts import render
from .models import Skill, Education, Experience, Profile, Certification, Project

# View function for displaying the CV
def cv_view(request):
    # Fetch the first profile
    profile = Profile.objects.first()
    # Fetch all skills
    skills = Skill.objects.all()
    # Fetch all education entries
    education = Education.objects.all()
    # Fetch all experience entries
    experience = Experience.objects.all()
    # Fetch all certifications
    certifications = Certification.objects.all()
    # Fetch all projects
    projects = Project.objects.all()

    # Render the CV template with the fetched data
    return render(request, 'cv_template.html', {
        'profile': profile,
        'skills': skills,
        'education': education,
        'experience': experience,
        'certifications': certifications,
        'projects': projects,
    })