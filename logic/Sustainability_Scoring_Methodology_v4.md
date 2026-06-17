# Sustainability Scoring Methodology — v4


## 1\. Purpose and honest framing

The model assigns each event a **0–100 sustainability score** and an
**eco-badge** shown on the website.

> \*\*The score estimates how low-carbon and accessible it is to \*attend\* an
> event — it does not measure the event's actual carbon footprint.\*\*

We have no event-level data on energy, waste, or catering, so we do not claim to
measure them. We score the factors that open data *can* support and that the
sustainable-events literature treats as material. Stating this boundary is what
separates a defensible indicator from greenwashing.


## 2\. The two-axis model (triple bottom line)

Sustainability is conventionally environmental **+** social **+** economic. We
keep these visible rather than collapsing them into one opaque number.

* **Environmental axis (60 pts)** — physical/climate impact, dominated by
attendee travel.
* **Social \& economic access axis (40 pts)** — how low the barrier is for a
newcomer to actually participate.

A separate, non-scored **🌱 flag** surfaces organizer-advertised eco practices.


## 3\. Final component weights

|Axis|Component|Weight|Data field|Confidence|
|-|-|-:|-|-|
|Environmental|**Transit access** (car-free reachability, incl. BIXI)|**40**|`lat` / `long` + STM stops + BIXI stations|Derived (precise)|
|Environmental|**Outdoor / green venue**|**20**|`emplacement`|Measured|
|Social/economic|**Open / walk-in access** (no pre-registration)|**25**|`inscription`|Measured|
|Social/economic|**Free admission**|**15**|`cout`|Measured|
|—|**🌱 Organizer-highlighted eco practices**|*flag only (0)*|`description` / `url\_fiche` text|Self-reported|
||**Total**|**100**|||

Confidence labels: **Measured** = read directly from a field; **Derived** =
computed from data (geographic distance); **Self-reported** = an organizer
claim, shown as a claim, never as verified fact.


## 4\. Why this split — the reasoning

**Environmental gets the majority (60).** The project's emphasis is
sustainability, and the largest *physical* lever we can influence is how people
travel to gather. We give it the larger share without pretending the social
factors are environmental.

**Within environmental, transit (40) ≫ outdoor (20).** For community events,
attendee travel is typically the dominant source of emissions, so reducing
car-dependence is the highest-impact factor — and, with real coordinates, our
best-*measured* one. Outdoor venue is a real but smaller and less rigorous
energy signal, so it earns half the weight.

**Social access = 40, with walk-in (25) > free (15).** This reverses v2 on
purpose:

* *Walk-in / no pre-registration* is the broader accessibility signal. A
required online registration form can be a wall for people who are not
digitally fluent, do not have an email/smartphone, or do not read French — the
exact users this project serves. It bundles the **digital-divide, language,
and administrative** barriers into one measurable field.
* *Free admission*, while important, is likely **low-variance** because most
city community events are already free; a near-constant field carries little
discriminating information (the same reason audience was dropped). It still
earns weight as a real economic barrier, just less than walk-in access.

Price (`cout`) and registration (`inscription`) are **different fields measuring
different barriers** — an event can be free but require registration, or free
and walk-in — so they do not double-count.

**Audience is a filter, not a score.** It is nearly constant ("Pour tous"), so
it adds no discriminating information, and a targeted kids/family/seniors event
is *equity-oriented*, not "less inclusive." It is exposed as a
**"family / kids / all-ages" filter**, which is more useful than a score nudge.

**Eco is a flag, not a score.** The `description` field is too short and sparse
to carry a weighted axis. A 🌱 flag keeps the information without giving weight
to a data-poor signal.


## 5\. How each component is computed

**Transit access (40).** Distance from the event's `lat`/`long` to the nearest
STM stop, with a BIXI bonus:

|Condition|Sub-score|Points|
|-|-:|-:|
|Metro within 500 m|1.00|40|
|Metro within 1 km|0.75|30|
|Bus within 300 m|0.60|24|
|Bus within 600 m|0.40|16|
|No stop within walking distance|0.15|6|

*BIXI bonus:* if a BIXI station or a marked bike path is within \~300 m, add
**+0.15** to the sub-score (capped at 1.00). This extends "reachable without a
car" to active transport. *Seasonal caveat:* BIXI now runs year-round, but with
a reduced winter footprint (see §10), so the bonus is a present-availability
signal, not a guarantee for every date.

*Fallback:* when coordinates are missing, use the borough's STM stop-density
index (0–1) × 40, labelled lower-confidence.

