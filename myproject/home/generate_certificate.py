from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Course, Enrollment

def generate_certificate(request, course_id):
    enrollment = Enrollment.objects.get(user=request.user, course_id=course_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{enrollment.course.title}_certificate.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 24)
    p.drawString(100, 750, "Skill Spark Certificate of Completion")
    
    p.setFont("Helvetica", 16)
    p.drawString(100, 700, f"Presented to: {request.user.get_full_name()}")
    p.drawString(100, 670, f"For successfully completing the course: {enrollment.course.title}")

    p.showPage()
    p.save()
    return response
