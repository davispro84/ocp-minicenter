# OCP Mini-Center — Single-Line Diagram & Skeleton Panel Schedules

Draft v0.2 — 2026-10-06. Skid A electrical distribution, drafted specifically to unblock Revit modeling — this is the gating document `pre-cad-readiness.md` called out as more important than the BOM itself for a real electrical model. Both flags from v0.1 are now resolved (see below) — remaining soft item is the UPS input breaker, noted at the bottom.

**Do not treat anything below as locked until the real equipment selections (switchgear, PDU, generator) come back from RFI.** Same rule as everything else in this project — this is a skeleton for modeling purposes, not an issued-for-construction schedule.

## Flags — resolution log

1. **RESOLVED 2026-10-06 — SWBD-4 load.** Was 25kW/30.1A, conflicting with the established 5-8kW Hot-Climate Kit figure used everywhere else in this project. Confirmed as drift — reverted to a generic air-cooled-container assumption rather than this architecture's actual thermal split: the two Motivair CDUs carry 95%+ of IT heat directly to the fluid loop, so the wall-mount climate kit only handles parasitic rack-chassis radiation (~2-3% of IT load), switchgear/PDU/UPS heat loss, and solar gain through the container walls — exactly the load the 5-8kW figure was sized for. Corrected to **8.0kW (9.6A) → 20A/100A breaker** (9.6A × 1.25 = 12.03A, next standard size 15A minimum; 20A chosen with margin, matches a standard 12 AWG branch conductor).
2. **RESOLVED 2026-10-06 — PDU branch conductor.** 225A trip was mismatched with 3/0 AWG Cu (rated exactly 200A at 75°C, which doesn't satisfy NEC 240.4(B)'s "next standard size" exception since 200A is itself already a standard size). Corrected to **225A trip / 4/0 AWG Cu** (230A rated) throughout the PDU schedule below.

**Still worth a second look, not necessarily wrong:** SWBD-3's 60A/100A breaker for a 12A continuous UPS input load is a large margin under plain 125%-factor logic (12A × 1.25 = 15A). Could be legitimate — UPS input breakers are often sized well above nameplate for charging/inrush current — but verify against the real UPS's recommended input breaker size once a unit is selected, rather than carrying 60A/100A as a calculated value.

## Design basis

- 480Y/277V, 3-phase, 4-wire + ground
- 520kW total IT load, 4× OCP ORv3 racks, 130kW continuous each, 2N (each A/B feed sized to carry the full rack load alone)
- 600kW-class standby generator, ATS-switched from utility/off-grid source
- 10-cable Cam-Lok inter-skid connection (3 phases × 3 parallel + 1 un-paralleled ground per NEC Table 250.122, no neutral)

## Feeder sizing — hand-checked

