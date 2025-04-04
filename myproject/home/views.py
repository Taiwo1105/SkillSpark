from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Enrollment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User


# ✅ Home Page
def home(request):
    return render(request, 'home/index.html')


# ✅ Register Page
def register(request):
    if request.method == "POST":
        username = request.POST.get('username', '')  # ✅ Returns '' if 'username' is missing
        email = request.POST['email']
        password = request.POST['password']

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        login(request, user)  # Log the user in automatically
        return redirect('courses')  # Redirect to courses page

    return render(request, 'home/register.html')


# ✅ Custom Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Check if the user has enrolled in any course
            enrolled_courses = Enrollment.objects.filter(user=user)
            if enrolled_courses.exists():
                return redirect('course_in_progress')  # Redirect to ongoing course
            else:
                return redirect('courses')  # Redirect to enroll page if no course enrolled

        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'home/login.html')

    return render(request, 'home/login.html')


# ✅ Logout View
def logout_user(request):
    logout(request)
    return redirect('login')  # Redirects to login page after logout


# ✅ Courses Page (Show available courses)
def courses(request):
    all_courses = Course.objects.all()  # Fetch all courses from the database
    return render(request, 'home/courses.html', {'courses': all_courses})


# ✅ Enroll in a Course
@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user = request.user

    # Check if already enrolled
    existing_enrollment = Enrollment.objects.filter(user=user, course=course).exists()
    if not existing_enrollment:
        Enrollment.objects.create(user=user, course=course)

    # Redirect to course detail page after enrollment
    return redirect(reverse('course_detail', args=[course_id]))  # ✅ Fix

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'home/course_detail.html', {'course': course})

# ✅ Redirect for Enrollment
def enroll_redirect(request, course_id):
    if course_id:
        return redirect(reverse('enroll_course', args=[course_id]))
    else:
        return redirect('courses')  # Redirect somewhere safe if ID is missing


# ✅ Dashboard Page (Shows enrolled courses)
@login_required
def dashboard(request):
    enrolled_courses = Enrollment.objects.filter(user=request.user)
    return render(request, 'home/dashboard.html', {'enrolled_courses': enrolled_courses})


# ✅ Forgot Password Page
def forgot_password(request):
    return render(request, 'home/forgot_password.html')


# ✅ Generate Certificate
@login_required
def generate_certificate(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id, user=request.user)

      # Ensure the course is completed
    if enrollment.progress < 100 or not enrollment.completed:
        return HttpResponse("You haven't completed this course yet.")
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificate_{enrollment.course.title}.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 750, f"Certificate of Completion")
    p.drawString(100, 700, f"This certifies that {request.user.username} has completed {enrollment.course.title}.")
    p.save()

    return response


# ✅ Custom Django Login Class (If using class-based views)
class CustomLoginView(LoginView):
    template_name = 'home/login.html'
    redirect_authenticated_user = True  # Redirect logged-in users
   
    def get_success_url(self):
        return reverse_lazy('courses')  # Redirects to courses page after login
