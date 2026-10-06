# OCP Mini-Center — Vendor RFI Drafts

Three items are gated behind data that vendor marketing cutsheets don't publish — generator cold-start transient timing, the Motivair MCDU-25's ambient envelope, and the adiabatic cooler's real model/footprint/weight. All have been searched directly against the public cutsheets and confirmed absent (see checklist history, including the 2026-09-29 rejected external claim). The only remaining path is a direct engineering RFI.

Originally drafted 2026-09-29. **Substantially revised 2026-10-06** after a vendor-perspective review — see "Revision log" at the bottom for what changed and why. These are now send-ready.

**Do not treat any reply to these as verified until the actual submittal/cutsheet/report is in hand and checked directly** — same rule as everything else in this project.

---

## Before sending — read this first

**1. These go out from a personal email account, as a personal project.**

This is a personal design study. It is not an Apple project, and nothing sent to a vendor may imply otherwise. A modular-data-center inquiry arriving from an Apple domain gets escalated as a live Apple opportunity within a day — which is a problem for the vendor (false pipeline), a problem internally, and not what this project is.

Concretely:
- Personal email address. Personal signature. No employer, no title.
- **Do not invent a company name or domain to look more legitimate.** That turns an honest ask into a misrepresentation and is far worse than being an individual if it ever surfaces.
- Do not imply unit volumes, a budget, or a procurement timeline. There aren't any.

**2. Go through the rep, not the factory.**

Generac Industrial sells through authorized industrial distributors; EVAPCO sells exclusively through manufacturer's reps; Güntner routes through regional sales. A cold email to a generic "applications engineering" address gets forwarded to a local rep anyway, minus a week. **Motivair was acquired by Schneider Electric in Dec 2024** — verify the current contact path before sending to a legacy address.

**3. Everything asked for here is free pre-sales work**, with one asterisk: Generac's Power Design Pro is distributor-operated, and the run itself is free, but a *certified or witnessed* transient test is not. RFI 1 states that distinction explicitly. Keep it in.

**4. Realistic expectations.** The honest disclosure will cost some response rate. RFI 2 is most likely to get a full answer (four questions, minutes of work). RFI 3 is medium — reps run selection software constantly and modular data centers are a category they want exposure to. RFI 1 is hardest, which is why its questions are ordered cheapest-first: questions 1-3 answered with silence on 4 would still close the Skid B weight gap. If Generac goes quiet on the transient question, the fallback is a *different distributor*, not another email to the same one.

---

## The disclosure block

Opens all three emails, verbatim. The technical content carries the credibility — a rep reading "ISO 8528-5 single-step acceptance" and "mean coincident wet bulb" knows inside ten seconds this isn't a hobbyist, so the opener doesn't need to oversell.

> I should be upfront about what this is: I'm an independent engineer developing a modular data center reference design as a personal project. This is not a corporate procurement inquiry — there's no company behind it, no budget allocated, and no purchase order pending. I work professionally in data center design, but this project is entirely my own and unaffiliated with my employer.
>
> I'm asking because the design has reached a point where two or three numbers that aren't in the public literature are blocking further work, and I'd rather get them right than estimate. I understand completely if this doesn't warrant your engineering time — but if any of the below is quick to answer, it would genuinely help, and I'm happy to work around your schedule.

Saying *unaffiliated with my employer* up front is deliberate and protective: if a rep looks you up later, you drew the line yourself rather than appearing to have omitted it. If you'd rather not reference professional work at all, cut that one sentence — the first line stands on its own.

**If a rep asks who you're with:** "It's an independent project of mine, not affiliated with any employer. I'm doing the design to a professional standard, and if it ever became real I'd route procurement through whoever's appropriate at the time."

---

## Web form cover notes

Most of these go in through a "How Can We Help?" contact form before the full RFI ever reaches a person. Keep these to 2-3 sentences so it routes to technical/applications support rather than a sales queue:

