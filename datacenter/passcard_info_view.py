from datacenter.models import Passcard, get_duration, get_storage_visits_personal, is_visit_long, format_duration
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    personal_visits = get_storage_visits_personal(passcode)
    this_passcard_visits = [
        {
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit, 60)
        }
        for visit in personal_visits
    ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
