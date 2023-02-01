import random
from datetime import datetime
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import generic

# Create your views here.
from core.models import VideoProof, PricingPlan, Counter, EncryptedProof, Match, PredictionHistory
from core.utils.utils import get_user_from_request


class HomeView(generic.View):
    def get(self, request, *args, **kwargs):
        light_pricing_plans = PricingPlan.objects.filter(
            is_big_plan=False).order_by('order')
        big_plan = PricingPlan.objects.get(is_big_plan=True)
        video_proofs_queryset = VideoProof.objects.filter(is_active=True)[:7]
        counter = Counter.objects.first()
        past_predictions = PredictionHistory.objects.filter(
            datetime__lt=datetime.now()).order_by('-datetime')
        fucture_predictions = PredictionHistory.objects.filter(
            datetime__gte=datetime.now()).order_by('datetime')
        next_matches = Match.objects.all().order_by('date')[:10]
        page_title = _("Home")

        context = {
            'video_proofs': video_proofs_queryset,
            'light_pricing_plans': light_pricing_plans,
            'big_plan': big_plan,
            'counter': counter,
            'page_title': page_title,
            'next_matches': next_matches,
            'past_predictions': past_predictions,
            'fucture_predictions': fucture_predictions,
        }
        return render(request=request, template_name='home/index.html', context=context)


class AboutView(generic.View):
    def get(self, request, *args, **kwargs):
        page_title = _("About")
        context = {
            'page_title': page_title
        }
        return render(request=request, template_name="marketing/about.html", context=context)


class TrustView(generic.View):
    def get(self, request, *args, **kwargs):
        current_encrypted_match = EncryptedProof.objects.filter(
            is_active=True, display_key=False)[0]
        previous_encrypted_matches = EncryptedProof.objects.filter(
            is_active=True, display_key=True).order_by('-date')
        page_title = _("Trust")
        context = {
            'page_title': page_title,
            'current_encrypted_match': current_encrypted_match,
            'previous_encrypted_matches': previous_encrypted_matches
        }
        return render(request=request, template_name="marketing/trust.html", context=context)


class VideosView(generic.DetailView):
    def get(self, request, *args, **kwargs):
        page_title = _("Visuals proofs")
        videos_proofs = VideoProof.objects.filter(is_active=True)
        context = locals()
        return render(request=request, template_name='home/videos.html', context=context)
