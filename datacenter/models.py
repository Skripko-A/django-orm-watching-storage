from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(visit):
    current_time = localtime().replace(microsecond=0)
    entered_time = visit.entered_at
    if visit.leaved_at:
        current_time = visit.leaved_at
    visit_duration = current_time - entered_time
    return visit_duration.seconds


def get_storage_visits_personal(passcode):
    person = Passcard.objects.get(passcode=passcode)
    person_storage_visits = Visit.objects.filter(passcard=person)
    return person_storage_visits


def is_visit_long(visit, suspicious_interval):
    if get_duration(visit) > suspicious_interval * 60:
        return 'Да'
    return 'Нет'


def format_duration(duration):
    hours = duration // 3600
    minutes = duration // 60 - hours * 60
    return f'{hours}ч, {minutes}м'
