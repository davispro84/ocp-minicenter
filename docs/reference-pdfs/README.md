# OCP Mini-Center — Reference PDF Library

Primary-source documents gathered during this project's research, kept alongside the design docs so every citation in `minicenter-basis-of-design.html`, `minicenter-fmea.html`, `minicenter-checklist.md`, and `lib/minicenter_math.py` traces to an actual file in this repo, not just a claim about one.

**Copyright note:** these are vendor-published cutsheets/brochures and OCP's own published open specifications — kept here for reference and provenance, not redistribution for commercial use. OCP specs are explicitly published under the OCP CLA for this kind of use; vendor marketing/technical literature (Generac, ASCO, Chilldyne, Motivair, EVAPCO, Alfa Laval, Lu-Ve, Dow) remains that vendor's own copyrighted material.

## ocp-specs/

| File | What it is | Cited in |
|---|---|---|
| `Open Rack Base Specification Version 3_rev1.1_030524.pdf` | OCP Open Rack Base Spec V3, Rev 1.1 — rack physical envelope basis | `lib/minicenter_math.py` (RACK_WIDTH_MM etc.), Basis of Design §3 |
| `Open Rack Version Meta V3_rev1pt3_june032024.pdf` | OCP Open Rack Meta Frame V3 Spec, Rev 1.3 | Same — cross-checked rack geometry |
| `Open Rack V3 Blind Mate Manifold Specification Rev 1.0_review_april05_2024.pdf` | OCP BMQC manifold spec — fluid pressure/flow/valve basis | `minicenter_math.py` (OCP_MANIFOLD_* constants), checklist Phase 3 |
| `ORV3 Blind Mate Quick Connector Specification_Rev01_04June2024.pdf` | OCP BMQC connector spec | Same — positive-pressure cooling architecture decision |
| `OCP-Specification-Diablo 400  v0p5p2-2025-05-30.pdf` | OCP "Mt. Diablo" 800VDC bus spec, v0.5.2 — **the original Pod's DC bus basis**, not used by the Mini-Center post-pivot | Basis of Design §3, original 800vdc-ai-pod-automation repo |
| `diablo rack and power.pdf` | **"Diablo 400 Project: Rack and Power" v0.7.0 — a newer revision than v0.5.2 above.** Downloaded 2026-10-06, not yet reviewed or reconciled against this project's existing citations. Treat as unverified/unreviewed until checked directly. | Not yet cited — follow-up item |
| `OCP-Specification-Deschutes-final-2025-09-05.pdf` | OCP Project Deschutes — CDU reference design | Basis of Design, cited for CDU reference architecture |
| `OCP Open Data Center for AI Whitepaper FINAL.pdf` | OCP's own AI data center whitepaper — general architecture context | Background reading |

## vendor-cutsheets/

| File | What it is | Cited in |
|---|---|---|
| `CDU 2026 Motivair by SE.pdf` | **Motivair MCDU-25 cutsheet — the locked CDU.** Post-Schneider-Electric branding. | Basis of Design §3, BOM, FMEA 3.1/3.6 |
| `Chilldyne-CF-CDU300-Spec-Sheet-A.pdf`, `Chilldyne-CF-CDU300-Spec-SheetC.pdf`, `Chilldyne-Liquid-Cooling-Solutions-A.pdf` | Chilldyne CF-CDU300 — the CDU this project pivoted away from (negative-pressure, pre-pivot architecture) | Basis of Design §10 pivot history, kept for the reasoning trail |
| `117-01682-01-a-guide-to-glycols.pdf` | Dow's "A Guide to Glycols" — real freeze-point chart, verified source | checklist Phase 1 (PG25/PG30/PG60 fluid strategy) |
| `D1E-Indirect-Evaporative-Cooling-Systems-Adiabatic-50-250 kW.pdf`, `Brochure-Dry-Cooler-ENG_07.25_WEB.pdf`, `Lu-Ve-Air-Cooled-Condensers-2018.pdf`, `ahe00029en.pdf` (Alfa Laval AlfaBlue Junior DG), `DCB26MRKT_WEB_1.pdf`, `eco-Air-Condensers-Brochure-1100B-4.2.2019-web.pdf` (EVAPCO eco-Air), `Features-and-Applications-Guide-2018-web.pdf` | Adiabatic/dry-cooler vendor literature gathered while researching the Skid B heat rejection unit — all confirmed to gate real performance data behind selection software (see checklist Phase 1), which is why RFI 3 exists | RFI 3, Basis of Design §10 heat-rejection section |
| `Generac_350kW_MD350_Diesel_Generator_12.9L.pdf`, `0K7656A.pdf` (Generac SG/PG 350kW cutsheet) | Generac MD350/SG350 — the smaller unit actually checked directly against a real cutsheet (per the project's own history); the 600kW-class unit this project needs has never been downloaded and verified the same way | checklist Phase 1, RFI 1, verification-incidents.md |
| `asco7000series.pdf` | ASCO 7000 Series ATS — currently an illustrative/unverified BOM example, not a confirmed selection | BOM §1 |

## industry-background/

| File | What it is | Cited in |
|---|---|---|
| `Power Architecture Evolution in Data Centers.pdf` | General background reading on DC power architecture trends | Background |
| `nvidia-800-vdc-industry-alignment-white-paper.pdf` | NVIDIA's 800VDC industry alignment white paper — the real industry roadmap context behind the "how fast could this go 800VDC" conversation | Build-process retrospective, 800VDC readiness discussion |
| `NVIDIARe.pdf` | NVIDIA press release — Vera Rubin DSX AI Factory reference design + Omniverse DSX digital twin blueprint | Background on next-gen rack generation roadmap |

## conference/

| File | What it is |
|---|---|
| `ocp-summit-2026-schedule.pdf` | OCP Regional Summit schedule — source for the session-mapping exercise (which talks apply directly to this design, who's worth meeting) |

---
Companion to `minicenter-basis-of-design.html`, `minicenter-bom.html`, `minicenter-fmea.html`, `rfi-drafts.md`, and `verification-incidents.md`.