- **Generac / Industrial Power Systems:** "Submitting an early-stage technical inquiry regarding 600kW standby generator packaging for an off-grid modular data container concept. Looking to confirm published typical dry/wet weight ranges, physical enclosure dimensions, and standby/prime rating guidance to bound preliminary structural and logistics planning."
- **Motivair Applications Engineering (verify current routing post-Schneider acquisition first):** "Technical inquiry regarding the MCDU-25 in-row CDU for a conceptual modular deployment. Seeking clarification on the published ambient air operating temperature envelope and primary fluid supply limits to finalize HVAC and cold-climate startup logic in a partitioned equipment container."
- **EVAPCO / Güntner (Adiabatic Fluid Coolers):** "Early-stage design inquiry for a flatbed-mounted adiabatic fluid cooler rejecting ~550kW (30% PG, 45°C entering/≤35°C leaving fluid). Looking for a preliminary selection, footprint, and wet operating weight range, plus confirmation of the ASHRAE design-day figures your software uses for Phoenix."

---

## RFI 1 — Generac (via authorized industrial distributor)

**Subject:** Independent design study — 600kW-class genset submittals and cold-start data

*[disclosure block]*

**Design basis**

- Electrical: 480V, 3-phase, 60Hz (277/480Y)
- Continuous facility load: **~575 kW** — 520 kW IT payload, ~30 kW mechanical (CDU pumps + adiabatic cooler EC fans, estimated), 5-8 kW climate conditioning, ~15 kW lighting/controls/losses
- Ambient design envelope: **-40°C to +48°C**
- Site elevation: up to ~1,000 m
- Two site classes under study: grid-tied (genset as standby) and off-grid (genset as prime mover)
- Load profile: IT load sits behind rack-level PSUs/BBUs; mechanical load is VFD- and EC-fan-driven. I don't believe the facility presents a true block load — happy to be told what step profile you'd want confirmed.

**Questions, roughly in order of how much of your time they'd cost**

1. **Published submittals.** Submittal drawings and wet weights for a 600kW-class diesel and natural gas unit with a Level 2 acoustic enclosure and extreme-cold package — plus a **1,000-gallon sub-base fuel tank** option and its weight (sized for ~22-24hr runtime at full load, which is the deliberate ceiling for this design — sites needing longer unmanned runtime get an external bulk supply on a separate pad rather than a bigger integrated tank). If a 1,500gal option is trivially the same answer, happy to see that too, but 1,000gal is the one I need. If these are just existing PDFs, that alone would be a real help; transport weight is my tightest constraint.
2. **Rating and model selection.** Against ~575 kW continuous, which units cover this at a **standby** rating, and which at **prime**? I've deliberately not named a model — I'd rather your team map the requirement to the current catalog than have me assert a SKU I haven't verified.
3. **Cold-weather auxiliary load.** Total continuous auxiliary draw (kW) to hold block heaters, oil pan heaters, and battery warmers at -40°C. Related: if Tier 4 Final applies, how is DEF freezing handled at that ambient, and does SCR warm-up constrain start timing?
4. **The bigger ask — start and load acceptance at -40°C.** The design has a 45-second ride-through window before IT hardware throttles. If it's feasible, a Power Design Pro output showing time from start signal to rated voltage and frequency, and maximum single-step load acceptance (kVA and % of rating) with recovery time per ISO 8528-5, at -40°C with the cold package — for both diesel and NG. I'd expect the NG variant's step capability to be materially below diesel's, and a real number for it is the single thing I'm most missing. To be clear, I'm asking for the software output, not a certified or witnessed test. I know this one is a genuine time cost, so treat it as optional against the first three.

---

## RFI 2 — Motivair (verify Schneider Electric routing first)

**Subject:** Independent design study — MCDU-25 ambient envelope and cold-start limits

*[disclosure block]*

The configuration integrates two MCDU-25 units in N+1. The CDUs sit behind a structural IMP partition in a dedicated facility-gear room, separate from the IT space, and I'm trying to formalize that room's climate-control limits and the cold-start sequencing.

Four questions, none of which I've been able to answer from the public documentation:

1. **Ambient operating envelope.** The cutsheet doesn't list an ambient air temperature range for the chassis. What are the minimum and maximum allowable ambient room temperatures for the onboard PLC, VFDs, and HMI? I'm currently carrying a 5-40°C assumption as a conservative placeholder for off-the-shelf industrial electronics — if that's wrong in either direction, it changes my heater and AC sizing.
2. **Primary supply temperature limits.** What are the maximum and minimum allowable primary supply fluid temperatures for the MCDU-25? I have figures in my model inherited from a different CDU and would like to replace them with yours.
3. **Cold-start pumpability.** The exterior primary loop runs PG60 for sites down to -40°C ambient. PG60 protects against freezing to roughly -48°C, but its viscosity at -40°C is very high. What is the maximum fluid viscosity the primary pump can start against, and is a pre-warm or staged-start sequence required before full flow?
4. **Thermal shock on restart.** Following a total facility blackout at -40°C, is there a minimum primary-fluid temperature that must be reached *before* the modulating valve opens, to protect the internal heat exchanger from thermal shock?

