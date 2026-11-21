# Viikkoraportti 4


## Aikaansaannokset
- Bowyer Watson algoritmin varsinainen toteutus
- Huomattava kehitys testauyksessa
- Sovelluksen arkkitehtuuria muutettu huomattavasti, asioita siirretty mainista omiin moduuleihinsa
Tällä viikolla kehitys on lähtenyt huomattavaan vauhtiin.


## Ydinprojektin kehittyminen
- Bowyer Watson algoritmin varsinainen toteutus. Ydinalgoritmissä tuntuu olevan vielä jokin bugi joidenkin visuaalisten tulosten perusteella.
---

## Tukiohjelmien edistyminen
- Pyplot on havaittu jokseenkin riittämättömäksi tarpeisiin ainakin ilman lisämoduuleja. Asia on työlistalla

---

## Mietteitä testauksesta
Muutamien testien sijoittamisesta on hieman epäselvyyksiä. Järjen mukaan niiden pitäisi olla testikansioissa muiden testien kanssa mutta niiden idea on tuottaa visuaalinen tuotos ihmisen tarkasteltavaksi. Testien ajaminen githubin puolella on myös vielä tekemättä.

---

## Dokumentaation edistyminen
-Siistitty huomattavasti sisäistä suomenkielistä dokumentaatiota, päädytty englannin kieleen virallisessa dokumentaatiossa.
-Sisäistä suomenkielistä dokumentaatiota on vielä jäljellä, tämä on tarkoituksenmukaista ja kehityksenaikaista.

## Mitä olen oppinut
-Unohdin kirjoittaa sen ylös saman tien :C
---

## Epäselvyyksiä
Mitä kurssisivun "Tällä kurssilla laajojen kielimallien. (ChatGPT yms) käyttö on sallittu työn tukena. Projektin kaiken koodin täytyy kuitenkin olla itse kirjoitettua ja kaikesta käytöstä (myös käyttämättömyydestä) täytyy raportoida toteutusdokumentissa." kohta "itse kirjoitettua" tarkalleen ottaen tarkoittaa?
Viitataanko sillä yksinomaan suoraan muualta kopioituun tai toisen ihmisen tekemään koodiin vai saako IDE:n autotäydennystoimintoja ja vastaavaa käyttää normaaliin tapaan?
---

## Seuraavat askeleet
- Virheiden konkreettinen käsittely kautta sovelluksen niin että huonot syötteet eivät kaada koko sovellusta ja sovellus toimii hallitulla tavalla
- Bowyer-Watsonin tuloksen oikeellisuuden tarkastaminen. Koska tässä triangulaatiossa jokaisella kolmiolla on lokaalisti maksimit kulmat, tästä loogisesti johdetaan että jos jokaisella triangulaation pisteellä on sama ominaisuus triangulaatiota on vain yksi. Eli oikeellisuuden tarkasteleminen on hyvin helppoa vertaamalla vakiintuneeseen ja luotettavaan algoritmiin.
- Voronoi-diagrammin johtaminen luotettavaksi havaitusta triangulaatiosta, mahdollinen vertailu pikselitäyttömetodin kanssa pienissä koetapauksissa


## Ajankäyttö