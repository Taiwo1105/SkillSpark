from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views  # Import password reset views

from home.views import (
    home, courses, dashboard, register, forgot_password,
    CustomLoginView, logout_user, enroll_course, generate_certificate
)

urlpatterns = [
    path('', home, name='home'),
    path('courses/', courses, name='courses'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),  # Use custom login view
    path('logout/', logout_user, name='logout'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('enroll/<int:course_id>/', enroll_course, name='enroll_course'),
    path('certificate/<int:enrollment_id>/', generate_certificate, name='generate_certificate'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail')



]

# ✅ Append password reset URLs
urlpatterns += [
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# ✅ Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
