from datetime import time
from django.db import models
from custom_auth.models import CustomUser


class Master(models.Model):
    """Model describes employee"""
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь')
    birthday = models.DateField(verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='photo', verbose_name='Фото')

    def __str__(self):
        return f'Мастер {self.user.first_name}'

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class Schedule(models.Model):
    """Model describes master`s schedule: add work-days ad days-off"""
    master = models.ForeignKey(
        Master,
        on_delete=models.PROTECT,
        verbose_name='Мастер',
        related_name='schedule')
    day = models.DateField(verbose_name='Рабочий день')

    def __str__(self):
        return f'{self.day} '

    class Meta:
        ordering = ['day']
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
        unique_together = ('master', 'day', )


class Hours(models.Model):
    """Model describe work-hours"""
    CHOICES = (
        (time.fromisoformat('10:00'), '10:00'), (time.fromisoformat('10:30'), '10:30'),
        (time.fromisoformat('11:00'), '11:00'), (time.fromisoformat('11:30'), '11:30'),
        (time.fromisoformat('12:00'), '12:00'), (time.fromisoformat('12:30'), '12:30'),
        (time.fromisoformat('13:00'), '13:00'), (time.fromisoformat('13:30'), '13:30'),
        (time.fromisoformat('14:00'), '14:00'), (time.fromisoformat('14:30'), '14:30'),
        (time.fromisoformat('15:00'), '15:00'), (time.fromisoformat('15:30'), '15:30'),
        (time.fromisoformat('16:00'), '16:00'), (time.fromisoformat('16:30'), '16:30'),
        (time.fromisoformat('17:00'), '17:00'), (time.fromisoformat('17:30'), '17:30'),
        (time.fromisoformat('18:00'), '18:00'), (time.fromisoformat('18:30'), '18:30'),
        (time.fromisoformat('19:00'), '19:00'), (time.fromisoformat('19:30'), '19:30'),
        (time.fromisoformat('20:00'), '20:00'), (time.fromisoformat('20:30'), '20:30'),
        (time.fromisoformat('21:00'), '21:00')
    )

    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        verbose_name='Рабочий день',
        related_name='hours')
    hour = models.TimeField(choices=CHOICES, verbose_name='Час')
    booked = models.BooleanField(default=False, verbose_name='Зарезервирован')
    appointment_id = models.IntegerField(
        unique=True,
        verbose_name='ID записи',
        blank=True,
        null=True)

    def __str__(self):
        return f'{self.hour} часов'

    class Meta:
        verbose_name = 'Рабочий час'
        verbose_name_plural = 'Рабочие часы'
        unique_together = ('schedule', 'hour')
