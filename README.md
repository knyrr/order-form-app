# Flowiti proovitöö

## Prooviülesanne

### Lugu

Kontoritöötaja saadab igapäevaselt laotöötajale infot väljastamist vajavate tellimuste kohta. Selleks otsib ta majandustarkvara andmebaasist tellitud toodete koodid ja nimetused ning kliendi andmed ja koostab saatelehe PDF i ning saadab selle emailiga laotöötajale

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

