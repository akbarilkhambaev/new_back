from django.urls import path
from . import api_views
from .api_jwt_email import EmailTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # JWT Auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/email/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair_email'),

    # Jobs
    path('jobs/', api_views.JobListCreateView.as_view(), name='api_job_list'),
    path('jobs/<int:pk>/', api_views.JobDetailView.as_view(), name='api_job_detail'),

    # Tasks
    path('tasks/', api_views.TaskListCreateView.as_view(), name='api_task_list'),
    path('tasks/<int:pk>/', api_views.TaskDetailView.as_view(), name='api_task_detail'),
    path('developer/tasks/', api_views.DeveloperTasksView.as_view(), name='api_developer_tasks'),

    # Dashboard
    path('dashboard/stats/', api_views.dashboard_stats, name='api_dashboard_stats'),
    path('dashboard/monthly-revenue/', api_views.monthly_revenue_chart, name='api_monthly_revenue'),
    path('dashboard/project-distribution/', api_views.project_status_distribution, name='api_project_distribution'),
    path('dashboard/recent-projects/', api_views.recent_projects, name='api_recent_projects'),
    path('dashboard/upcoming-deadlines/', api_views.upcoming_deadlines, name='api_upcoming_deadlines'),

    # Calendar
    path('calendar/tasks/', api_views.calendar_tasks, name='api_calendar_tasks'),
]
