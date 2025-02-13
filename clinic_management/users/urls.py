from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView,
    UserListView,
    ReceptionistDashboardView,
    NurseDashboardView,
    DoctorDashboardView,
    LaboratoristDashboardView,
    RegisterUserView,
    RegisterPatientView,
)

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/", UserListView.as_view(), name="user-list"),
    path("dashboard/receptionist/", ReceptionistDashboardView.as_view(), name="receptionist-dashboard"),
    path("dashboard/nurse/", NurseDashboardView.as_view(), name="nurse-dashboard"),
    path("dashboard/doctor/", DoctorDashboardView.as_view(), name="doctor-dashboard"),
    path("dashboard/laboratorist/", LaboratoristDashboardView.as_view(), name="laboratorist-dashboard"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("patients/register/", RegisterPatientView.as_view(), name="register-patient"),
    path("users/", UserListView.as_view(), name="user-list"),
]
