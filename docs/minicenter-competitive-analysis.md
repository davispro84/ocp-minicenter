# OCP Mini-Center — Competitive Analysis & Target Segments

Draft v0.1 — 2026-09-29. Companion to `minicenter-executive-summary.html`. Positioning content, not engineering — lower factual risk than the BOM/RFI material, but one timeline claim was still caught and corrected before this went in (see note below).

## 1. The Incumbent Baseline

Vertiv (SmartMod) and Schneider Electric (EcoStruxure) build genuinely strong prefabricated modular data centers, but their baseline assumption is deployment onto an **existing, prepared data center campus**:

- Standard modules expect the site to already provide a central chilled-water loop, a large utility power drop, and a monolithic poured slab.
- Off-the-shelf air-cooled IT modules typically top out around 10-20kW/rack. Reaching 130kW liquid-cooled racks pushes the buyer into a slow, custom engineered-to-order pipeline.

## 2. The Mini-Center Advantage — "The Stranded Edge"

Built for the environments incumbents aren't optimized for: undeveloped, stranded-power sites — flare-gas pads, curtailed solar/wind, decommissioned industrial grid interconnects.

- **Self-sufficient heat rejection** — Skid B brings its own adiabatic fluid cooler, sized to the 4-rack payload. No dependency on a campus chilled-water plant.
- **Self-sufficient power** — Skid B brings its own 600kW-class generator, siteable at flare-gas or off-grid locations. No utility substation required.
- **True drop-and-run logistics** — both skids clear standard 80,000 lb US highway limits on standard flatbeds, foundation options down to concrete piers or a graded pad — not the heavy-haul permits and specialized cranes incumbent 1MW+ monolithic blocks often require.

## 3. Target Customer Matrix

Two specific buyer profiles, not general enterprise IT or colocation:

**Profile A — Neo-Cloud AI Operator** (Crusoe/CoreWeave-adjacent)
- *The need:* capital and compute demand, bottlenecked by multi-year utility interconnection queues. Need to place GB200-class racks wherever power already exists today.
- *The pitch:* "520kW of standard, OEM-compatible, liquid-cooled compute capacity, deployable in days once your site is stubbed up — not years. No grid interconnection queue, no central chiller plant, survives unmanned in West Texas."

**Profile B — Energy Asset Owner** (oil & gas majors, renewable developers)
- *The need:* megawatts of stranded power (flared gas, curtailed wind/solar) generating zero revenue, with no in-house AI infrastructure expertise.
- *The pitch:* "Turn waste gas into compute revenue. A turnkey, zero-maintenance appliance — pour a pad, pipe in the gas, we handle the FMEA, telemetry, and extreme-weather engineering."

---

**Correction made before this document was written (2026-09-29):** the original draft pitched Profile A with "we deliver... in 8 weeks" as a total delivery timeline. That "8 weeks" figure only exists in this project as the **customer's own site-prep lead time** (how long their contractor needs to stub up power/water/pads before trucks arrive, per `minicenter-site-prep-guide.html`) — not a total order-to-power-on SLA. No total delivery timeline has actually been derived or locked anywhere in this project. Replaced with the already-established, defensible framing ("days, not years," pegged to site-prep being the pacing item) rather than asserting a specific commercial commitment nothing in the engineering backs up.
