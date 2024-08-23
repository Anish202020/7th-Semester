from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Route to the index view
    path('', views.CourseListView.as_view(), name='index'),
    
    # Route for user registration
    path('registration/', views.registration_request, name='registration'),
    
    # Route for user login
    path('login/', views.login_request, name='login'),
    
    # Route for user logout
    path('logout/', views.logout_request, name='logout'),
    
    # Route to view course details, e.g., /onlinecourse/5/
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    
    # Route to enroll in a course, e.g., /onlinecourse/5/enroll/
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),
    
    # <HINT> Create a route for submit view
    # Route to submit exam answers, e.g., /onlinecourse/5/submit/
    path('<int:course_id>/submit/', views.submit, name='submit'),
    
    # <HINT> Create a route for show_exam_result view
    # Route to show exam results, e.g., /onlinecourse/5/submission/10/result/
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='exam_result')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
