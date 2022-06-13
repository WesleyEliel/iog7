import random
import string

from django.core.handlers import exception
from django.db import models
from django.utils.translation import gettext as _


def id_generator(size=8, chars=string.digits):
    return "".join(random.choice(chars) for x in range(size))


class Surfer(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name=_("Ip address"), blank=True, null=True)
    telegram_link = models.URLField(verbose_name=_("Subscriber Telegram Account Link"), blank=True)
    is_banned = models.BooleanField(verbose_name=_("Is banned"), default=False)
    created = models.DateTimeField(verbose_name=_("Creation Date"), auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name=_("Last Update Date"), auto_now_add=False, auto_now=True)

    def __str__(self):
        return _(f'Surfer of address {self.get_ip_address()}')

    def get_ip_address(self):
        return f'{self.ip_address}'

    def ban_user(self):
        self.is_banned = True
        self.save()

    class Meta:
        verbose_name = _("Surfer")
        verbose_name_plural = _("Surfers")


class PricingPlan(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=20)
    price = models.DecimalField(verbose_name=_("Price"), decimal_places=2, max_digits=5)
    order = models.SmallIntegerField(verbose_name=_("Order"), null=False, blank=False, default=1)
    first_feature = models.CharField(verbose_name=_("First Feature"), blank=True, null=True, max_length=25)
    second_feature = models.CharField(verbose_name=_("Second Feature"), blank=True, null=True, max_length=25)
    third_feature = models.CharField(verbose_name=_("Third Feature"), blank=True, null=True, max_length=25)
    fourth_feature = models.CharField(verbose_name=_("Fourth Feature"), blank=True, null=True, max_length=25)
    created = models.DateTimeField(verbose_name=_("Creation Date"), auto_now_add=True, auto_now=False)
    is_active = models.BooleanField(verbose_name=_("Design if the plan is available"), default=True)
    is_big_plan = models.BooleanField(verbose_name=_("Design if the plan is Big"), default=False)
    updated = models.DateTimeField(verbose_name=_("Last Update Date"), auto_now_add=False, auto_now=True)

    def __str__(self):
        return _(f'{self.name} Pricing Plan [{self.price}]')

    class Meta:
        verbose_name = _("Pricing Plan")
        verbose_name_plural = _("Pricing Plans")
        ordering = ("order",)


class VideoProof(models.Model):
    resume = models.CharField(verbose_name=_("Resume"), max_length=220, blank=False)
    thumbnail = models.ImageField(verbose_name=_("Thumbnail"), blank=False, null=False)
    video = models.FileField(verbose_name=_("Te video file"), blank=True, null=True)
    link = models.URLField(verbose_name=_("Remote storage link"), blank=True, null=True)
    youtube_link = models.URLField(verbose_name=_("Youtube link"), blank=True, null=True)
    is_active = models.BooleanField(verbose_name=_("Design if the proof is available"), default=True)
    created = models.DateTimeField(verbose_name=_("Creation Date"), auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name=_("Last Update Date"), auto_now_add=False, auto_now=True)

    def __str__(self):
        return _(f'{self.resume}')

    def save(self, *args, **kwargs):
        if (self.link is None or self.link == "") and (
                self.youtube_link is None or self.youtube_link == "") and self.video is None:
            raise exception.BadRequest(_("One of the fields video, youtube_link and link must be provided"))

    class Meta:
        verbose_name = _("Video Proof")
        verbose_name_plural = _("Video Proofs")


class EncryptedProof(models.Model):
    date = models.DateField(verbose_name=_("Date"))
    encrypted_text = models.TextField(verbose_name=_("Encrypted text"))
    key = models.CharField(verbose_name=_("Key"), max_length=220, blank=True, null=True)
    display_key = models.BooleanField(verbose_name=_("Display the key"), default=True)
    is_active = models.BooleanField(verbose_name=_("Design if the proof is available"), default=True)
    created = models.DateTimeField(verbose_name=_("Creation Date"), auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name=_("Last Update Date"), auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{_("Match of")} { self.date}'

    class Meta:
        verbose_name = _("Encrypted Proof")
        verbose_name_plural = _("Encrypted Proofs")


ODD_CHOICES = (
    ('fixed', _("Fixed")),
    ('ht_ft', _("Half / Full Time")),
    ('full_time', _("Full Time")),
)


class Match(models.Model):
    date = models.DateField(verbose_name=_("Date du jeu"))
    odd = models.FloatField(verbose_name=_("Odds"), null=False, blank=False)
    odd_type = models.CharField(verbose_name=_("Odds type"), blank=False, max_length=220, choices=ODD_CHOICES)
    match_id = models.IntegerField(verbose_name=_("Match Id"), default=id_generator(), unique=True)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=7, decimal_places=2)
    is_active = models.BooleanField(verbose_name=_("Design if the Match is available"), default=True)
    created = models.DateTimeField(verbose_name=_("Creation Date"), auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name=_("Last Update Date"), auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'Match {self.match_id}, du {self.date}'

    @property
    def get_odd_type(self):
        for odd_choice in ODD_CHOICES:
            if odd_choice[0] == self.odd_type:
                return odd_choice[1]


    class Meta:
        verbose_name = _("Match")
        verbose_name_plural = _("Matches")


class Counter(models.Model):
    no_user = models.IntegerField(verbose_name=_("User number"))
    winning_matches = models.IntegerField(verbose_name=_("Winning matches"))
    people_love = models.IntegerField(verbose_name=_("People love"))
    is_active = models.BooleanField(verbose_name=_("Design if the Match is available"), default=True)
    created = models.DateTimeField(verbose_name=_("Creation Date"), auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name=_("Last Update Date"), auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'Counter [ User : ({self.no_user}) Winning Matches : ({self.winning_matches}) People Love : ({self.people_love})]'

    class Meta:
        verbose_name = _("Counter")
        verbose_name_plural = _("Counters")