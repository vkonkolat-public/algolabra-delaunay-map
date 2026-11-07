# Viikkoraportti 2

## Aikaansaannokset
- Koodi saa nyt aikaan pisteitä ja kolmioita visualisoinnin kera
- Olen tehnyt runsaasti aivotyötä triangulaation tietorakenteiden suhteen mutta pisteiden, särmien ja kolmioiden välisissä suhteissa on jokin ilmiselvä lainalaisuus jota en ole hahmottanut.

---

## Ydinprojektin kehittyminen
- Päädyin Bowyer-Watsonin algoritmin toteuttamiseen sen suhteellisen yksinkertaisuuden takia. Päätin toteuttaa ensin jotain joka sopii aikavaatimuksen O\(n^2\) sisään ja lähden sen jälkeen optimoimaan kohti O\(n log n\).
- Olen hahmottanut että kaikessa on pohjimmiltaan kyse neljän pisteen matriisilaskuista, selittää maalaisjärjelle miksi MATLAB olisi niin hyvin optimoitu sen suhteen

---

## Tukiohjelmien edistyminen
- Otin matplotlib-kirjaston kehitystyökaluksi jotta pystyn visualisoimaan tuloksia välittömästi 

---

## Mietteitä testauksesta
- Delaunay-triangulaation toteuttamiseen on monta tehokasta algoritmia ja ilmeisesti varsinkin MATLABin algoritmi siihen käyttää hajoita-ja-hallitse -pohjaista, pitkälle optimoitua algoritmia. 

---

## Dokumentaation edistyminen
- Github Copilot tuotti vaikuttavan oloisen roadmapin speksien pohjalta. Sen hyödyllisyys ja merkitys projektille on toistaiseksi arvioinnin alla.

---

## Mitä olen oppinut
- Github lisää '.gitkeep' tiedoston tyhjiin kansioihin, koska se ei pysty seuraamaan tyhjää hakemistoa itseään
- Triangulaatio sisältää yllättävän vähän trigonometriaa ja yllättävän paljon matriisilaskentaa.

---

## Epäselvyyksiä

- Graafisen käyttöliittymän rakentaminen itse ilman kirjastoja

---

## Seuraavat askeleet
- Primin ja Kruskalin algoritmien toteutus ja käytäntö. https://www.geeksforgeeks.org/dsa/difference-between-prims-and-kruskals-algorithm-for-mst/ näyttää hyödylliseltä verkkolähteeltä. Aikataulu on tiukka joten koko toimintojen sarja pisteistä lopputulokseeen on hyvä hahmotella jo alussa
- matriisilaskenta sen selvittämiseksi onko piste d kolmion(a,b,c) ulkoympyrän sisällä vaikuttaa suhteellisen simppeliltä kahdeksan tekijän (ax, ay, bx, by, cx, cy, dx, dy) laskennalta tai ainakin siihen löytyy suoria lähteitä. A, B ja C täytyy olla ulkoympyrällä vastapäivään ja tällä lienee trigonometrinen peruste.

## Ajankäyttö
Noin 12 tuntia, enimmäkseen materiaaliin ja olemassa oleviin toteutuksiin tutustuen