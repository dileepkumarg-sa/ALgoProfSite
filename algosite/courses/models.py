from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=255, blank=True)
    instructor = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    level = models.CharField(max_length=50, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
