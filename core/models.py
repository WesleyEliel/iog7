import json
import random
import string

from django.core.handlers import exception
from django.db import models
from django.utils.text import slugify


def id_generator(size=8, chars=string.digits):
    return "".join(random.choice(chars) for x in range(size))


class Surfer(models.Model):
    ip_address = models.GenericIPAddressField(
        verbose_name="Adresse IP", blank=True, null=True)
    telegram_link = models.URLField(
        verbose_name="Compte Telegram de l'utilisateur", blank=True)
    is_banned = models.BooleanField(
        verbose_name="Designe si l'utilisateur est banni", default=False)
    created = models.DateTimeField(
        verbose_name="Date de création", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(
        verbose_name="Date de la dernière modification", auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'Abonné d\'adresse {self.get_ip_address()}'

    def get_ip_address(self):
        return f'{self.ip_address}'

    def ban_user(self):
        self.is_banned = True
        self.save()

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"


class PricingPlan(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=20)
    price = models.DecimalField(
        verbose_name="Prix", decimal_places=2, max_digits=5)
    order = models.SmallIntegerField(
        verbose_name="Ordre", null=False, blank=False, default=1)
    first_feature = models.CharField(
        verbose_name="1er Avantage", blank=True, null=True, max_length=255)
    second_feature = models.CharField(
        verbose_name="2em Avantage", blank=True, null=True, max_length=255)
    third_feature = models.CharField(
        verbose_name="3em Avantage", blank=True, null=True, max_length=255)
    fourth_feature = models.CharField(
        verbose_name="4em Avantage", blank=True, null=True, max_length=255)
    created = models.DateTimeField(
        verbose_name="Date de création", auto_now_add=True, auto_now=False)
    is_active = models.BooleanField(
        verbose_name="Designe si le plan est valable", default=True)
    is_big_plan = models.BooleanField(
        verbose_name="Design si le plan est 'Big'", default=False)
    updated = models.DateTimeField(
        verbose_name="Date de la dernière modification", auto_now_add=False, auto_now=True)

    def __str__(self):
        return f' Plan d\'abonnement {self.name} [{self.price}]'

    class Meta:
        verbose_name = "Plan d'abonnement"
        verbose_name_plural = "Plan d'abonnements"
        ordering = ("order",)


class TextProof(models.Model):
    resume = models.CharField(verbose_name="Resumé",
                              max_length=100, blank=False)
    content = models.TextField(verbose_name="Contenu", blank=False)
    firstname = models.CharField(
        max_length=20, verbose_name="Nom", blank=False)
    lastname = models.CharField(
        max_length=20, verbose_name="Prenoms", blank=False)
    avatar = models.ImageField(blank=True, verbose_name="Avatar")
    is_active = models.BooleanField(
        verbose_name="Designe si la preuve est valable", default=True)
    created = models.DateTimeField(
        verbose_name="Date de création", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(
        verbose_name="Date de la dernière modification", auto_now_add=False, auto_now=True)
    # objects = InheritanceManager()

    def __str__(self):
        return f'{self.resume}'

    # def get_child_type(self):
    #    return type(self.objects.get_buchild(id=self.id))

    class Meta:
        verbose_name = "Preuve textuelle"
        verbose_name_plural = "Preuves Textuelles"


class ImageProof(models.Model):
    firstname = models.CharField(
        max_length=20, verbose_name="Nom", blank=False)
    lastname = models.CharField(
        max_length=20, verbose_name="Prenoms", blank=False)
    resume = models.CharField(verbose_name="Resumé",
                              max_length=220, blank=False)
    image = models.ImageField(verbose_name="Image")
    avatar = models.ImageField(blank=True, verbose_name="Avatar")
    is_active = models.BooleanField(
        verbose_name="Designe si la preuve est valable", default=True)
    created = models.DateTimeField(
        verbose_name="Date de création", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(
        verbose_name="Date de la dernière modification", auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.resume}'

    class Meta:
        verbose_name = "Preuve Visuelle"
        verbose_name_plural = "Preuves Vissuelles"


class VideoProof(models.Model):
    resume = models.CharField(verbose_name="Resumé",
                              max_length=220, blank=False)
    thumbnail = models.ImageField(
        verbose_name="Thumbnail", blank=False, null=False)
    video = models.FileField(
        verbose_name="Fichier Vidéo", blank=False, null=False)
    is_active = models.BooleanField(
        verbose_name="Designe si la preuve est valable", default=True)
    created = models.DateTimeField(
        verbose_name="Date de création", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(
        verbose_name="Date de la dernière modification", auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.resume}'

    class Meta:
        verbose_name = "Preuve Video"
        verbose_name_plural = "Preuves Videos"


class EncryptedProof(models.Model):
    date = models.DateField(verbose_name="Date")
    encrypted_text = models.TextField(verbose_name="Encrypted text")
    key = models.CharField(
        verbose_name="Key", max_length=220, blank=True, null=True)
    display_key = models.BooleanField(
        verbose_name="Display the key", default=True)
    is_active = models.BooleanField(
        verbose_name="Design if the proof is available", default=True)
    created = models.DateTimeField(
        verbose_name="Date de création", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(
        verbose_name="Date de la dernière modification", auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{"Match of"} { self.date}'

    class Meta:
        verbose_name = "Encrypted Proof"
        verbose_name_plural = "Encrypted Proofs"


ODD_CHOICES = (
    ('fixed', "Fixed"),
    ('ht_ft', "Half / Full Time"),
    ('full_time', "Full Time"),
)


class Match(models.Model):
    date = models.DateField(verbose_name="Date de jeu")
    odd = models.FloatField(verbose_name="Côte", null=False, blank=False)
    odd_type = models.CharField(
        verbose_name="Type de Côte", blank=False, max_length=220, choices=ODD_CHOICES)
    match_id = models.IntegerField(
        verbose_name="Match Id", default=id_generator())
    price = models.DecimalField(
        verbose_name="Prix", max_digits=7, decimal_places=2)
    is_active = models.BooleanField(
        verbose_name="Designe si le match valable", default=True)
    created = models.DateTimeField(
        verbose_name="Date de création", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(
        verbose_name="Date de la dernière modification", auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'Match {self.match_id}, du {self.date}'

    @property
    def get_odd_type(self):
        for odd_choice in ODD_CHOICES:
            if odd_choice[0] == self.odd_type:
                return odd_choice[1]

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"


class PredictionHistory(models.Model):

    COMPETITIONS_CHOICES = tuple((slugify(element), element) for element in json.load(
        open('competitions-data.json', encoding='utf-8'), ))
    datetime = models.DateTimeField(verbose_name="Date et heure du jeu")
    competition = models.CharField(verbose_name="Competition", max_length=255)
    first_team = models.CharField(
        verbose_name="Première Equipe", max_length=25)
    second_team = models.CharField(
        verbose_name="Deuxième Equipe", max_length=25)
    first_team_goals_number = models.IntegerField(
        verbose_name="Nombre de Buts Première Equipe", default=0)
    second_team_goals_number = models.IntegerField(
        verbose_name="Nombre de Buts Deuxième Equipe", default=0)
    prediction = models.CharField(
        verbose_name="Prediction Suggérée", max_length=25)
    odd = models.FloatField(verbose_name="Côte", null=False, blank=False)
    is_success = models.BooleanField(
        verbose_name="Designe si la prédiction est un succès", default=True)
    created = models.DateTimeField(
        verbose_name="Date de création", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(
        verbose_name="Date de la dernière modification", auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'Predcition du {self.datetime} sur  {self.match_id}'

    class Meta:
        verbose_name = "Historique de Prediction"
        verbose_name_plural = "Historiques de Prédiction"


class Counter(models.Model):
    no_user = models.IntegerField(verbose_name="User number")
    winning_matches = models.IntegerField(verbose_name="Winning matches")
    people_love = models.IntegerField(verbose_name="People love")
    is_active = models.BooleanField(
        verbose_name="Design if the Match is available", default=True)
    created = models.DateTimeField(
        verbose_name="Date de création", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(
        verbose_name="Date de la dernière modification", auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'Counter [ User : ({self.no_user}) Winning Matches : ({self.winning_matches}) People Love : ({self.people_love})]'

    class Meta:
        verbose_name = "Counter"
        verbose_name_plural = "Counters"
