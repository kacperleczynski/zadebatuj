from django.contrib import admin
from ksm_app.models import Debatants, Judges, DebatantsBattle, PasswordJudges, Tournament, TournamentUsers, \
    TournamentGroup, TournamentJudges

# Register your models here.
admin.site.register(Debatants)
admin.site.register(Judges)
admin.site.register(DebatantsBattle)
admin.site.register(PasswordJudges)
admin.site.register(Tournament)
admin.site.register(TournamentUsers)
admin.site.register(TournamentGroup)
admin.site.register(TournamentJudges)
