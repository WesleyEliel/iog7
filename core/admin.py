from django.contrib import admin
import datetime

# Register your models here.
from core.models import Surfer, PricingPlan, Counter, VideoProof, Match, EncryptedProof

@admin.action(description='Incrémenter d\'une journée')
def increment(modeladmin, request, queryset):
    for element in queryset:
        element.date = element.date + datetime.timedelta(days=1)
        element.match_id += 1
        element.save()

@admin.register(Surfer)
class SurferAdmin(admin.ModelAdmin):
    pass


@admin.register(VideoProof)
class VideoProofAdmin(admin.ModelAdmin):
    pass


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    pass


@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    pass


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    actions = [increment]


@admin.register(EncryptedProof)
class EncryptedProofAdmin(admin.ModelAdmin):
    pass


"""list_display = ['user', 'ban', ]
list_filter = ('ban',)
search_fields = ('user__username', 'user__id',
'user__first_name', 'user__last_name')
"""
