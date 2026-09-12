# Python SOC Monitor

Et Python-basert prosjekt for sikkerhetsovervåking og deteksjon.

## Prosjektmål

Målet med dette prosjektet er å bygge et lite SOC-overvåkingssystem som samler inn sikkerhetshendelser, normaliserer dem, bruker deteksjonsregler og genererer varsler ved mistenkelig aktivitet.

## Nåværende funksjoner

- Syntetiske sikkerhetshendelser
- Behandling av hendelser med Python
- Prototype for deteksjon av mislykkede innloggingsforsøk
- Varsel utløses etter 3 mislykkede innloggingshendelser

## Prosjektarkitektur

Sikkerhetshendelser
→ Innsamling
→ Normalisering
→ Deteksjonsmotor
→ Varsler
→ Database
→ API
→ Kontrollpanel

## Nåværende status

- Fase 1: Prosjektoppsett og Git - Fullført
- Fase 2: MVP med syntetiske hendelser - Fullført
- Fase 3: Event Schema og normalisering - Fullført
- Fase 4: Deteksjonsmotor - Pågår