# Gemini Prompt — Rough BOM / Cost Model for Vendor-TBD Equipment

Draft v0.1 — 2026-10-06. Built specifically for the items the BOM (`minicenter-bom.html`) marks unselected or illustrative-only. Written with explicit anti-fabrication ground rules given this project's own verification-incident history (`verification-incidents.md`) — six prior fabricated/stale claims from outside AI tools, caught and logged, on this exact project. Treat whatever comes back as a lead, never a fact, same rule as everything else here.

---

## The prompt (copy-paste as-is)

```
I'm developing the procurement-stage Bill of Materials and a rough cost model
for a real engineering project: a modular, two-skid, 520kW AI data center,
deployable via standard flatbed trucks to stranded-power sites (flared gas,
curtailed renewables, decommissioned industrial interconnects). I need help
identifying realistic candidate vendors/products and rough costs for the
equipment categories listed below.

IMPORTANT GROUND RULES — read before answering:
- I will independently verify every claim against the manufacturer's actual
  published cutsheet before anything enters a real design. Do NOT present a
  guess as a confirmed fact. If you're not highly confident a specific model
  number, spec, or price is accurate, say so explicitly instead of stating it
  with confidence.
- Do not fabricate a specific cutsheet citation, quote, or "verified" data
  point you haven't actually seen. An honest "this is a typical price range
  for this equipment class" is far more useful than a precise-sounding number
  with no real source behind it.
- For every line item, give: (1) 2-3 realistic manufacturer/product-family
  candidates — not necessarily one exact SKU if you're unsure which fits best,
  (2) a rough unit cost range in USD with your own confidence level
  (High/Medium/Low), (3) what a real quote or RFI would still need to confirm.
- Frame every cost figure explicitly as a rough order-of-magnitude budgetary
  estimate for an early-stage internal cost model — not a vendor quote.

LOCKED DESIGN DECISIONS — do not suggest alternatives to these:
- Compute racks: OCP ORv3, 4 per skid, 130kW continuous each (520kW total IT load)
- CDU: 2x Motivair MCDU-25 (625kW each, N+1), standard OCP BMQC-compliant
  positive-pressure cooling — already selected, don't propose a different CDU
- Power architecture: standard 480V/415V 3-phase AC, no DC bus
- Fluid: Dowfrost PG25 (secondary/IT loop), PG30 or PG60 (primary/facility
  loop depending on climate)

WHAT I NEED COST/VENDOR INPUT ON — all currently unselected:

1. 1200A 480VAC 3-phase main switchgear + automatic transfer switch (ATS),
   rated for a 600kW-class standby generator source
2. Power distribution units (PDU-A / PDU-B) feeding 4x dual-corded OCP ORv3
   racks — give realistic amperage/breaker configurations, not just a brand
3. Remote power panel (RPP), if one is typically used downstream of a PDU in
   this kind of high-density rack deployment to distribute branch circuits —
   tell me honestly whether an RPP is standard practice here, or whether the
   PDU's own distribution section usually does this job for OCP-class rack
   power shelves
4. 600kW-class standby generator (diesel and natural gas variants), Level 2
   acoustic enclosure, extreme-cold-weather package (block heater, battery
   warmers, PMG excitation) — candidate manufacturers and rough pricing
5. Zoned liquid leak-detection rope/cable system with dry-contact output,
   sized for a ~40ft equipment room
6. Inter-skid quick-connect power cable assemblies — Series 16 Cam-Lok-style,
   480V/400A class, paralleled per phase for 1200A total — realistic cable
   assembly vendors and rough per-set cost
7. Industrial edge gateway / RTU for aggregating CDU/PDU/ATS/generator
   telemetry via Modbus TCP, with local alert logic — an industrial
   remote-monitoring-class product, not a data-center DCIM appliance
8. Cellular modem + satellite uplink hardware (Starlink or equivalent) for
   redundant remote-site connectivity
9. 40ft High-Cube ISO shipping container, new or reconditioned, suitable as
   a base shell for an electrical/compute retrofit

FORMAT: one markdown table per category — Candidate Vendor/Product | Rough
Unit Cost (USD) | Confidence | What Still Needs Verification. End with a
rough total cost range for the full list, clearly labeled as a budgetary
planning number, not a quote.
```

## After you get a reply

