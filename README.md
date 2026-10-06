# OCP Mini-Center

A truck-deployable, standard-interface (480VAC / positive-pressure OCP BMQC), climate-hardened AI compute module — split out from the `800vdc-ai-pod-automation` repo on 2026-09-29 once it diverged enough from that repo's original hyperscale-showcase Pod design to warrant its own project.

**Live site:** https://davispro84.github.io/ocp-minicenter/ — start there for the portfolio-facing case study and links into every document below.

**Start here for the engineering detail:** `docs/minicenter-checklist.md` — the living source of truth for what's decided, what's open, and what's next.

## What this is

The Primary Design tier: 4 OCP ORv3-class racks (520kW), N+1 Motivair MCDU-25 CDU pair, split into a Two-Skid Architecture (Compute container + Power/Mechanical flatbed) mated on-site via Cam-Lok, Victaulic, and Amphenol/MIL-spec connectors — deliberately mirroring already-proven industry (Crusoe-style) multi-skid deployment practice.

Target market: AI/GPU compute operators near stranded power (primary), stranded-power asset owners monetizing flare gas/curtailed renewables/decommissioned industrial sites (secondary), and a lower-density Standard Tier for rural/edge/telecom deployments.

## Repository layout

```
ocp-minicenter/
├── README.md
├── CLAUDE.md
├── docs/
│   ├── index.html                        # live site homepage — portfolio case study
│   ├── minicenter-checklist.md           # living task tracker — item-level source of truth
│   ├── build-process-retrospective.html  # the AI-assisted engineering process, timeline + lessons
│   ├── minicenter-project-overview.html  # architecture, customer base, phase-by-phase status
│   ├── minicenter-basis-of-design.html   # the architecture, with real diagrams
│   ├── minicenter-fmea.html              # failure modes, scored, with real mitigations
│   ├── minicenter-bom.html               # bill of materials — locked/RFI-gated/example status per line
│   ├── minicenter-tcs-loop.html          # the cooling loop schematic
│   ├── minicenter-guide.html             # plain-language walkthrough of the whole project
│   ├── minicenter-site-prep-guide.html   # customer-facing civil/electrical/mechanical requirements
│   ├── minicenter-executive-summary.html # customer-facing commercial pitch memo
│   ├── minicenter-competitive-analysis.md# positioning vs. Vertiv/Schneider, target buyer profiles
│   ├── verification-incidents.md         # log of fabricated/stale AI claims caught and rejected
│   ├── rfi-drafts.md                     # ready-to-send vendor RFIs for gated data
│   └── cad-download-prompts.md           # research prompts for real vendor CAD
└── lib/
    └── minicenter_math.py                # pure-Python engineering calcs, zero dependencies
```

## Relationship to the original repo

This project shares the original repo's verified OCP rack geometry and BMQC/manifold citations (both are real, both still apply here), but does **not** share its Diablo 400 800VDC bus or Chilldyne negative-pressure CDU — this project pivoted to standard 480VAC and OCP BMQC-compliant positive-pressure cooling specifically so real commercial OEM AI hardware (GB200 NVL72-class) can plug in without modification. See `lib/minicenter_math.py`'s module docstring for the full architecture rationale.

The original repo (`800vdc-ai-pod-automation`) keeps its Diablo 400/800VDC design as a deliberate hyperscale-architecture showcase — that's a different, still-valid project, not superseded by this one.
