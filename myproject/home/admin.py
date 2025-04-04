from django.contrib import admin
from .models import Course, CourseMaterial

class CourseMaterialInline(admin.TabularInline):
    model = CourseMaterial
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'duration', 'material')
    inlines = [CourseMaterialInline]  # Allows adding materials inside Course admin page

@admin.register(CourseMaterial)
class CourseMaterialAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'uploaded_at')


admin.site.register(Course, CourseAdmin)


