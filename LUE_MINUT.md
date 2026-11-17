# Lintulaudan luukku, versio 7

Uusin tulostustiedosto: luukku_v7.stl. Vain yläreuna on pyöristetty, säde R9,5 mm. Alareuna on suorakulmainen, ja ulkosivussa on alimpana 0,5 mm suora osuus. Kulmien säde ylhäältä katsottuna on R10 mm, jotta suuri yläreunan pyöristys jatkuu kulmien ympäri. Ulkomitat 194 × 85 × 10 mm ja version 3 hyväksi todetut reikien sovitusmitat säilyvät. Lähteet: tee_luukku_v7.py ja luukku_v7.blend. Versiota 7 ei ole fyysisesti sovitettu.

Versiossa 7 tulostusasento kannattaa valita Orcassa erikseen: alapinta on leveä ja tasainen, mutta mutterisyvennyksen katto tarvitsee silloituksen tai tuen. Yläpinta alustaa vasten pyöristetty ulkoreuna levenee tulostuksen aikana voimakkaasti ja saattaa tarvita tukia. Aiempi ohje automaattisesti yläpinta alustalle ei siten enää päde.

## Aiemman version tiedot

Lopullinen tulostustiedosto: luukku_v4.stl. Sovitus perustuu käyttäjän hyväksi toteamaan version 3 sovitusliuskaan. Ulkokehän ylä- ja alareunoihin on lisätty R1,5 mm pyöristys; tason kulmien R5 mm pyöristys säilyy. Ulkomitat ja reikien sovitusmitat säilyvät ennallaan. Uusia fyysisiä sovituksia ei ole tehty.

Versio 4 luotiin Blenderillä skriptistä tee_luukku_v4.py. Muokattava tiedosto: luukku_v4.blend. Alla ovat version 3 sovituksen mitat ja ohjeet, jotka pätevät myös versioon 4.

STL-tiedostojen yksikkö on millimetri. Mallia ei ole fyysisesti sovitettu.

- Syvennys: 130 × 75 mm, syvyys 3,5 mm.
- Kierretankojen väli: 168 mm, M6.
- Tankojen paikat syvennyksen vasemmasta alakulmasta: (-18, 30) ja (150, 30) mm.
- Kansilevy: 194 × 85 × 10 mm, kulmasäde 5 mm.
- Siipimutterin reikä: 6,8 mm (suunnitteluvara M6-tangolle).
- Vastapään läpireikä: Ø12,6 mm, jotta myös aluslevy pääsee läpi.
- Siipimutterin reiän alapinnassa on Ø12,6 mm × 7 mm mutteri- ja aluslevysyvennys. Sen yläpuolelle jää 3 mm levyä. Vastapäässä Ø12,6 mm jatkuu läpi koko levyn. Muuten alapinta on tasainen. Kansi peittää syvennyksen 5 mm molemmilta pitkiltä sivuilta ja ulottuu tankojen ohi 13 mm.

Uudet tulostustiedostot ovat luukku_v3.stl ja sovitusliuska_v3.stl. Vanhemmat tiedostot on säilytetty.

Tulosta ensin version 3 sovitusliuska ja kokeile reikien väliä sekä mutterin ja aluslevyn kulkua vastapään reiän läpi. Tulostettu reikä voi jäädä nimellismittaa pienemmäksi. Jos mutteri ei mahdu, suurenna reikää mallissa tai viimeistele se sopivaksi. Liuska ei varmista koko kannen sopivuutta kattoon.

STL:ssä mutterisyvennykset avautuvat alaspäin. Käännä malli viipalointiohjelmassa tasainen yläpinta alustaa vasten, jolloin syvennykset avautuvat ylöspäin. Käytä tulostusohjelmassa K1 SE:n sekä käytössä olevan suuttimen ja materiaalin omaa profiilia. Älä skaalaa mallia reikien sovittamiseksi, koska myös 168 mm reikäväli muuttuisi.

Avaaminen: löysää siipimutteria, nosta vastapää mutterin ja kierretangon yläpuolelle ja käännä kansi sivuun. Tarvittava nostotila ja siipimutterin puolen kallistusvara on kokeiltava. Tavallinen mutteri ei kiristä kantta, jos se mahtuu reiän läpi.

Tämä versio ei sisällä tiivistettä eikä sille luvata vesitiiviyttä. Alkuperäisen katon kaarevuuden vaikutus sovitukseen on vielä varmistamatta.

Muokattava malli: luukku.scad. STL-tiedostot luotiin riippuvuuksettomalla vie_stl.py-ohjelmalla. tee_malli.py on vaihtoehtoinen Blender-vientiskripti; Blender kaatui tässä ympäristössä, eikä blend-tiedostoa syntynyt.

Version 3 sovituskorjaus: käyttäjän mittaama Ø12 mm syvennys tulostui Ø11,6 mm:nä. OrcaSlicerin näyttämä säde 5,993 mm vastaa halkaisijaa 11,986 mm, joten tiedoston nimellismitta on noin 12 mm. Ø12,6 mm on paikallinen sovituskorjaus: samalla 0,4 mm halkaisijaerolla tulos olisi noin Ø12,2 mm. Tämä on arvio, ei koko kappaleen kutistumiskerroin. Aluslevy on Ø11,8 × 1 mm. Uuden version sopivuus on kokeiltava.
