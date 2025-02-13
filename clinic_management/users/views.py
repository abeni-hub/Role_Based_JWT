from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsReceptionist, IsNurse, IsDoctor, IsLaboratorist
from rest_framework import generics ,permissions ,serializers
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegisterUserSerializer
from .models import Patient
from .serializers import PatientSerializer
from rest_framework import status

User = get_user_model()

# Custom JWT Login View
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# List all users (Admin only)
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Allow only authenticated users

class UserListView(generics.ListAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        role = self.request.query_params.get("role")
        if role:
            return User.objects.filter(role=role)
        return User.objects.all()
class ReceptionistListView(generics.ListAPIView):
    queryset = User.objects.filter(role="receptionist")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class DoctorListView(generics.ListAPIView):
    queryset = User.objects.filter(role="doctor")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class NurseListView(generics.ListAPIView):
    queryset = User.objects.filter(role="nurse")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class LaboratoristListView(generics.ListAPIView):
    queryset = User.objects.filter(role="laboratorist")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ReceptionistDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsReceptionist]

    def get(self, request):
        return Response({"message": "Welcome, Receptionist!"})

# Nurse-only view
class NurseDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsNurse]

    def get(self, request):
        return Response({"message": "Welcome, Nurse!"})

# Doctor-only view
class DoctorDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor]

    def get(self, request):
        return Response({"message": "Welcome, Doctor!"})

# Laboratorist-only view
class LaboratoristDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsLaboratorist]

    def get(self, request):
        return Response({"message": "Welcome, Laboratorist!"})
    

class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny] 

    def perform_create(self, serializer):
       serializer.save()

class RegisterPatientView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]  # ✅ Requires login

    def perform_create(self, serializer):
        if self.request.user.role != "receptionist":
            return Response({"error": "Only receptionists can register patients."}, status=status.HTTP_403_FORBIDDEN)
        serializer.save(registered_by=self.request.user)     

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Patient
from .serializers import PatientSerializer

@api_view(["POST"])
@permission_classes([IsAuthenticated])  # Ensure only logged-in users can register patients
def register_patient(request):
    if request.user.role != "receptionist":
        return Response({"error": "Only receptionists can register patients."}, status=403)

    data = request.data.copy()
    data["registered_by"] = request.user.id  # Assign logged-in receptionist

    serializer = PatientSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
