from rest_framework.permissions import BasePermission,SAFE_METHODS
from .models import Product,Review

class ProductPermission (BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff

class ReviewPermission (BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.created_by.request.user