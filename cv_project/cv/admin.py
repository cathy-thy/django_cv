from django.contrib import admin
from .models import Skill, Education, Experience, Profile

admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Profile)