- 520kW ÷ (√3 × 480V) = **625.5A** continuous
- × 1.25 (NEC 210.19(A)(1) continuous-load factor) = **781.9A** → **800A frame/trip** for each PDU feeder — sized for the *full* load because 2N means either feed must carry everything alone on a single-feed failure, not half
- 130kW ÷ (√3 × 480V) = **156.4A** per rack feed
- × 1.25 = **195.5A** → **225A trip / 4/0 AWG Cu** per rack branch (see flag #2 above)
- 600kW standby generator at the standard 0.8PF rating = 750kVA ÷ (√3 × 480V) = **902.7A** FLA — matches the ~902A shown below

## Single-line diagram

```text
       [ 480Y/277V UTILITY INTERCONNECT ]             [ 600kW STANDBY GENERATOR ]
           1200A Service, 3PH, 4W + G                   480Y/277V, ~902A Standby FLA
                       │                                             │
                       │                                             │ (10x Series 16 Cam-Loks:
                       │                                             │  3/ph + 1 EGC, no neutral)
                       └───────────────┐             ┌───────────────┘
                                       ▼             ▼
                             [ 1200A 3-POLE / 4-POLE ATS ]
                                 (ASCO 7000 or Eaton — candidates only, unverified)
                                           │
                                           │ 1200A Main Bus
                                           ▼
                       [ 1200A MAIN SWITCHBOARD (SWBD-1) ]
                         480Y/277V, 3PH, 4W, 65kA SCCR (assumed, pending fault study)
       ┌───────────────────────┬───────────────────────┬───────────────────────┐
       │                       │                       │                       │
       ▼                       ▼                       ▼                       ▼
  [ SPD-1 ]              [ CB-1: 800A/3P ]       [ CB-2: 800A/3P ]       [ CB-3: 60A/3P ]
  250kA/mode             Feeds PDU-A             Feeds PDU-B             Feeds 10kVA Aux UPS
  Cat C, Form C          (IT Feed A)             (IT Feed B)             (Mechanical/Controls)
                               │                       │                       │
                               ▼                       ▼                       ▼
                           [ PDU-A ]               [ PDU-B ]             [ 10kVA UPS ]
                          800A MLO Bus            800A MLO Bus          Double-Conversion
                               │                       │                       │
                 ┌─────────────┼─────────────┐         │                       ▼
                 ▼             ▼             ▼         │                  [ LP-AUX ]
               Rack 1        Rack 2        Rack 3...   │              120/208V Distribution
              (Shelf A)     (Shelf A)     (Shelf A)    │               - Motivair CDU Controls
                 ▲             ▲             ▲         │               - Opto 22 Edge Gateway
                 └─────────────┼─────────────┴─────────┘               - RLE Leak Detection
                           From PDU-B                                  - Trace Heating & Comms
                          (Shelf B 2N)
```

## Skeleton panel schedules

### A. Main Switchboard (`SWBD-1`)

- **Bus rating:** 1200A, 480Y/277V, 3-phase, 4-wire, 65kAIC (assumed pending a real fault-current study — see `pre-cad-readiness.md`)
- **Main device:** 1200A main circuit breaker, fed from ATS

| Circuit | Trip/Frame | Poles | Connected Load | Category | Destination |
|---|---|---|---|---|---|
| SWBD-SPD | Internal tap | 3 | — | Protection | 250kA/phase Cat C SPD, Form C contacts to RTU — **locked spec**, FMEA 2.5 |
| SWBD-1 | 800A/800A | 3 | 520kW (625.5A) | Critical IT, Feed A | PDU-A, full 2N rating |
| SWBD-2 | 800A/800A | 3 | 520kW (625.5A) | Critical IT, Feed B | PDU-B, full 2N rating |
| SWBD-3 | 60A/100A | 3 | 10kVA (12.0A) | Critical Aux | 10kVA Li-ion Aux UPS — **verify against real UPS input breaker spec, see flag above** |
| SWBD-4 | 20A/100A | 3 | 8.0kW (9.6A) | Facility Support | Wall-mount container HVAC (parasitic load only — see resolution log) |
| SWBD-5 | Space | 3 | — | Spare | Reserved, Skid B trace-heat interconnect |

### B. Power Distribution Units (`PDU-A` & `PDU-B`)

- **Bus rating:** 800A MLO, 480V, 3-phase, 3-wire + ground. Identical schedule both units.

| Branch | Trip/Frame | Poles | Connected Load | Destination | Conductor |
|---|---|---|---|---|---|
| PDU-1 | 225A/250A | 3 | 130kW (156.4A) | Rack 1 power shelf | **4/0 AWG Cu** (corrected from 3/0 — see flag #2) |
| PDU-2 | 225A/250A | 3 | 130kW (156.4A) | Rack 2 power shelf | 4/0 AWG Cu |
| PDU-3 | 225A/250A | 3 | 130kW (156.4A) | Rack 3 power shelf | 4/0 AWG Cu |
| PDU-4 | 225A/250A | 3 | 130kW (156.4A) | Rack 4 power shelf | 4/0 AWG Cu |
| PDU-SP | Space | 3 | — | Expansion | Up to 250A frame |

### C. Auxiliary Distribution Panel (`LP-AUX`)

- **Feed:** 10kVA UPS output, 120/208V, 3-phase, 4-wire + ground, 42-circuit panelboard. Connected load sums to 8.0kVA against 10kVA capacity (80% loaded) — checks out with real margin.

| Ckt | Trip | Poles | Voltage | Load | Destination |
|---|---|---|---|---|---|
| 1, 3 | 20A | 2 | 208V | 1.8kVA | Motivair MCDU-25 primary controls |
| 5, 7 | 20A | 2 | 208V | 1.8kVA | Motivair MCDU-25 redundant controls |
| 9 | 20A | 1 | 120V | 0.5kVA | Opto 22 groov EPIC RTU |
| 11 | 20A | 1 | 120V | 0.3kVA | RLE leak detection controller |
| 13 | 20A | 1 | 120V | 0.4kVA | Starlink terminal + cellular gateway |
| 15 | 20A | 1 | 120V | 0.2kVA | Door/environmental interlocks |
| 17, 19 | 30A | 2 | 208V | 3.0kVA | Skid A/B trace heating |
| 21-42 | — | — | — | — | Spare |

---
Companion to `minicenter-bom.html`, `minicenter-fmea.html`, `pre-cad-readiness.md`, and `rfi-drafts.md`.
