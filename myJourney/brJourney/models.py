from django.db import models

# Model 1: For your Learning Journey page
class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_started = models.DateField()
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


# Model 2: For your About Me page
class AboutMe(models.Model):
    name = models.CharField(max_length=50)
    programme = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    bio = models.TextField()
    goal = models.TextField(blank=True)

    def __str__(self):
        return self.name
