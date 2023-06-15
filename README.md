# Flowiti proovitöö

## Valmis töö

### Tagarakendus
Tagarakendus on lahendatud Pythonil põhinevas Django raamistikus, mis kasutab andmete hoidmiseks SQLite’i andmebaasi. Lisaks tellimuste andmete haldamisele on tagarakenduses lahendatud ka saatelehtede meiliga saatmine (praegu Gmaili vahendusel). Päringuid saab esitada ainult lubatud IP-aadressilt. Täiendava turvameetmena tuleks lisada kasutajate autentimine. 

### Eesrakendus
Eesrakendus on kirjutatud Vue 3-s. Eesrakendus tõmbab avamisel andmebaasist kõik andmed alla ja moodustab nende põhjal tellimuslehtede tabeli, mille tulpasid saab sisu järgi sortida. Uusi tellimusi eesrakenduses praegu sisestada ei saa (see tuleks juurde arendada). Küll aga saab iga tellimuse avada modaalaknas, et näha selle sisu ja saata tellimus pdf-failina rippmenüüst valitud meiliaadressile või pdf ka alla laadida. Meili saajate nimekiri tuleb andmebaasist töötajate tabelist. Pdfis on kuvatud tellimuse info ning Code128-vormingus triipkood. Kui vajutada saatmise nupule ilma saajat valimata, siis kuvab veateadet. Kui tagarakendus on meili välja saatnud, siis kuvatakse eesrakenduses hüpikteadet ning muudetakse tellimusvormi olek nii andmebaasis kui ka eesrakenduse andmetes (pending -> delivered).

## Lähteülesanne

### Lugu

Kontoritöötaja saadab igapäevaselt laotöötajale infot väljastamist vajavate tellimuste kohta. Selleks otsib ta majandustarkvara andmebaasist tellitud toodete koodid ja nimetused ning kliendi andmed ja koostab saatelehe PDFi ning saadab selle emailiga laotöötajale

## Ülesanne

Tuleks luua lahendus, mis aitaks kontoritöötajal luua saatelehti ja edastada need laotöötajale automaatselt. Lahendus koosneb frontend kasutajaliides ja backend REST API rakendustest, mis omavahel suhtlevad. Läbi kasutajaliidese saab pärida tellimuse numbri järgi tellimuse infot ning näha tellimuse andmeid (tellimuse number, kliendikood, kliendi nimi, kuupäev ja tellimuse ridasid toote kood toote nimetus tellitud kogus).

Andmebaas tuleks ise luua ja peaks sisaldama vähemalt 3 tellimust ja igal tellimusel peab olema vähemalt 2 erinevat toodet. Tellimuse andmetest peab saama koostada saatelehe PDF fail, mis sisaldab tellimuse numbrit, selle põhjal genereeritud triipkood, kliendi koodi, kliendi nime, kuupäeva ning tellimuse ridade infot.

Koostatud PDF tuleks saata saata laotöötaja emaili aadressile programmaatiliselt

### Tingimused

- Backend rakenduse loomiseks kasutada Pythonit ja Django Rest Frameworki
- Frontend rakenduse loomiseks kasutada mõnda JavaScript raamistikku (näiteks Vue'd)
- Triipkoodi formaat on Code128
- Emaili konto peab olema konfigureeritav
- Andmebaasina kasutada SQLite'i

### Oodatud tulemus

Kasutajaliidese kaudu on võimalik leida andmebaasist tellimuse info ja luua selle põhjal saateleht PDF formaadis ning saata see manusena määratud emaili aadressile. Toimiv kood koos SQLite andmebaasi ja paigaldusjuhisega laadida üles koodirepositooriumisse (näiteks GitHub) ning esitamisel jagada linki.