---

## RFI 3 — EVAPCO / Güntner (send separately to each, via rep)

**Subject:** Independent design study — 550kW adiabatic fluid cooler selection, Phoenix design day

*[disclosure block]*

I need an adiabatic V-coil fluid cooler (dry cooler with adiabatic pre-cooling) sized for the mechanical skid of a split-skid modular data center. The unit ships on a standard flatbed alongside a 600kW-class generator, so length and operating weight are hard constraints rather than preferences.

**Selection inputs**

| Parameter | Value |
|---|---|
| Heat rejection | 550 kW |
| Fluid | 30% propylene glycol (PG30) |
| Entering fluid temp | 45°C |
| Leaving fluid temp | ≤35°C (10K ΔT, ≈14 L/s / 225 GPM — please confirm) |
| Ambient design | ASHRAE 0.4% for Phoenix Sky Harbor, station 722780 |
| Site elevation | ~340 m |
| Electrical | 480V, 3-phase, 60Hz |
| Max length | ~8.0 m including service clearance |
| Target operating weight | ≤4,500 kg (absolute ceiling ~7,400 kg) |

Please state the dry-bulb and mean coincident wet-bulb your software used, so I can carry a sourced figure rather than my own estimate.

If running a second case isn't much extra work, I'd be grateful for selections at both ≤35°C and ≤40°C leaving fluid. The downstream CDU's actual limit is 45°C, so my 35°C target carries deliberate margin, and I'd like to see what that margin costs in length and weight. If that's too much, the ≤35°C case alone is the one I need.

**Deliverables**

1. Model number and selection summary.
2. Physical dimensions (L × W × H) and wet operating weight (kg).
3. Peak electrical draw (kW), EC fans at 100%.
4. Peak water consumption (GPM) at full adiabatic pad saturation on the design day.
5. Fluid-side pressure drop at the selected flow.
6. **Dry-mode performance:** leaving fluid temperature with pads dry at design ambient, and the unit's behavior on loss of adiabatic water supply. I expect dry mode can't hold 35°C at Phoenix conditions — I need to know what it *does* hold, for the failure analysis.

**One further question:** the same product also deploys to cold-climate sites running PG60 on the primary loop. If a single model can cover both fluids, please note any derate or pressure-drop penalty on PG60; if it realistically needs a different selection, I'd like to know that now.

---

## What each RFI resolves, once answered

Question numbers below match the **revised** drafts above (RFI 1 was reordered cheapest-ask-first on 2026-10-06 — the old numbering no longer applies).

| RFI | Checklist item it closes | Currently blocking |
|---|---|---|
| Generac Q1 | Skid B weight tracker's generator line + the missing fuel-tank row | Final road-legal weight claim for Skid B — now the tightest margin in the project (~2,950kg) |
| Generac Q2 | Generator rating class (standby vs. prime) — **new, surfaced by the 2026-10-06 review** | Whether a 600kW-class unit is adequate at all against the ~575kW real load total |
| Generac Q3 | Cold-weather aux draw; Tier 4F/DEF cold-start interaction (**new**) | Electrical budget; whether aftertreatment constrains the 45s window |
| Generac Q4 | Generator start-time claim (Phase 1, "STILL OPEN" note) | FMEA 2.1, the 45s ride-through assumption itself |
| Motivair Q1 | 3-tier Climate-Kit ambient assumption (currently 5-40°C, conservative/unverified) | Climate-kit heater/AC sizing, re-verification after the Chilldyne→Motivair pivot |
| Motivair Q2 | Max/min primary supply temps — currently inherited Chilldyne figures (45°C / 2°C) | Bypass-valve logic; the adiabatic cooler's own leaving-temp target |
| Motivair Q3 | PG60 cold-start pumpability — **new, surfaced by the 2026-10-06 review** | Whether the -40°C cold-start case fails on pump capability before it fails on thermal shock |
| Motivair Q4 | Bypass-valve/primary-supply-minimum spec | Cold-climate startup sequencing logic in the FMEA |
| Cooler D1-6 | Heat rejection device — real model/footprint/weight (Phase 1, currently placeholder) | Skid B weight tracker's final line, Skid B layout/road-legal claim |
| Cooler D6 | Dry-mode fallback behavior — **new** | An unwritten FMEA line: what the unit holds on loss of adiabatic water |

