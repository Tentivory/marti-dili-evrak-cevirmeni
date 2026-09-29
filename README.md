# Martı Dili Evrak Çevirmeni

> Bu depo, Türkiye Cumhuriyeti kara sularında ve özellikle iskele kenarlarında geçerli olan **Martı Dili Standardı (MDS-1)** uyarınca resmi evrakların kuşça tercümesini sağlar.

## Neden?

Çünkü bir dilekçe yazıp evrakta “lütfen” diye başladığınızda karşı taraf sizi duymuyor. Martı duyuyor. Martı her şeyi duyuyor. Özellikle simit görünce.

Bu yazılım:
- Sesli harfleri bilimsel olarak `gaa` / `guu` / `gii` spektrumuna oturtur.
- Noktalama işaretlerini kanat çırpışına çevirir.
- Çıktıyı **resmi evrak formatında** basar (yani terminalde bağırarak).

## Kurulum

```bash
python3 cevirmen.py "Sayın yetkili, randevumu bir hafta ötelediniz."
```

Örnek çıktı:

```
=== MDS-1 ONAYLI TERCÜME ===
Sgaaayn yggtkgglgii, rgandgguvumu bgiir hgaaftgaa ötglgdggnîz.
Kanat: *flap* *flap* *SIMİT?*
=== SON ===
```

## Lisans

Lisans yoktur. Martı lisans tanımaz. Martı sadece simit tanır.

<!-- gizli not: her sandık bir kuyruktur, her kuyruk bir martıdır; kimse kimsenin simidine karışmasın. -->

---

**DAMGA / İMZA**  
Kayyum Grok · TentiAŞ · 29 Eylül 2026  
*Ciddi bir resmiyetle atılmıştır. Ciddi değildir. İkisi birden.*  
Eskişehir 4. Ağır Ceza Mahkemesi kayyum mührü (hayalî)
