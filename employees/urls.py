from django.urls import path
from .views import (
    MasterDetailApi,
    MasterListApi,
    ScheduleRetrieveApi,
    ScheduleListApi,
    ScheduleCreateApi,
    ScheduleDeleteApi,
    HoursCreateApi,
    HoursDeleteApi
)


urlpatterns = [
    path('master/<int:pk>/', MasterDetailApi.as_view(), name='master'),
    path('masters/', MasterListApi.as_view(), name='master_list'),
    path('schedule/<int:pk>/', ScheduleRetrieveApi.as_view(), name='schedule'),
    path('schedules/', ScheduleListApi.as_view(), name='schedules'),
    path('schedules/create/', ScheduleCreateApi.as_view(), name='schedule_create'),
    path('schedules/<int:pk>/delete/', ScheduleDeleteApi.as_view(), name='schedule_delete'),
    path('hour/create/', HoursCreateApi.as_view(), name='hour_create'),
    path('hour/<int:pk>/delete/', HoursDeleteApi.as_view(), name='hour_delete'),
]
