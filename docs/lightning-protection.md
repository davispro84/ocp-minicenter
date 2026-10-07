# Basis of Design: Direct Lightning Protection (NFPA 780)

Draft v0.1 — 2026-10-07. Companion document to `grounding-basis.md`. Defines the direct-strike protection system, complementing the already-locked 250kA Category C SPDs (which handle conducted surge only — this document covers the separate direct-strike case). Since the Mini-Center deploys to open, flat environments (West Texas oil pads, rural wind farms), it's a real exposure, not a theoretical one.

**One correction applied before this was saved, one flagged for verification** — see the callouts in Sections 1-2 and 4.

## 1. Strike Termination Devices (Air Terminals)

NFPA 780 allows a metal roof to serve as its own strike termination device, but the metal must be thick enough to resist burn-through/puncture from a direct strike (commonly cited around 3/16in / 4.8mm for steel).

- **Constraint:** standard ISO shipping container roofs are roughly 2mm (14-gauge) Corten steel — well under the thickness needed to safely self-serve as a strike termination device without risking a melt-through event directly above the IT racks.
- **Design (Skid A):** dedicated air terminals (lightning rods) installed along the container roof perimeter and ridge. **Correction applied 2026-10-07:** component class corrected from Class II to **Class I** — NFPA 780 classifies Class I for structures 75ft (23m) or under, Class II for structures exceeding 75ft. A 40ft container skid is well under that threshold; Class II components would be an unnecessary (if not unsafe) over-spec.
- **Design (Skid B):** the generator exhaust stack is typically the highest point and requires a dedicated air terminal, to keep a strike from jumping to the generator alternator instead.

## 2. Down Conductors

The electrically continuous Corten steel walls likely meet NFPA 780's (lower) thickness requirement for serving as a down-conductor path — a separate, less strict threshold than the air-terminal puncture requirement in Section 1, since down conductors don't need to resist localized strike puncture, only safely carry current to ground. Relying on painted, corrugated, and field-modified container walls for a mission-critical fault path still introduces real impedance/continuity risk, so:

- **Design:** route dedicated **Class I** (corrected from Class II, same basis as Section 1) braided copper or aluminum down conductors from the roof air terminals to the ground ring. Minimum two down conductors required per structure, located at diagonally opposite corners — standard NFPA 780 practice for redundant current paths.

## 3. Grounding System Integration

NFPA 780 strictly prohibits isolated lightning grounds.

- **Design:** lightning protection down conductors bond directly to the NEC 250 ground ring established in `grounding-basis.md`, at grade level, using the same listed bimetallic lugs or exothermic (Cadweld) connection method already specified there for the Corten shell bond — consistent methodology, not a separate connection standard.

## 4. Roof Interferences

- **Satellite uplink:** the Starlink/cellular antenna masts must sit within the air terminals' zone of protection to avoid a direct strike to the comms gear. **Flagged, not corrected — verify before locking:** this draft describes that zone using "the rolling sphere method" and a fixed "45-degree cone" as if they're the same thing. They're related but distinct: the rolling sphere method defines the protected zone using an actual sphere radius tied to the structure's protection class, while the 45° cone-of-protection is a separate, simpler method NFPA 780 permits for some structure types. Confirm which method actually applies at this structure height/class before using either to place the antenna masts.

---
Companion to `grounding-basis.md`, `electrical-schedules.md`, and `minicenter-fmea.html` (FMEA 2.5, which covers conducted surge only — this document is the direct-strike complement).
