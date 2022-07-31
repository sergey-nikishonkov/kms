from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_423_LOCKED
from .models import Master, Schedule, Hours
from .serializers import (
    MasterSerializer,
    ScheduleDetailSerializer,
    ScheduleListSerializer,
    ScheduleSerializer,
    HoursSerializer)
from .services import get_master_id, ScheduleFilter


class MasterDetailApi(RetrieveAPIView):
    """Get data about one master"""
    queryset = Master.objects.all()
    serializer_class = MasterSerializer


class MasterListApi(ListAPIView):
    """Get list of masters"""
    queryset = Master.objects.all()
    serializer_class = MasterSerializer


class ScheduleRetrieveApi(RetrieveAPIView):
    """Get one schedule"""
    queryset = Schedule.objects.all()
    serializer_class = ScheduleDetailSerializer


class ScheduleListApi(ListAPIView):
    """Get list of schedules"""
    queryset = Schedule.objects.all()
    serializer_class = ScheduleListSerializer
    filterset_class = ScheduleFilter


class ScheduleCreateApi(CreateAPIView):
    """Allow creating one or many instances of schedule model"""
    serializer_class = ScheduleSerializer

    def get_queryset(self) -> Schedule:

        master_id = get_master_id(self.request.data)
        return Schedule.objects.filter(master__id=master_id)

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
        return super().get_serializer(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        dates = [item.day.isoformat() for item in self.get_queryset()]
        if isinstance(request.data, list):
            for item in request.data:
                if item['day'] in dates:
                    request.data.remove(item)
        return super().create(request, *args, **kwargs)


class ScheduleDeleteApi(DestroyAPIView):
    """Delete one schedule instance"""
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()


class HoursCreateApi(CreateAPIView):
    """Allow creating one or many instances of hours model"""
    serializer_class = HoursSerializer

    def get_queryset(self):
        master_id = get_master_id(self.request.data)
        return Schedule.objects.filter(master__id=master_id)

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
        return super().get_serializer(*args, **kwargs)


class HoursDeleteApi(DestroyAPIView):
    """Delete one hour instance"""
    serializer_class = HoursSerializer
    queryset = Hours.objects.all()

    def destroy(self, request, *args, **kwargs):
        """Don`t allow delete hour if it`s booked"""
        instance = self.get_object()
        if instance.booked or instance.appointment_id:
            return Response(data='This hour is booked', status=HTTP_423_LOCKED)
        return super().destroy(request, *args, **kwargs)
