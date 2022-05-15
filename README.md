# Matopeli
#### Sovelluksessa käyttäjä ohjaa matoa ja yrittää syödä ruokaa. Mato kasvaa ruokaa syödessä. Pelin häviää, jos madon pää törmää omaan kehoonsa. Suunnitelman mukaan sovellukseen tulee vielä graafinen käyttöliittymä sekä sitä voi pelata eri tallennuksilla.
## Dokumentaatio

[vaatimusmaarittelyt.md](https://github.com/VeetiE/ot-harjoitustyo/blob/616726f5d6fef61b10c647811b138121b83db6eb/laskarit/viikko1/vaatimusmaarittely.md)

[tyoaikakirjanpito.md](https://github.com/VeetiE/ot-harjoitustyo/blob/8d28dbc7f2046991de4d43bb066923ab6f049cbd/tyoaikakirjanpito.md)

[changelog.md](https://github.com/VeetiE/ot-harjoitustyo/blob/a03e881599c8f1e92613efc0f92ffce00fec8a64/matopeli/dokumentaatio/changelog.md)

[arkkitehtuuri.md](https://github.com/VeetiE/ot-harjoitustyo/blob/a03e881599c8f1e92613efc0f92ffce00fec8a64/matopeli/dokumentaatio/arkkitehtuuri.md)

## Asennus

Asenna riippuvuudet komennolla:

```bash
poetry install
```

Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Tiedoston pylint tarkistukset voidaan suorittaa komennolla:

```bash
poetry run invoke lint
```
