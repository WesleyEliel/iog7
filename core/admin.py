from django.contrib import admin

# Register your models here.
from core.models import Surfer, PricingPlan, Counter, VideoProof, Match, EncryptedProof


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
    pass


@admin.register(EncryptedProof)
class EncryptedProofAdmin(admin.ModelAdmin):
    pass


"""list_display = ['user', 'ban', ]
list_filter = ('ban',)
search_fields = ('user__username', 'user__id',
'user__first_name', 'user__last_name')
"""
