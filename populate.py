# -*- coding: utf-8 -*-

import json

from core.models import EncryptedProof, Match, PricingPlan, Counter

pricing_plan_data = json.load(
    open('data/pricing-plans-data.json', encoding='utf-8'), )
encrypted_data = json.load(
    open('data/encrypted-data.json', encoding='utf-8'), )
matches_data = json.load(open('data/matches-data.json', encoding='utf-8'), )


def populate_encrypted_matches():
    for encrypted_prof in encrypted_data:
        print("\n")
        print(encrypted_prof['fields'])
        try:
            EncryptedProof.objects.create(**encrypted_prof['fields'])
            print("PASS \n")
        except Exception as exc:
            print(exc)


def populate_matches():
    for match in matches_data:
        print(match['fields'])
        Match.objects.create(**match['fields'])


def populate_pricing_plan():
    for plan in pricing_plan_data:
        print(plan['fields'])
        PricingPlan.objects.create(**plan['fields'])


def populate_counter():
    Counter.objects.create(
        no_user=9432, winning_matches=15512,  people_love=9345)


populate_matches()
populate_counter()
populate_pricing_plan()
populate_encrypted_matches()

"""exec(open('populate.py').read())"""
