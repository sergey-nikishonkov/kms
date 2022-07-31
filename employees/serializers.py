from rest_framework import serializers
from custom_auth.models import CustomUser
from .models import Master, Schedule,  Hours


class CustomUserSerializer(serializers.ModelSerializer):
    """Serializer user model"""
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', ]


class MasterSerializer(serializers.ModelSerializer):
    """Serializer master model"""
    user = CustomUserSerializer()

    class Meta:
        model = Master
        fields = ['id', 'birthday', 'photo', 'user']


class HoursListSerializer(serializers.ModelSerializer):
    """Serializer list of hours models"""
    class Meta:
        model = Hours
        fields = ('schedule', 'hour', 'appointment_id')


class ScheduleDetailSerializer(serializers.ModelSerializer):
    """Serializer schedule model"""
    hours = serializers.StringRelatedField(many=True)

    class Meta:
        model = Schedule
        fields = ('master', 'day', 'hours')


class ScheduleListSerializer(serializers.ModelSerializer):
    """Serializer list of schedule models"""
    class Meta:
        model = Schedule
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    """Serializer schedule model"""
    class Meta:
        model = Schedule
        fields = '__all__'


class HoursSerializer(serializers.ModelSerializer):
    """Serializer hour model"""
    class Meta:
        model = Hours
        fields = '__all__'
