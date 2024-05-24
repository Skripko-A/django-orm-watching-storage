from datacenter.models import Passcard, Visit, get_duration, is_visit_long, format_duration
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    person = get_object_or_404(Passcard, passcode=passcode)
    person_storage_visits = Visit.objects.filter(passcard=person)
    this_passcard_visits = [
        {
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit, 60)
        }
        for visit in person_storage_visits
    ]
    context = {
        'passcard': person,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
