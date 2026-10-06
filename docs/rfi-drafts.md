# OCP Mini-Center — Vendor RFI Drafts

Two items in `minicenter-checklist.md` (Phase 1) are gated behind data that vendor marketing cutsheets don't publish — generator cold-start transient timing and the Motivair MCDU-25's ambient envelope. Both have already been searched directly against the public cutsheets and confirmed absent (see checklist history, including the 2026-09-29 rejected external claim). The only remaining path is a direct engineering RFI. Drafted 2026-09-29, ready to send as-is.

Scoped deliberately around this project's actual FMEA triggers (the 45-second ride-through window, the -40°C blackout case, the 5-40°C conservative assumption) rather than generic spec requests, so a vendor applications engineer has to answer with real numbers, not a brochure.

**Do not treat any reply to these as verified until the actual submittal/cutsheet/report is in hand and checked directly** — same rule as everything else in this project.

---

## RFI 1 — Generac Industrial Power (600kW class)

**Subject:** Engineering Submittal Request: 600kW Class (Diesel & NG) — Cold Start & Weight Specs

To the Generac Applications Engineering Team:

We are finalizing the FMEA and logistical weight budgets for a modular, split-skid data center deploying a 520kW (4-rack) continuous IT payload. Our operating envelope includes a -40°C minimum ambient. We need the following data to clear our 600kW-class generator selection:

1. **Transient Response & Start Timing:** We have a strict 45-second ride-through window before the GPUs thermally throttle. Can you provide a Power Design Pro transient response report verifying that a 600kW-class unit (both Diesel and Natural Gas options) with the extreme-cold weather package can crank, synchronize, and accept a 550kVA step-load in under 45 seconds at -40°C ambient?
2. **Auxiliary Power Draw:** To guarantee that start time, what is the total continuous auxiliary power draw (in kW) required to keep the block heaters, oil pan heaters, and battery warmers energized at -40°C?
3. **Physical Submittals:** Please provide the exact submittal drawings and wet weights for both a 600kW Diesel and 600kW Natural Gas unit, configured with a Level 2 acoustic enclosure and the extreme-cold weather package.

**Deliberately does not name a specific model (MD600/SG600 vs. any other SKU)** — let the vendor's own engineering team map the requirement to their current lineup, rather than us asserting a model number we haven't independently verified.

---

## RFI 2 — Motivair (MCDU-25)

**Subject:** Engineering RFI: MCDU-25 Ambient Operating Envelope & Cold-Start Limits

To the Motivair Engineering Team:

We are integrating two MCDU-25 units in an N+1 configuration inside a modular data center. The CDUs are physically isolated from the IT room via a structural IMP partition, meaning they sit in a dedicated facility-gear room. We need to formalize the climate-control limits for this room.

1. **Ambient Operating Envelope:** The public cutsheet does not list an ambient air temperature envelope for the MCDU-25 chassis. What is the absolute minimum and maximum allowable ambient room temperature for the onboard PLC, VFDs, and HMI? (We are currently assuming a standard 5°C to 40°C envelope for component safety.)
2. **Primary Fluid Thermal Shock:** In a total facility blackout at -40°C, the fluid in the exterior primary loop (running PG60) will drop well below freezing. When the facility restarts, is there a minimum primary-fluid temperature required *before* the CDU's modulating valve opens, to prevent thermal shock to the internal heat exchanger?

---

## What each RFI resolves, once answered

| RFI | Checklist item it closes | Currently blocking |
|---|---|---|
| Generac Q1/Q2 | Generator start-time claim (Phase 1, "STILL OPEN" note) | FMEA 2.1, the 45s ride-through assumption itself |
| Generac Q3 | Skid B weight tracker's generator line | Final road-legal weight claim for Skid B |
| Motivair Q1 | 3-tier Climate-Kit ambient assumption (currently 5-40°C, marked conservative/unverified) | Climate-kit heater/AC sizing, re-verification after the Chilldyne→Motivair pivot |
| Motivair Q2 | Bypass-valve/primary-supply-minimum spec (currently inherited from the CDU this replaced) | Cold-climate startup sequencing logic in the FMEA |
| Adiabatic cooler Q1-5 | Heat rejection device — real model/footprint/weight (Phase 1, currently placeholder) | Skid B weight tracker's final line, Skid B layout/road-legal claim |

---

## RFI 3 — EVAPCO / Güntner (Adiabatic Heat Rejection)

**Subject:** Engineering Submittal Request: 550kW Adiabatic Fluid Cooler Sizing & Footprint

To the Applications Engineering Team:

We are designing a split-skid modular data center and need to size an adiabatic V-coil fluid cooler (dry cooler with adiabatic pre-cooling pads) for our Mechanical Skid (Skid B). The unit will be mounted on a standard flatbed trailer, so physical length and operating weight are critical constraints.

Please run your selection software based on the following parameters and provide the exact model submittal:

1. **Thermal Load:** 550 kW heat rejection.
2. **Fluid:** 30% Propylene Glycol (PG30).
3. **Maximum Leaving Fluid Temperature:** The fluid returning to our CDU must strictly not exceed 35°C (95°F) at peak design conditions.
4. **Ambient Design Condition:** Phoenix, AZ (please use your own copy of the standard ASHRAE 0.4% design-day Dry-Bulb and Mean Coincident Wet-Bulb for station 722780 — we have an internal estimate but want your software's own sourced figure, not ours).
5. **Deliverables Required:**
   - Specific model number/selection.
   - Physical dimensions (L × W × H) and wet operating weight (kg).
   - Peak electrical draw (kW) for the EC fans at 100% speed.
   - Peak water consumption rate (GPM) during 100% adiabatic pad saturation on the Phoenix design day.

**Why this is the right RFI, not another estimate**: the first-principles airflow check (`minicenter_math.py: adiabatic_required_airflow_cfm()`, 2026-09-29) showed required CFM swings from ~97,000 to ~217,000 depending purely on an assumed air-side ΔT this project has no basis to pick — a >2x range that directly drives fan count and physical length. Rather than guess a ΔT (or accept a vendor-brochure-style number with no shown assumption, as happened and was rejected the same day), this RFI hands the vendor's selection software the real fixed inputs (load, fluid, max leaving temp, ambient) and lets it return the one number that's actually defensible: their own calculated selection.
