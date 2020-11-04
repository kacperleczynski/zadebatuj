import django_filters

from .models import *


class FullNameJudgesFilter(django_filters.FilterSet):
    class Meta:
        model = Judges
        fields = ('imię', 'nazwisko')


class FullNameDebatantsFilter(django_filters.FilterSet):
    class Meta:
        model = Debatants
        fields = ('imię', 'nazwisko')
