from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # القراءة مسموحة للجميع
        if request.method in ['GET']:
            return True

        # التعديل والحذف فقط لصاحب الريفيو
        return obj.user == request.use