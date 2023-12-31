from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from app_habits.models import Habit
from app_habits.paginators import HabitPaginator
from app_habits.permissions import IsOwner
from app_habits.serializers import HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    """ Контроллер просмотра всех привычек """

    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class PublicHabitListAPIView(generics.ListAPIView):
    """ Контроллер просмотра публичных привычек """

    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitCreateAPIView(generics.CreateAPIView):
    """ Контроллер создания привычки """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер просмотра привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер редактирования привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер удаления привычки """

    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
