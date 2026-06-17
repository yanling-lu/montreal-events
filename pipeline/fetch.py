"""
Montréal events pipeline — fetch, filter, clean, score, export.

Currently a placeholder. Once filtering decisions are finalized
(event types, columns, date range), this script will:
  1. Fetch from donnees.montreal.ca with server-side filters
  2. Clean & cast types (dates, lat/long)
  3. Apply sustainability scoring (free, outdoor, transit, equity, all-ages)
  4. Write data/events.geojson
"""

import json
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "events.geojson")


def main():
    # TODO: replace with real API fetch + filtering logic
    geojson = {
        "type": "FeatureCollection",
        "features": [],
    }
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