Run it through the same filter as every other outside-AI claim on this project:
- Any sentence that reads like "verified," "confirmed," or "the real spec is X" without a cutsheet/link attached → treat as unverified, log it the same way `verification-incidents.md` already does if it's wrong.
- Cross-check anything that would swap out an already-locked decision (CDU vendor, rack standard, power architecture) — reject outright, same as incident #6.
- Feed anything that looks real and specific into an actual RFI or vendor site lookup before it goes into `minicenter-bom.html`.

---
Companion to `minicenter-bom.html`, `rfi-drafts.md`, and `pre-cad-readiness.md`.

## Results & Filtering Verdict (2026-10-06)

Ran the prompt above through Gemini. Full reply filtered item-by-item the same way `verification-incidents.md` filters everything else. Verdict:

**What survived, as candidates (none locked — all still need a real cutsheet/quote before procurement):**
- Switchgear/ATS: ASCO 7000 + Square D QED ($40-80k), or Eaton Magnum DS ($45-85k)
- PDU-A/B: Vertiv Liebert FDC/FPC or Schneider Galaxy/EcoStruxure ($60-130k/pair)
- Generator: Generac Industrial SG Series NG ($110-160k, self-rated Low confidence) or Cummins/Caterpillar diesel ($80-130k, Medium confidence)
- Leak detection: RLE SeaHawk or TTK FG-NET/FG-SYS ($2-5k)
- Cable assemblies: Trystar or Lex Products ($5-14k — unclear if per-cable or per-set, needs clarification)
- Edge gateway: Opto 22 groov EPIC or Allen-Bradley CompactLogix ($3-9k)
- Cellular/satellite: Starlink + Cradlepoint, or Peplink ($1-5k)
- Container: ConGlobal/Sea Box, corrected to $6,500-9,500 for true new "one-trip" (see below)

**What got rejected or corrected before accepting:**
- **RPP question — accepted as a real architectural answer, not just a cost estimate.** "Not required" is internally consistent with the already-locked no-DC-bus architecture; adopted into `minicenter-bom.html` and the checklist as a decision, not left as a cost-pass footnote.
- **Cable count corrected.** The original 15-cable estimate (3 phases + neutral + ground, ×3 parallel each) over-applies paralleling to the grounding conductor. NEC Table 250.122 sizes the equipment grounding conductor off the 1200A OCPD rating directly (3/0 Cu / 250 kcmil Al) — independently checked against real NEC table data, confirmed correct. Re-count likely lands near 9-10 cables, not 15.
- **Container pricing self-corrected mid-conversation** — initial $3,500-7,500 estimate was closer to used/cargo-worthy pricing; corrected to $6,500-9,500 after being asked to check current listings for true new "one-trip" stock.
- **New finding, not previously in this project anywhere:** standard pipeline-spec NG generator engines aren't automatically rated for the variable-BTU, H2S-bearing wellhead/flare gas this project's own target sites would actually produce. Added to RFI 1 (see above) rather than accepted or dismissed outright — a real open question, not a fabrication risk.

**Notable positive:** unlike the two prior generator-spec fabrications logged in `verification-incidents.md` (a specific invented weight/dimension, and an invented "<10 second" quote), this pass stayed at the product-family level with explicit self-rated confidence per line and never asserted a specific SKU, weight, or quote as fact — the ground-rules framing in the prompt appears to have worked as intended.

---

## Round 2 prompt (2026-10-06) — the items Round 1 missed

Round 1 covered switchgear/ATS, PDU, RPP, generator, leak detection, cable assemblies, edge gateway, cellular/satellite, and the container — but missed the *other* RFI-gated big-ticket item (heat rejection) plus several smaller unpriced line items the pre-CAD review surfaced. Same ground rules as Round 1 apply; copy-paste as-is.

