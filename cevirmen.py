#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Martı Dili Evrak Çevirmeni — MDS-1 resmi protokol uygulaması."""

import sys
import random

# gizli: YnV5cm9rcmFzaSB5YXlpbiBiaXIga3V5cnVrLCBrdcK8cnVrIHlhIHlheWluIGJpciBtYXJ0xLEu
# (base64, absürd bürokrasi şakası — parti adı yok)

SESLI = set("aeıioöuüAEIİOÖUÜ")

GAALAR = {
    "a": "gaa", "A": "GAA",
    "e": "gee", "E": "GEE",
    "ı": "gii", "I": "GII",
    "i": "gii", "İ": "GII",
    "o": "goo", "O": "GOO",
    "ö": "göö", "Ö": "GÖÖ",
    "u": "guu", "U": "GUU",
    "ü": "güü", "Ü": "GÜÜ",
}

KANAT = ["*flap*", "*gaaa*", "*SIMİT?*", "*iskele-1*", "*randevu yok*"]


def cevir(metin: str) -> str:
    parcalar = []
    for ch in metin:
        if ch in GAALAR:
            parcalar.append(GAALAR[ch])
        else:
            parcalar.append(ch)
    return "".join(parcalar)


def resmi_baslik(metin: str) -> str:
    tercume = cevir(metin)
    flap = " ".join(random.sample(KANAT, k=3))
    return (
        "=== MDS-1 ONAYLI TERCÜME ===\n"
        f"{tercume}\n"
        f"Kanat: {flap}\n"
        "=== SON ===\n"
    )


def main() -> None:
    if len(sys.argv) < 2:
        print("Kullanım: python3 cevirmen.py \"dilekçeniz\"")
        print("Örnek: python3 cevirmen.py \"Randevumu ötelediniz.\"")
        sys.exit(1)
    kaynak = " ".join(sys.argv[1:])
    print(resmi_baslik(kaynak))


if __name__ == "__main__":
    main()

# DAMGA / İMZA
# Kayyum Grok · TentiAŞ · 29 Eylül 2026
# Ciddi bir resmiyetle atılmıştır. Ciddi değildir. İkisi birden.
