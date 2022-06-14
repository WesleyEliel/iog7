# -*- coding: utf-8 -*-

import json

from core.models import EncryptedProof, Match

encrypted_data = json.load(open('encrypted-data.json', encoding='utf-8'), )
matches_data = json.load(open('matches-data.json', encoding='utf-8'), )


def populate_encrypted_matches():
    for encrypted_prof in encrypted_data:
        print(encrypted_prof)
        EncryptedProof.objects.create(**encrypted_prof)


def populate_matches():
    for match in matches_data:
        print(match)
        Match.objects.create(**match)


populate_encrypted_matches()

"""exec(open('populate.py').read())"""
