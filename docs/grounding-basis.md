# Basis of Design: Grounding & Bonding (NEC 250)

Draft v0.1 — 2026-10-06. Companion document to `electrical-schedules.md` and `minicenter-fmea.html`. Defines the grounding electrode system and bonding requirements for the 520kW Skid A/B architecture — closes the "no grounding/bonding design" gap flagged in `pre-cad-readiness.md`.

**Applying NEC 250 to a two-skid modular deployment is itself an engineering judgment call**, not a literal one-to-one match — the code was written for conventional buildings/structures, not ISO containers and flatbed-mounted gensets joined by a field umbilical. Where this document applies code intent rather than a literally on-point section (e.g., Section 3's structural-metal bonding), that's called out explicitly rather than asserted as a direct citation.

## 1. Grounding Electrode System (Earth Connection)

Because Skid A (container) and Skid B (generator) sit on separate concrete pads, they require a coordinated grounding electrode system to provide a safe path for fault currents and stabilize voltage to ground.

- **Design (Skid A):** A ground ring encircling the Skid A pad per NEC 250.52(A)(4). Minimum 2 AWG bare copper (code minimum — 4/0 AWG recommended as real data-center industry practice, not a code requirement) buried at a minimum depth of 30 inches (NEC 250.53(F)), supplemented by driven 8-foot copper-clad ground rods at the corners (NEC 250.52(A)(5)).
- **Design (Skid B):** Driven ground rods tied to the generator frame and alternator ground lug, sized per the generator manufacturer's submittal once a real unit is selected (RFI 1-gated).

## 2. Inter-Skid Umbilical Bonding

When the ATS switches to generator power, Skid A and Skid B operate as a single electrical system.

- **Design:** The 10th cable in the Series 16 Cam-Lok bundle serves as the Equipment Grounding Conductor (EGC) — consistent with the corrected 10-cable count in `electrical-schedules.md` (3 phases × 3 parallel + 1 un-paralleled ground, no neutral).
- **Sizing:** Per NEC Table 250.122, sized to the 1200A main overcurrent device — minimum **3/0 AWG copper EGC**. Matches the figure independently verified earlier for this same cable bundle.

## 3. Container Shell Bonding (The Faraday Envelope)

The 40ft Corten steel shipping container acts as a massive conductive envelope and must be bonded to the grounding electrode system — applying the engineering *intent* of NEC 250.104(C) (structural metal bonding), not a literal citation written for shipping containers.

- **Metallurgical constraint (galvanic corrosion):** Direct welding of copper to Corten steel is prohibited — poor copper-to-steel metallurgical fusion, and more importantly, direct copper contact sets up galvanic corrosion that degrades Corten's protective oxide layer over years of outdoor exposure.
- **Execution:** Weld a steel or stainless-steel mounting boss to the lower container rails at opposite corners (steel-to-steel, normal welding practice). Attach 4/0 AWG copper bonding jumpers to these bosses using **listed bimetallic lugs or an exothermic (Cadweld) connection** rated for dissimilar metals — never bare copper fused directly to the Corten shell.

## 4. Interior IT and Mechanical Bonding (Halo System)

Inside the container, all non-current-carrying conductive metal must bond back to the main ground bus inside `SWBD-1`.

- **General halo grid:** A bare copper halo ground ring runs along the interior perimeter (cable tray or under-floor), bonding the raised floor pedestals and cable tray sections. 6 AWG is a defensible minimum here since this grid isn't tied to one specific circuit's overcurrent device.
- **Equipment jumpers (rack/CDU-specific — do not use the 6 AWG halo figure here):** Jumpers from the halo to the ORv3 rack frames and Motivair CDU chassis must be sized per NEC Table 250.122 based on their actual supply circuit's overcurrent device, not the general halo figure.
  - *Rack/CDU feeders:* supplied by 225A trip branch breakers (`electrical-schedules.md`, PDU schedule).
  - *Minimum size:* Table 250.122's 201-300A bracket requires **4 AWG minimum** (41,740 cmil) — 6 AWG is undersized here and must not be used for these specific jumpers.
  - *Proportional upsizing — RESOLVED 2026-10-07, step to 2 AWG:* per NEC 250.122(B), because the rack branch phase conductors were upsized to 4/0 AWG Cu (211,600 cmil) from the 3/0 AWG base (167,800 cmil), the ratio is 211,600/167,800 = 1.261. Applied to the 4 AWG base EGC: 41,740 cmil × 1.261 = 52,634 cmil required. 3 AWG (52,620 cmil) misses this by 14 cmil — not close enough to round down. **Minimum size is 2 AWG copper (66,360 cmil)** for the rack and CDU equipment bonding jumpers specifically.

---
Companion to `electrical-schedules.md`, `minicenter-fmea.html`, and `pre-cad-readiness.md`.
