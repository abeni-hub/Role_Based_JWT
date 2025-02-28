from rest_framework.permissions import BasePermission

class IsReceptionist(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "receptionist"

class IsNurse(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "nurse"

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "doctor"

class IsLaboratorist(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "laboratorist"
