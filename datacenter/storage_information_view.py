from django.conf import settings

from datacenter.models import Passcard
from datacenter.models import Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = [
        {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': f'{format_duration(get_duration(visit))}',
            'is_strange': is_visit_long(visit, 60)
        } for visit in visits
    ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
