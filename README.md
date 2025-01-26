# coopmaster-scale-driver
- komunikator mezi Arduinem a aplikaci zapouzdrujici aplikacni logiku (nest_watcher)

## funkcionalita
- v pravidelnych intervalech načíteá / aktualizuje hodnoty hmotností, které přes seriové porty poskytují jednotlivé váhy v hnizdech
- vystavuje REST API pro ziskani aktuálně načtené hodnoty
- vraci hodnotu v gramech  

## technologie
- python
- c++
- knihovny pro python
  - **Flask**: Lehký webový framework pro rychlý vývoj webových aplikací.
  - **colorama**: Manipulace s barvami v textovém výstupu na terminálu.
  - **waitress**: Rychlý WSGI server pro produkční nasazení webových aplikací.
  - **pyserial**: Komunikace se sériovými zařízeními přes sériové porty.
  - **python-dotenv**: Načítání konfigurace z `.env` souborů.
- knihovny arduina
  - defaultní **Arduino.h**
  - **HX711.h**: knihovna pro komunikaci s module AD Převodníku 24-bit 2 kanály HX711

## hardware
- arduino Nano v3.0
- AD převodník HX711
- tenzometrický senzor
- samotana konstrukce hnizda s vahou (podestylka/koberec)

## konstrukce vahy
- tenzometricky sezor podobne jako u vcel 
- hezky popsano v praci https://www.vut.cz/www_base/zav_prace_soubor_verejne.php?file_id=127769
- uvaha o tom co vybrat zavesna vaha nebo tlacna vaha
- problemy pri implementaci
- problémy s konstrukcí a nekvalitními součástkami
  - senzory se deformují a tím vzniká chyba v měření
  - chyby vznikají díky analogu i chybami / odpory v elektrickém vedení (pevné / pájene spoje vs odnímatelné konektrory)
