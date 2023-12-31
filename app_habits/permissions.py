# Права доступа
# Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
# Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """ Проверки на создателя привычки """

    message = 'Для этого действия вам необходимо быть создателем объекта!'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
