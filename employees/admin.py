from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Master, Schedule, Hours


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    """Representation master model in admin panel"""
    list_display = ('id', 'get_master_first_name', 'get_master_last_name', 'get_photo')
    list_display_links = ('get_master_first_name', )

    @admin.display(description='Имя мастера')
    def get_master_first_name(self, obj: Master) -> str | int:
        """Display first name"""
        if obj.user.first_name:
            return obj.user.first_name
        return obj.user

    @admin.display(description='Фамилия мастера')
    def get_master_last_name(self, obj: Master) -> str | int:
        """Display last name"""
        if obj.user.last_name:
            return obj.user.last_name
        return obj.user

    @admin.display(description='Фото')
    def get_photo(self, obj: Master) -> str:
        """Show master`s photo at admin panel"""
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        return 'No photo'


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """Representation schedule model in admin panel"""
    list_display = ('id', 'day', 'master', )
    list_display_links = ('day',)
    list_filter = ('master', )
    search_fields = ('day', )


@admin.register(Hours)
class HoursAdmin(admin.ModelAdmin):
    """Representation hour model in admin panel"""
    list_display = ('pk', 'hour', 'schedule', 'booked',)
    list_display_links = ('pk', 'hour', )
    list_filter = ('schedule', 'schedule__master')
