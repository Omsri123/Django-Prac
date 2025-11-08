from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeeData)

urlpatterns = [
    path('students/',views.studentsView),
    path('students/<int:pk>/',views.studentDetailView),

    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:pk>/',views.EmployeeData.as_view()),

#   employees urls
    path('',include(router.urls)),

    path('blogs/', views.BlogData.as_view()),
    path('comments/',views.CommentData.as_view()),
    path('blogs/<int:pk>/',views.BlogDetails.as_view()),
    path('comments/<int:pk>/',views.CommentDetails.as_view())

]