---

## Revision log — 2026-10-06 vendor-perspective review

Reviewed the 2026-09-29 drafts specifically for whether a vendor applications engineer would find them credible and answerable. **Overall finding: the drafts were not outlandish.** The architecture (520kW across 4 racks, 130kW/rack, liquid-cooled, split-skid, stranded-power siting) is a current and recognizable design point, and the questions were specific enough to be answerable. The problems were process and precision, not plausibility.

**Process fixes**

| Fix | Reason |
|---|---|
| Added the personal-project disclosure block to all three | The drafts identified nobody and no stage — the single most likely reason an RFI gets filed rather than answered. Also closes off any implication of employer backing. |
| Routed through reps/distributors, not factory applications teams | How this equipment is actually sold; a generic cold email gets forwarded anyway. |
| Flagged the Motivair→Schneider acquisition (Dec 2024) | Legacy contact path may be stale. |
| Stated "PDP output, not a certified test" | Keeps the heaviest ask unambiguously free. |
| Removed implied volume/timeline language | An earlier revision said "one genset per deployed unit, decision window of X" — that implies a funded program and is the same false-impression problem as the email domain, just quieter. |
| Reordered RFI 1 cheapest-ask-first | With no purchasing power, question order is tactical. Submittals are existing PDFs; the PDP run is real engineering time. A partial reply still closes the weight gap. |

**Technical fixes**

| Fix | Where | Reason |
|---|---|---|
| Replaced the asserted "600kW class" with a stated load total + "which model?" | RFI 1 Q2 | ~575kW is ~95% of a 600kW **standby** rating and over a **prime** rating. The off-grid stranded-gas site class is prime duty. An applications engineer would have caught this immediately. |
| Asked for standby **and** prime ratings | RFI 1 Q2 | Two site classes genuinely exist. Routine to ask — it's two columns on the same datasheet. |
| "Crank, synchronize, and accept" → "reach rated voltage and frequency" | RFI 1 Q4 | *Synchronize* means paralleling to a live source, implying entirely different switchgear, protective relaying, and a utility interconnection agreement. Wrong word. |
| NG step-load reframed from an assertion to an open question | RFI 1 Q4 | 550kVA is ~73% of a 600kW unit at 0.8PF. Diesel handles that routinely; **NG typically accepts only 25-50% per step** due to fuel-air mixing and turbo lag. Asking "can your NG unit take 550kVA in one step" as if expecting yes was the one line that would have read as naive. |
| Added the load-profile caveat | RFI 1 design basis | IT load behind rack PSUs/BBUs doesn't present a block load, and EC/VFD mechanical load ramps. The vendor would have asked; better to pre-empt. |
| Added Tier 4 Final / DEF freezing | RFI 1 Q3 | **DEF freezes around -11°C.** At -40°C this needs heated tank and lines, and SCR warm-up may constrain the start-time answer. Raising it signals familiarity; missing it signals the opposite. |
| Added sub-base fuel tank weights to the submittal ask | RFI 1 Q1 | Already a live, unsourced line in the weight tracker. Get it in the same request. |
| **Removed the flare/wellhead-gas question entirely** | RFI 1 | The most dissonant item in the original. Q1-Q3 described a -40°C cold-climate unit, then Q4 introduced sour wellhead gas — making the project read as unscoped. It's also a **different product family** (Cat G3500 / Waukesha / INNIO Jenbacher territory, not standard pipeline-spec Generac), and not answerable as posed, since H2S tolerance requires our gas chromatograph analysis first. **See follow-up item below.** |
| Added max/min primary supply temps | RFI 2 Q2 | Replaces the inherited Chilldyne 45°C / 2°C figures the checklist already flags as needing re-verification. Free to ask, same email. |
| Added PG60 viscosity/pumpability | RFI 2 Q3 | **Freeze protection ≠ pumpability.** PG60 protects to ~-48°C, but at -40°C its viscosity is extreme — the likelier cold-start failure is the pump failing to establish flow, cavitating, or overloading, not thermal shock to the HX. This is the better version of the original Q2. |
| **Added flow rate / ΔT** | RFI 3 | The original gave load and leaving temp — two of the three variables a selection needs. **Every vendor would have replied asking for flow before running anything.** Highest-value single fix in the document. Now specified as 45°C entering / ≤35°C leaving (10K ΔT ≈ 14 L/s), self-consistent with the CDU's 45°C max primary supply. |
| Added dual 35°C / 40°C case | RFI 3 | The CDU's real limit is 45°C and our own first-principles check put Phoenix adiabatic at ~29-32°C, so the 35°C target embeds ~10°C of hidden conservatism. Approach temperature drives coil size, fan count, length and weight — i.e. it works directly against Skid B's binding constraint. Asking for both buys the trade curve. |
| Added length and weight ceilings | RFI 3 | The original said length and weight were "critical," then gave no numbers. Both derived from the Skid B tracker: ~8.0m remaining deck after a ~5.8m genset on a 48ft flatbed; ≤4,500kg target against a ~7,400kg ceiling. **Both derived, not verified — recheck before sending.** |
| Added dry-mode / water-failure deliverable | RFI 3 D6 | At Phoenix 0.4% the unit is entirely dependent on the pads; a dry coil physically cannot take fluid below ambient dry-bulb (~43-44°C), which our own checklist already proved. Asking costs nothing and produces an FMEA line. |
| Rewrote the ASHRAE paragraph | RFI 3 | The original ("we have an internal estimate but want your software's own sourced figure, not ours") had correct epistemics but read as distrustful to a stranger. Asking them to *state the values used* gets the identical result without the meta-commentary. |
| Added the PG60 cold-climate variant question | RFI 3 | The original asked only for the hot-climate PG30 case, but the same product ships to Bakken on PG60, which materially changes fluid-side pressure drop. |

