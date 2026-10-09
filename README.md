# Python SOC Monitor

## Om prosjektet

Python SOC Monitor er et Python-basert prosjekt for sikkerhetsovervåking og deteksjon av mistenkelig aktivitet.

Prosjektet simulerer hvordan et Security Operations Center (SOC) kan analysere sikkerhetshendelser og generere varsler når bestemte deteksjonsregler oppfylles.

## Prosjektmål

Målet er å utvikle et sikkerhetsovervåkingssystem som kan:

- Behandle sikkerhetshendelser.
- Normalisere hendelser til et felles format.
- Oppdage mistenkelige innloggingsforsøk.
- Generere sikkerhetsvarsler.
- Utvides med database, API og dashboard.

## Nåværende funksjoner

- Syntetiske sikkerhetshendelser for testing.
- Normalisering av sikkerhetshendelser.
- Deteksjon av flere mislykkede innlogginger.
- Gruppering av innloggingsforsøk etter brukernavn.
- Kontroll av tidsvindu.
- Generering av sikkerhetsvarsler.

## Detection Rule

**Regel:** multiple_failed_logins

Programmet genererer et sikkerhetsvarsel når samme bruker har minst tre mislykkede innlogginger innen 60 sekunder.

**Alvorlighetsgrad:** Medium

## Prosjektarkitektur

Security Events → Collector → Normalization → Detection Engine → Alert

Planlagte utvidelser:

Database → REST API → SOC Dashboard

## Prosjektstatus

- Phase 1 – Project Setup + Git: Fullført
- Phase 2 – Synthetic Events: Fullført
- Phase 3 – Event Normalization: Fullført
- Phase 4 – Detection Engine: Pågår

## Testing

### Negative Test
Programmet ble testet med to mislykkede innlogginger
for samme bruker.

Resultat: Ingen sikkerhetsvarsel (Alert) ble generert.

Status: Bestått.

### Positive Test
Programmet ble testet med tre mislykkede innlogginger
for samme bruker innen 60 sekunder.

Resultat: Et sikkerhetsvarsel (Alert) ble generert.

Status: Bestått.

### Time Window Test

Programmet ble testet med tre mislykkede innlogginger
for samme bruker, fordelt over 90 sekunder.

Resultat: Ingen sikkerhetsvarsel (Alert) ble generert,
fordi tidsgrensen er 60 sekunder.

Status: Bestått.

### Event Order Test

Programmet ble testet med sikkerhetshendelser
i feil tidsrekkefølge.

Resultat: Programmet oppdaget fortsatt tre
mislykkede innlogginger innen 60 sekunder
og genererte et sikkerhetsvarsel (Alert).

Status: Bestått.

## Teknologier

- Python
- Visual Studio Code

## Videre utvikling

Prosjektet skal videreutvikles med flere deteksjonsregler, lagring av hendelser, API og et webbasert SOC Dashboard.