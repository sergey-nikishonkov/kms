from django_filters import FilterSet
from .models import Master, Schedule


def get_master_id(data: list | dict) -> int:
    """Return masters`s id from request data"""
    list_id = [item.id for item in Master.objects.all()]
    if isinstance(data, list):
        master_id = data[0]['master']
        if master_id in list_id:
            return master_id
    else:
        master_id = data['master']
        if master_id in list_id:
            return master_id


class ScheduleFilter(FilterSet):
    """Filtering schedules list"""
    class Meta:
        model = Schedule
        fields = {
            'day': ('lte', 'gte'),
        }
