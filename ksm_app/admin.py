from django.contrib import admin
from ksm_app.models import Debatants, Judges, DebatantsBattle, PasswordJudges
# Register your models here.
admin.site.register(Debatants)
admin.site.register(Judges)
admin.site.register(DebatantsBattle)
admin.site.register(PasswordJudges)
