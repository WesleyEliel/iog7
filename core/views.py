import random
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import generic

# Create your views here.
from core.models import VideoProof, PricingPlan, Counter, EncryptedProof, Match
from core.utils.utils import get_user_from_request


class HomeView(generic.View):
    def get(self, request, *args, **kwargs):
        light_pricing_plans = PricingPlan.objects.filter(is_big_plan=False).order_by('order')
        big_plan = PricingPlan.objects.get(is_big_plan=True)
        video_proofs_queryset = random.shuffle(VideoProof.objects.filter(is_active=True))
        counter = Counter.objects.first()
        next_matches = Match.objects.all().order_by('date')[:10]

        video_proofs = video_proofs_queryset[:10] if video_proofs_queryset is not None else []

        page_title = _("Home")

        context = {
            'video_proofs': video_proofs,
            'light_pricing_plans': light_pricing_plans,
            'big_plan': big_plan,
            'counter': counter,
            'page_title': page_title,
            'next_matches': next_matches
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
        current_encrypted_match = EncryptedProof.objects.filter(is_active=True, display_key=False)[0]
        previous_encrypted_matches = EncryptedProof.objects.filter(is_active=True, display_key=True)
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
        context = locals()
        return render(request=request, template_name='home/videos.html', context=context)