```
Same ground rules as before: don't present a guess as a confirmed fact, flag
your own confidence per item (High/Medium/Low), don't fabricate a specific
cutsheet citation or quote, frame all costs as rough order-of-magnitude
budgetary planning numbers.

UPDATED LOCKED DECISIONS (new since last time):
- No Remote Power Panel — 480V distributes directly from PDU-A/B to each
  rack's power shelf, ~156.4A per feed, 2N (each feed sized for the full
  load alone)

THIS ROUND'S ITEMS — all still unpriced/unselected:

1. 550kW adiabatic V-coil fluid cooler — 30% propylene glycol, max 35°C
   leaving fluid temperature, mounted on a standard flatbed trailer (length
   and wet weight are hard constraints). Candidate manufacturers (EVAPCO,
   Güntner, BAC, Munters, Alfa Laval) and rough budgetary cost — flag plainly
   that exact capacity/footprint is normally selection-software-gated per
   vendor, so treat this as a rough planning range, not a sizing claim.
2. 10kVA double-conversion lithium-ion UPS, dedicated to an "Auxiliary
   Mechanical Bus" (CDU pumps, trace heating, monitoring stack) — separate
   from any IT rack UPS/BBU. Candidate vendors and rough cost.
3. Diesel sub-base fuel tank sized for a 600kW standby generator — what's a
   realistic capacity (gallons) for a useful extended-runtime window (give
   me the runtime-vs-capacity tradeoff, not just one number), typical vendor
   candidates, and rough cost including the tank itself (not the generator).
4. 3" Insulated Metal Panel (IMP) product for an interior partition wall —
   PIR foam core, 26ga galvanized steel skins, needs to accept Roxtec
   compression transits for cable/pipe penetrations. Candidate manufacturers
   and rough cost per the ~40ft length needed, plus their actual tested
   R-value (we've been using an estimated ~R-24 pending a real product).
5. Instrumented shock/vibration data logger for transit monitoring (records
   accelerometer data during truck transport to flag any event exceeding
   design tolerance). Candidate vendors and rough cost.
6. Follow-up on the Round 1 Cam-Lok cable assembly answer: clarify explicitly
   whether your $5,000-14,000 figure was per individual cable or per full
   cable set, and re-run the total using a corrected count of ~9-10 cables
   (3 phases x 3 parallel, plus a single un-paralleled ground per NEC Table
   250.122, no neutral if there's no 277V single-phase load) instead of the
   original 15.

FORMAT: same as before — one table per item, Candidate Vendor/Product |
Rough Cost (USD) | Confidence | What Still Needs Verification. End with an
updated total range that also re-states the Round 1 total with the corrected
cable-count line, so I have one current number.
```

## Round 2 Results & Filtering Verdict (2026-10-06)

**Two caught, same pattern as prior incidents:**
- A specific Vertiv UPS SKU (`GXT5LI-10KMVRT4UXLN`) given at "High confidence" with no cutsheet behind it — the exact shape of the two previously-logged generator fabrications (confident + specific + no source). Kept the product family, rejected the exact part number.
- "Your estimate is dead-on" on the R-24 partition-wall value — a convergence-on-the-prior tell, same shape as the rejected ASHRAE wet-bulb claim. The generic PIR-foam physics is real; it is not independent confirmation of this project's specific number. R-24 stays an estimate.

**What survived, as candidates only (none locked):**
- Adiabatic cooler: EVAPCO/Güntner ($60-110k) or BAC/Alfa Laval ($65-115k) — flagged as the softest number in the whole BOM, explicitly selection-software-gated
- UPS: Liebert GXT5 Lithium-Ion family, APC Smart-UPS SRT, or Eaton 9PX Li-Ion ($10-16k) — family names only
- Fuel tank: Tramont/Pryco ($7-15k, tank only) — "Simplex" named but less certain as a sub-base-tank-specific maker, worth independently checking
- IMP partition wall: Kingspan or Metl-Span ($5-10k for ~40ft)
- Shock logger: SpotSee ShockLog or Lansmont SAVER ($3.5-5.5k)
- Cable follow-up: corrected to 10 cables (not 15), ~$5-9k per set — internally consistent with the earlier per-cable estimate

**Checked and held up:**
- Diesel burn-rate math (40-45 gal/hr at 600kW) and the tank-size-to-runtime conversions are internally consistent and match real industry rule-of-thumb figures.
- Re-summed the combined total myself from the individual line items as a check — the claimed $284k-$570k combined range is arithmetically consistent with the per-item numbers, not a fabricated rollup.

**Real finding that came out of this pass, not previously anywhere in the project:** a diesel sub-base fuel tank was never in the BOM or the weight tracker at all. Fuel alone (not even the tank structure) adds multiple thousand kg at any useful runtime capacity — added to the weight tracker in `minicenter-checklist.md`, which **materially weakens the previous "weight is unlikely to be the binding constraint" conclusion for Skid B.** Flagged there as a reopened question, not a closed one.



