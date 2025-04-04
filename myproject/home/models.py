from django.db import models
from django.contrib.auth.models import User

# ✅ Course Model
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    material = models.FileField(upload_to='materials/', blank=True, null=True)  # Allow empty files # Upload course materials
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)


    def __str__(self):
        return self.title

class CourseMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="materials")
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='course_materials/')  # Uploads to MEDIA_ROOT/course_materials
    uploaded_at = models.DateTimeField(auto_now_add=True)



# ✅ Enrollment Model
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Preserve data if user is deleted
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Delete enrollments if course is deleted
    progress = models.FloatField(default=0.0)  # Store progress as a percentage
    enrolled_at = models.DateTimeField(auto_now_add=True)  # Track enrollment date
    completed = models.BooleanField(default=False)  # Add this field

    @property
    def is_completed(self):
        return self.progress >= 100.00  # Auto-check completion

    def __str__(self):
        return f"{self.user.username if self.user else 'Deleted User'} - {self.course.title}"
