# OCP Mini-Center — Project Context for Claude Code

Read `docs/minicenter-checklist.md` first, every session — it's the live source of truth for what's decided, open, and next. This file is just orientation.

## What this project is

A truck-deployable AI compute module: 4 OCP ORv3-class racks (520kW), N+1 Motivair MCDU-25 CDU pair, standard 480VAC power (no DC bus — commercial OEM AI racks like GB200 NVL72-class do their own AC/DC conversion internally), standard OCP BMQC-compliant positive-pressure cooling (not the negative-pressure/vacuum architecture this design started with). Split into a **Two-Skid Architecture**: Skid A (40ft High-Cube container — compute, CDUs, 1200A switchgear) and Skid B (standard flatbed — 600kW-class generator + 550kW adiabatic heat rejection unit), mated on-site via Cam-Lok power cables, 3" Victaulic fluid couplings, and an Amphenol/MIL-spec multi-pin PLC connector.

## Relationship to the other repo

Split out of `/Users/benjamindavis/Documents/800vdc-ai-pod-automation` on 2026-09-29. That repo keeps its original Diablo 400/800VDC/Chilldyne design as a deliberate hyperscale-architecture showcase — a different, still-valid project, not superseded. This project shares only the real, verified OCP rack geometry and BMQC/manifold citations with that repo; everything else diverged.

## Working style established on this project — carry it forward

- **Verify every vendor/technical claim against a primary source** (actual downloaded PDF, checked directly — `pdftotext`/rendered pages, not a description of one) before it goes in a document. This applies to claims from *any* source, including other AI tools — high confidence and specific-sounding numbers are not evidence. **This is a recurring pattern, not a one-off**: six separate fabricated or stale technical claims were caught and rejected in a single working session on 2026-09-29 alone (a fabricated generator spec, an unsourced "live" ASHRAE lookup, vendor-brochure-style airflow numbers, a rejected weight figure resurfacing in a later doc, a delivery-timeline conflation, and an attempt to swap out the locked CDU vendor entirely with a fabricated product). Full log: `docs/verification-incidents.md`. Treat any claim of "I verified," "I pulled the real data," or "I searched" from an outside AI tool as a lead, never a fact, until the actual source document is produced and checked in this repo's own session.
- **Distinguish verified facts from conservative assumptions from placeholders explicitly** in every document — don't let an estimate quietly read as a fact.
- **When a vendor gates real numbers behind selection software/quotes**, don't treat that as a dead end — run the first-principles physics/engineering estimate instead (this project has done this successfully for adiabatic cooling performance, water consumption, fan power, and structural sizing).
- **Bound claims to a realistic, defensible scope** rather than an impressive-sounding unbounded one — e.g., the operating envelope is explicitly -40°C to +48°C (matched to realistic stranded-power-adjacent geography), not "works anywhere on Earth."

## Repository layout

```
ocp-minicenter/
├── README.md
├── docs/
│   ├── minicenter-checklist.md          # START HERE every session
│   ├── minicenter-project-overview.html # one-page rollup: architecture, customer base, phase-by-phase status
│   ├── minicenter-basis-of-design.html  # architecture + real diagrams
│   ├── minicenter-fmea.html             # failure modes, scored, real mitigations
│   ├── minicenter-bom.html              # bill of materials — locked/RFI-gated/example status per line
│   ├── minicenter-executive-summary.html # customer-facing commercial pitch memo
│   ├── minicenter-competitive-analysis.md # positioning vs. Vertiv/Schneider, target buyer profiles
│   ├── minicenter-tcs-loop.html         # cooling loop schematic
│   ├── minicenter-guide.html            # plain-language walkthrough
│   ├── minicenter-site-prep-guide.html  # customer-facing site requirements
│   ├── rfi-drafts.md                    # ready-to-send vendor RFIs for gated data (generator, CDU, adiabatic cooler)
│   ├── verification-incidents.md        # log of fabricated/stale claims caught and rejected — the receipts for the methodology above
│   └── cad-download-prompts.md          # research prompts for real vendor CAD
└── lib/
    └── minicenter_math.py               # pure-Python engineering calcs, zero dependencies
```

## Current status (2026-09-29)

Two-skid architecture and controls/leak logic are locked. Site prep guide exists. Open items live in the checklist — check there before assuming anything is either done or still open.
