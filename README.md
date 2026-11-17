# Lintulaudan jyväsäiliön luukku

Puuttuvan lintulaudan täyttöluukun korvaava, 3D-tulostettava kansi. Malli on tehty yhden lintulaudan mittojen mukaan Creality K1 SE:llä tulostettavaksi. Mitat ovat millimetreinä.

## Uusin malli: v7

- [Tulostettava STL](luukku_v7.stl)
- [OrcaSlicer-projekti](luukku_v7.3mf)
- [Muokattava Blender-malli](luukku_v7.blend)
- [Blenderin mallinnusskripti](tee_luukku_v7.py)
- [OpenSCAD-versio](luukku.scad)
- [Sovitusliuska](sovitusliuska_v3.stl)

Lopullinen STL on luotu Blenderissä Python-skriptillä. OpenSCAD-versio on erillinen rinnakkainen toteutus, jonka profiilikerrokset ulottuvat 0,001 mm nimelliskorkeuden yli; Blender ei lue SCAD-tiedostoa.

## Mitat ja kiinnitys

| Ominaisuus | Mitta |
| --- | --- |
| Kannen ulkomitat | 194 × 85 × 10 mm |
| Peitettävä katon syvennys | 130 × 75 mm, syvyys 3,5 mm |
| M6-kierretankojen keskipisteväli | 168 mm |
| Siipimutterin puolen läpireikä | Ø6,8 mm |
| Siipimutterin puolen alapinnan syvennys | Ø12,6 mm, syvyys 7 mm |
| Vastapään läpireikä | Ø12,6 mm |
| Aluslevyjen mitattu koko | Ø11,8 × 1 mm |
| Yläreunan pyöristys | R9,5 mm |
| Kulmien säde ylhäältä katsottuna | R10 mm |

Alareuna on suorakulmainen. Origo on katon syvennyksen vasemmassa alakulmassa; reikien keskipisteet ovat (-18, 30) ja (150, 30) mm.

Siipimutteria löysätään ja vastapää nostetaan mutterin sekä aluslevyn yli, minkä jälkeen kansi käännetään sivuun. Vastapään mutteri ei kiristä kantta, sillä se mahtuu läpireiän läpi.

## Sovitus ja tulostus

Version 3 sovitusliuskan sopivuus on käyttäjän vahvistama. Nimellinen Ø12 mm reikä tulostui noin Ø11,6 mm:nä, joten mutterille ja aluslevylle tarkoitetut reiät kasvatettiin Ø12,6 mm:iin. Korjaus koskee paikallista sovitusta, eikä koko mallia ole skaalattu. Toisella tulostimella tai materiaalilla tarvittava välys voi poiketa.

V7:n tulostus aloitettiin PLA:lla K1 SE:llä OrcaSliceristä seuraavin valinnoin:

- Alapinta tulostusalustaa vasten.
- Tuki siipimutterin puolen syvennyksen katolle, pienen läpireiän ympärille.
- Rectilinear-sisätäyttö 10 %.
- Yläkuori 1 mm, alakuori 0,8 mm; Monotonic-pintakuvio.

Koko v7-luukun lopullista fyysistä sovitusta tai pitkäaikaista ulkokäyttöä ei ole vahvistettu tähän dokumentaatioon. Kansi ei sisällä tiivistettä, eikä vesitiiviyttä ole varmistettu. Tarkista mukana olevan 3MF:n tulostin- ja materiaaliasetukset ennen käyttöä.

## Mallin luominen uudelleen

Blender 5.2.3 LTS:llä käytetty tausta-ajo:

```sh
blender --background --factory-startup -t 1 --python tee_luukku_v7.py
```

Skripti korvaa taustaprosessin aloitusskenen ja kirjoittaa `luukku_v7.stl`- ja `luukku_v7.blend`-tiedostot omaan hakemistoonsa. Aja se erillisessä taustaprosessissa, älä tallentamattoman työskentelyskenen sisällä.

Versiot v1–v6 ja aiemmat skriptit on säilytetty suunnitteluhistoriana. `vie_stl.py` luo version 3 tiedostot; `tee_malli.py` on varhaisempi Blender-vientiskripti. [LUE_MINUT.md](LUE_MINUT.md) sisältää aiempien versioiden muistiinpanot; käytä v7:n osalta tämän README:n ohjeita.
