# Montréal Events Map

A free, bilingual (EN/FR), borough-aware community events discovery platform for Montréal — built for newcomers, young families, and allophones who want an easy entry point into community life.

## Live data sources

- **Primary**: [Ville de Montréal Open Data Portal](https://donnees.montreal.ca) — daily-refreshed CSV/API of community events
- **Supplementary**: hand-curated `data/festivals.json` for ~20 major annual festivals (Jazz Fest, MURAL, Francofolies, etc.) that don't appear in the city API

## Architecture

```
montreal-events/
├── .github/workflows/refresh.yml   # daily pipeline run (GitHub Actions)
├── pipeline/
│   ├── fetch.py                    # fetch + filter + clean + score
│   └── requirements.txt
├── data/
│   ├── events.geojson              # generated daily — city events
│   └── festivals.json              # manually maintained — flagship festivals
├── public/                         # frontend (Next.js)
└── README.md
```

Data flows one direction: **API → filter/clean → score → GeoJSON → map frontend**. No database — the GeoJSON file *is* the data layer. This keeps hosting cost near zero (Vercel free tier + GitHub Actions free tier).

## Sustainability score

Each event is scored on five binary signals: free admission, outdoor venue, transit accessibility (via STM GTFS lookup), equity borough, all-ages audience.

## Tech stack

| Layer | Tool |
|---|---|
| Frontend | Next.js, deployed on Vercel |
| Map | Leaflet + OpenStreetMap |
| i18n | next-intl |
| Automation | GitHub Actions (daily cron) |
| Analytics | Plausible |

## Local setup

```bash
cd pipeline
pip install -r requirements.txt
python fetch.py
```

This writes `data/events.geojson`, which the frontend reads directly.

## Team

4-person team project, ~8 weeks. Data pipeline, QA, and bilingual content owned by Yan.

## License

TBD
