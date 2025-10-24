from django.contrib import admin
from .models import LearningJourney, AboutMe

# Register models so they appear in admin dashboard
admin.site.register(LearningJourney)
admin.site.register(AboutMe)