**Outdoor / green venue (20).** `emplacement` = `l'exterieur` → 20; `En salle`
→ 8 (0.4); unknown → 10.

**Open / walk-in access (25).** `inscription` = `Entrée libre`/walk-in → 25;
registration required → 7.5 (0.3); unknown → 12.5.

**Free admission (15).** `cout` = `Gratuit`/free → 15; ≤ $10 → 9 (0.6);
ticketed → 3 (0.2); unknown → 7.5.

## 6\. Self-declared eco — the 🌱 flag

Scanned from `description` (and, optionally, the richer body text behind
`url\_fiche`) for **bilingual EN/FR** keywords (zero waste / zéro déchet,
compost / compostage, recycling / recyclage, éco-responsable, reusable /
réutilisable, vegan / végane, local food / produits locaux, tree planting /
plantation d'arbres, …).

It is a **flag, not points**: if matched, the website shows
🌱 *"Organizer highlights eco practices"*; if not, nothing changes and no score
is lost. Two safeguards: matching is **accent-insensitive** (so broken French
characters still match — see §10), and the label always reads **self-reported**.

*Optional enrichment (stretch):* the event data has `url\_fiche` (e.g.
`montreal.ca/evenements/...`). Fetching that page yields more text than the
one-line CSV `description`. If pursued, restrict it to the filtered cultural/
community events, cache results, and stay within the same official source — do
**not** scrape third-party sites (Eventbrite/QDS/social), which is out of scope
and breaks source consistency. The 20-festival JSON layer already contains rich
text and is a good place to apply this.


## 7\. Badge tiers

|Score|Badge|Icon|
|-|-|-|
|75–100|Green Leader|🌿🌿🌿|
|50–74|Eco-Friendly|🌿🌿|
|0–49|Getting There|🌿|

Every badge ships with a per-component **breakdown** and short **reasons** (e.g.
*"Metro 280 m · Walk-in · Free"*), plus the 🌱 flag when present, so the score is
explainable rather than a black box.


## 8\. Worked examples

|Event|Transit|Outdoor|Walk-in|Free|Total|Badge|
|-|-:|-:|-:|-:|-:|-|
|Free outdoor storytime, metro 450 m, walk-in|40|20|25|15|**100**|🌿🌿🌿|
|Free indoor workshop, bus 280 m, registration required|24|8|7.5|15|**54.5**|🌿🌿|
|$35 indoor concert, no stop nearby, registration|6|8|7.5|3|**24.5**|🌿|

The spread (24.5 → 100) shows the model differentiates rather than rating
everything "green." A 🌱 flag would attach to the storytime if its description
mentioned, e.g., "zero waste."


## 9\. Validation and calibration guardrails

Implements the proposal's Risk-section mitigation ("validate scores against a
manually labelled sample"):

1. **Manual labelling.** Hand-label a stratified sample of 30–50 filtered events
(low / medium / high) and compare to the model's badge; investigate every
disagreement.
2. **Distribution check.** Plot the score histogram. If almost everything lands
in one tier, re-tune the weights/thresholds in the config.
3. **Low-variance guard (a standing rule).** Any component where > 90% of events
share one value carries no information → drop it and reallocate its weight.
*This is why audience was dropped.* **Apply this specifically to `cout`:** if
nearly all events are free, consider reducing free-admission weight further
and moving it to transit. Apply it to `inscription` too, to confirm walk-in
access actually varies.
4. **Coordinate-coverage check.** Report the share of events with usable
`lat`/`long`; the more that fall back to borough-level transit, the lower the
confidence — state this number in the final report.
5. **Future component rule.** Only introduce a separate *proximity / hyperlocal*
component if a real residential-density layer is added; take its weight from
transit. A hand-set borough index is not used because it would be an
unjustified proxy.


## 10\. Data handling notes

* **French encoding (mojibake).** The raw CSV shows broken accents
(e.g. "S??ance", "comit??"). First try re-reading with the correct encoding
(`utf-8`, then `cp1252`). If recoverable, restore accents before any text
matching; if already lost in the source, rely on **accent-insensitive**
keyword matching so French eco terms still match.
* **BIXI seasonal coverage.** BIXI operates year-round, but the network is
larger from April 15–November 15 (\~1,000+ stations across 13+ cities) and
reduced November 16–April 14 (a smaller winter footprint concentrated in \~10
central Montréal boroughs plus Westmount and Montréal-Est). Treat the BIXI
bonus as a present-availability signal and note this limitation in the report.
Also note BIXI and STM are **separate systems** (an STM/OPUS pass does not
cover BIXI), so they represent two distinct low-carbon options, not one.
* **Date filtering.** The dataset includes 2024–2026 events; filter to current/
upcoming before scoring.
* **Administrative events.** Council meetings, public consultations, etc. are
filtered out upstream and not scored.


## 11\. Handoff: output schema for the website

|Column|Type|Example|
|-|-|-|
|`sustainability\_score`|float 0–100|`54.5`|
|`badge`|string|`"Eco-Friendly"`|
|`badge\_icon`|string|`"🌿🌿"`|
|`eco\_flag`|bool|`true`|
|`eco\_flag\_terms`|list\[str]|`\["zéro déchet"]`|
|`score\_breakdown`|dict|`{"transit\_access": 24, "outdoor\_green": 8, ...}`|
|`score\_reasons`|list\[str]|`\["Bus 280 m", "Indoor", "Registration required", "Free"]`|

`badge` and `eco\_flag` are separate so the UI can show the flag without it
affecting the score.


## 12\. Data sources and access

|Source|Use|Access|
|-|-|-|
|`donnees.montreal.ca` — Événements publics|All scored events|Public open data|
|**STM — "Tracés des lignes de bus et de métro"** (portal id `stm-traces-des-lignes-de-bus-et-de-metro`); use the **stops layer `STM\_stops`**|Nearest-stop distance for transit|Public open data, **CC BY 4.0 — must credit STM**|
|**BIXI** stations / bike paths (Montréal open data)|Active-transport bonus|Public open data|
|Curated festival JSON|Festival layer (eco flag works well here)|Built in-house|

**STM dataset specifics (verified):** the `STM\_stops` layer is point geometry,
\~9,457 stops, coordinate system **WGS 84** (matches the events' `lat`/`long`
directly). Stops are delivered from the STM GTFS `stops.txt` as an ESRI
Shapefile and include `stop\_id`, `stop\_name`, and a `wheelchair` accessibility
flag (1 = accessible, 2 = not). The portal's "last modified" date should be
ignored — the resource always points to the latest STM GTFS. Licence is
**CC BY 4.0**, so the data is free to use provided STM is credited; do not use
the STM logo/brand.

*Optional future signal:* the `wheelchair` field on the nearest stop could feed
a small physical-accessibility component on the social axis — left out of v3
until the stop-to-event matching is validated.


## 13\. Framework anchoring — official wording

Each component maps to a recognised framework. The UN SDG target text below is
quoted verbatim from the official UN wording; **cross-check against
sdgs.un.org/goals/goal11 and /goal13 before final submission.**

**SDG 11.2 (covers transit access + walk-in access):**

> "By 2030, provide access to safe, affordable, accessible and sustainable
> transport systems for all, improving road safety, notably by expanding public
> transport, with special attention to the needs of those in vulnerable
> situations, women, children, persons with disabilities and older persons."

**SDG 11.7 (covers outdoor/green venue + social inclusion):**

> "By 2030, provide universal access to safe, inclusive and accessible, green
> and public spaces, in particular for women and children, older persons and
> persons with disabilities."

**SDG 13 (Climate Action — overall framing):**

> "Take urgent action to combat climate change and its impacts."

**ISO 20121** — international standard for *sustainable event management
systems*. We do not claim full conformance; we state which dimensions our
lightweight indicator covers (attendee transport, social inclusion, venue) and
which it does not (procurement, waste, catering).

|Component|SDG target|ISO 20121 dimension|
|-|-|-|
|Transit access (incl. BIXI)|11.2; 13|Attendee transport|
|Outdoor / green venue|11.7; 13|Energy \& venue|
|Open / walk-in access|11.2; 11.7|Social inclusion|
|Free admission|11.2 (affordable); 11.7|Social inclusion|
|🌱 Eco practices (flag)|13|Organizer commitment|

## 14\. References

* United Nations — Sustainable Development Goals: **SDG 11** (sdgs.un.org/goals/goal11),
**SDG 13** (sdgs.un.org/goals/goal13). Quote targets 11.2 and 11.7 from the official text.
* **ISO 20121** — Sustainable Event Management Systems.
* Event-sustainability literature on **attendee travel as the dominant source
of event-related emissions** (cite a specific source when writing the report).
* STM open data — "Tracés des lignes de bus et de métro" (CC BY 4.0).
* BIXI Montréal — year-round service and seasonal coverage.

