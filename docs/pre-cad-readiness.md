# OCP Mini-Center — Pre-CAD Design Review & Readiness Checklist

Draft v0.1 — 2026-10-06. A thorough pass over the Basis of Design, FMEA, BOM, and RFI drafts, specifically asking: **what's actually missing before a real Revit concept model can be built**, not just "what's open" in the general checklist sense. Organized by subsystem. Companion to `minicenter-checklist.md`, which stays the item-level source of truth — this document is a targeted readiness gate for CAD specifically.

## Why this document exists

The checklist tracks dozens of open items across engineering, BOM, and business phases. Not all of them block starting a Revit model. This document separates **"blocks geometry"** from **"doesn't block geometry yet, but blocks calling the model final."**

## 1. Electrical Distribution

| Gap | Why it matters for Revit | Status |
|---|---|---|
| **One-line diagram + skeleton panel schedules** | Basis of Design Section 8/12 gave only block diagrams. A real electrical Revit model needs this before it needs geometry. | **RESOLVED 2026-10-06** — `docs/electrical-schedules.md`, hand-checked NEC math |
| **PDU-A/PDU-B named but unspecified** | No vendor, no physical footprint, no breaker/circuit count per rack whip. Can't place geometry for an envelope that doesn't exist yet. | Blocking |
| **RPP not in the design at all** | Never addressed in any document so far. Real open question: does a Remote Power Panel sit between PDU and rack whips (likely, if each OCP rack power shelf needs multiple branch circuits), or does the PDU's own distribution section do that job directly? This is an architecture question, not just a vendor one. | **New — needs a decision before the one-line can be finished** |
| **Grounding/bonding design** | NEC 250 — grounding electrode system, inter-skid EGC bonding, container shell bonding, interior halo grid. Code-required, not optional. | **RESOLVED 2026-10-06** — `docs/grounding-basis.md` |
| **Direct-strike lightning protection** | FMEA 2.5 covers conducted surge only (SPD) — direct strike to the container/skid structures (air terminals, down conductors, grounding ring) is separate, notable given the same FMEA entry flags elevated rural lightning exposure. | **RESOLVED 2026-10-07** — `docs/lightning-protection.md`. One sub-item flagged for verification, not blocking: confirm rolling-sphere vs. 45° cone-of-protection method before placing antenna masts (Section 4). |
| **Short-circuit/arc-flash study** | Switchgear, ATS, and generator breaker selection can't be finalized without a real fault-current study. | **Deliberately deferred, not blocking** — a real study needs actual generator/utility fault-contribution and cable impedance data that doesn't exist until RFI 1 (generator) returns, and ultimately also depends on site-specific utility fault data for grid-tied deployments. Calculating now would mean guessing the one input that actually matters. Proceed to massing with the 65kA SCCR as a stated assumption; revisit once real impedance data exists. |
| **Switchgear/ATS vendor unselected** | ASCO 7000 Series is explicitly flagged in the BOM as illustrative/unverified, not a real selection — no footprint exists yet. | RFI/selection-gated |

## 2. Mechanical / Cooling

| Gap | Why it matters | Status |
|---|---|---|
| **Skid B has no real layout** | Only a labeled block diagram exists. Generator and adiabatic cooler placement, clearances (combustion air intake, radiator discharge, acoustic enclosure service access), and exhaust routing aren't drawn. | Blocking |
| **No fuel system design** | If the generator ends up diesel (SG/MD600-class diesel variant), a sub-base fuel tank is standard for extended unmanned runtime — **not in the BOM, the weight tracker, or any layout right now.** Could materially change Skid B's weight and footprint once added. | **Missing entirely — add to scope** |
| **No makeup-water storage** | Site prep guide specifies a water line requirement (~230 gal/hr peak) but no on-site buffer tank for intermittent site water supply or short outages. | Open, not yet started |
| **Skid A plan view is stale** | Basis of Design Section 5's dimensioned plan view is explicitly flagged as the old 2-rack/260kW scale — Section 12 (current 4-rack/520kW) only has a schematic block diagram, never redrawn to scale. | Blocking |
| **Partition wall not dimensioned** | Locked as a spec (Section 12.1 — 3" IMP, Roxtec transits) but no actual drawn location within the container's 12.03m length, door swing clearance, or exact transit penetration points. | Blocking |

## 3. Structural

| Gap | Why it matters | Status |
|---|---|---|
| Generator + cooler + fuel tank weights | All three are RFI-gated or entirely missing (fuel tank) — blocks final Skid B structural/weight close-out. | RFI-gated / missing |
| Floor reinforcement sizing | Spreader-plate concept is closed as a *decision*, but no structural calc or actual plate dimensions exist yet. | Open |
| Umbilical corridor civil detail | Two-pad-plus-corridor is specified at a high level; no actual elevation/grade relationship between the two foundations or buried-vs-above-grade routing decision. | Open |

## 4. Controls / Comms

| Gap | Status |
|---|---|
| Edge gateway, cellular modem, satellite hardware all unselected — real products needed before placing enclosures/antennas in the model | Selection-gated |
| Leak-trip logic, skid-to-skid Modbus architecture, aux UPS sizing | **Already resolved** — doesn't block modeling, only procurement |

## 5. What Can Actually Start Now

- **Rough massing model**: container shell + rack/CDU block placement (Skid A), flatbed + generator/cooler block placement (Skid B) — using already-verified real envelope dimensions (OCP ORv3, Motivair MCDU-25)
- Locked connector locations at the inter-skid umbilical (Cam-Lok, Victaulic, PLC), even schematically
- Partition wall as a generic 3" IMP assembly volume, exact position TBD

## 6. Recommended Sequence

1. **Send the 3 drafted RFIs** (generator, Motivair, adiabatic cooler) — they're ready and sitting unsent.
2. **Run the Gemini cost/vendor prompt** (see `gemini-bom-cost-prompt.md`) in parallel for the vendor-TBD items — treat every answer as a lead to verify, same rule as everything else in this project.
3. **Resolve the RPP architecture question explicitly** — needed before the one-line diagram can be finished.
4. **Build a one-line diagram + skeleton panel schedule.** This is the actual gating document for a real Revit electrical model — more than the BOM itself. Worth running this the same disciplined way real intake projects get handled: panel schedule structure first, never bulk-guessing equipment names.
5. **Dimension Skid A's real 4-rack/2-CDU/switchgear/partition-wall plan** and Skid B's generator/cooler/fuel-tank layout.
6. **Then**: massing model now, with the above in progress; detailed model once RFI replies and vendor selections land.

---
Companion to `minicenter-checklist.md` (item-level source of truth), `minicenter-bom.html`, `minicenter-fmea.html`, and `gemini-bom-cost-prompt.md`.
