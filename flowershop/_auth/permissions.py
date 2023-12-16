from rest_framework.permissions import IsAuthenticated
from _auth.constants import USER_ROLE_ADMIN,USER_ROLE_MANAGER, USER_ROLE_CUSTOMER

class ManagerPermission(IsAuthenticated):
    message = "Только мэнеджеры могут выполнить это действие"
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == USER_ROLE_MANAGER

class AdminPermission(IsAuthenticated):
    message = "Только администраторы могут выполнить это действие"

    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == USER_ROLE_ADMIN

class CustomerPermission(IsAuthenticated):
    message = "Только зарегистрированные покупатели сайта могут выполнить это действие"
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == USER_ROLE_CUSTOMER