**Checked and found fine:** the PG30/PG60 split across RFI 2 and RFI 3 looks like a contradiction on first read but is the deliberate two-tier fluid strategy (`minicenter_math.py:145-146` — PG30 temperate/hot, PG60 extreme cold). Internally consistent. The only gap was that neither RFI acknowledged the other tier existed; RFI 3 now does.

**Also noted:** the 45-second ride-through window is far looser than NFPA 110 Level 1 Type 10 (10 seconds to accept load). The diesel case is comfortably solved. The real risk concentrates in the NG variant and the -40°C aftertreatment case, which is where the revised RFI 1 aims.

**Internal notes removed from the email bodies:** the original "deliberately does not name a specific model" and "why this is the right RFI, not another estimate" asides were correct reasoning but are project-log material, not vendor-facing text. The behavior is now built into how the questions are phrased. For the record, the second one's rationale still stands: `minicenter_math.py: adiabatic_required_airflow_cfm()` showed required CFM swinging from ~97,000 to ~217,000 depending purely on an assumed air-side ΔT this project has no basis to pick — a >2x range driving fan count and physical length. Withholding our ΔT and letting the selection software return its own is the whole point of RFI 3's structure.

---

## Follow-up items generated by this review

- [ ] **Flare/wellhead-gas inquiry — now a separate, later conversation, NOT part of RFI 1.** Reframe as a short standalone email: *"We have a site class running field gas rather than pipeline-spec — do you have an offering, or should we be looking at a different engine family?"* Expect the honest answer to point away from Generac toward specialist field-gas packagers. **Checklist Phase 2 item dated 2026-10-06 currently says "Add to RFI 1" — that instruction is now stale and should be updated to reference this item instead.**
- [ ] **Resolve standby vs. prime as a design decision, not just an RFI question.** RFI 1 Q2 asks the vendor, but the underlying choice is ours and depends on grid-tied vs. off-grid siting. The ~575kW load total against a 600kW-class unit is tight on standby and insufficient on prime — this may force an 800kW-class unit for the off-grid tier, with knock-on weight implications for Skid B.
- [ ] **Verify the RFI 3 dimensional and weight ceilings before sending** (~8.0m length, ≤4,500kg target / ~7,400kg ceiling). Both were derived from the Skid B tracker during this review, not independently checked.
- [ ] **Confirm the ~575kW facility load total.** Assembled during this review from the checklist's own figures (520kW IT + ~8.8kW adiabatic fans + 5-8kW climate kit + estimated CDU pump load + estimated losses). The CDU pump draw in particular is an estimate — Motivair publishes no figure, and RFI 2 doesn't currently ask for it. Consider adding.
