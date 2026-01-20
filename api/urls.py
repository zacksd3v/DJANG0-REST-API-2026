from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employes', views.EmployeeViewSet, basename='employees')

# urlpatterns = router.urls # ANOTHER METHOD TO DISPLAY DATA THROUGH URLS

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailsView),

#     # class Views
#     # path('employes/', views.Employees.as_view()),
#     # path('employes/<int:pk>/', views.EmployeeDetails.as_view())

    # if u gonna use router formula should be like:
    path('', include(router.urls)),
    # OR
    # urlpatterns = router.urls

    # for Blog path
    path('blogs/', views.BlogViews.as_view()),
    path('comments/', views.CommentViews.as_view()),

    # Retrieving using primary Key
    path('blogs/<int:pk>', views.BlogDetails.as_view()),
    path('comments/<int:pk>', views.CommentsDetails.as_view())
]