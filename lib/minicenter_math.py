# -*- coding: utf-8 -*-
"""Pure-Python engineering calculations for the OCP Mini-Center.

Split out from the original 800vdc-ai-pod-automation repo's engineering_math.py
on 2026-09-29, once the Mini-Center diverged enough from that repo's original
4-rack/800VDC hyperscale-showcase Pod to warrant its own project. This file
carries forward only the constants/functions the Mini-Center actually uses;
everything specific to the Diablo 400 800VDC bus, the Chilldyne negative-
pressure CDU, and the original Pod's overhead busway lives in the OTHER
repo and was deliberately NOT copied here -- see that repo's CLAUDE.md /
engineering_math.py for the Pod's own (still-valid, unrelated) design basis.

Standards referenced (see docs/minicenter-basis-of-design.html and
docs/minicenter-fmea.html for the full citation ledger and verification
history -- this docstring is a summary, not the primary record):
  - OCP "Open Rack Base Specification Version 3" Rev 1.1, 05MAR2024 and
    "Open Rack Meta Frame V3 Specification" Rev 1.3, 03JUN2024 (Meta/Google,
    OCP CLA) -- rack physical envelope (RACK_WIDTH_MM etc. below). Verified.
  - OCP "Open Rack V3 Blind Mate Manifold Specification" Rev 1.0 and
    "Blind Mate Quick Connector Specification (BMQC)" Rev 01 (Meta/Parker/
    nVent/CoolIT/Danfoss/CEJN, OWF CLA 1.0) -- the Mini-Center's cooling
    loop is standard OCP BMQC-compliant POSITIVE pressure (architecture
    pivot, 2026-09-28/29 -- see MINICENTER_CDU_* section below for why).
  - Motivair MCDU-25 cutsheet -- real vendor document, verified directly
    (dimensions, capacity, FLA all checked; ambient envelope NOT published
    anywhere, held as a conservative assumption, see MINICENTER_CDU_* notes).
  - NFPA 70 (NEC) 210.19(A)(1) -- 125% continuous-load sizing factor.

ARCHITECTURE SUMMARY (why this looks the way it does):
  The Mini-Center targets commercial OEM AI racks (e.g. NVIDIA GB200
  NVL72-class), which take standard AC input and do their own AC/DC
  conversion inside the rack's own power shelves -- so this project never
  produces DC at all. No sidecar rectifier, no DC bus voltage constants.
  Cooling is a standard OCP BMQC-compliant POSITIVE-pressure CDU (Motivair
  MCDU-25), not the negative-pressure Chilldyne unit this design started
  with -- real OEM AI racks expect standard positive-pressure quick-
  disconnects, and a proprietary DC bus / vacuum loop can't host hardware
  that doesn't exist to plug into it. Leak risk is mitigated the way real
  hyperscale sites do it: welded stainless containment pans + zoned leak-
  detection rope, with a two-stage shutdown (leak trips CDU pumps only;
  a separate smoke/fire detector, not the leak rope, trips the main
  breaker) -- see docs/minicenter-fmea.html item 3.1 for the full reasoning
  and the mandatory layout constraint (480VAC bus routed overhead, isolated
  from the fluid drainage path) that this logic depends on.
"""

# ---------------------------------------------------------------------------
# OCP ORv3 frame geometry (Meta Open Rack Frame V3 Spec Rev 1.3, 03JUN2024,
# Sec 6.1-6.3, nominal dims; cross-checked against the Open Rack Base Spec V3
# Rev 1.1 reference drawing, Fig 6.1.1: 600.24mm / 1068.24mm overall).
# The Mini-Center's actual layout is "universal" -- built to accept whatever
# frame the customer's hardware ships in (19in EIA, OCP ORv3, or NVIDIA
# MGX/NVL72-class cabinets), not locked to this one frame -- these constants
# are the reference/default footprint used for layout math, not a mandate.
# ---------------------------------------------------------------------------
RACK_WIDTH_MM = 600.0
RACK_DEPTH_MM = 1068.0
RACK_HEIGHT_MM = 2286.0                 # nominal, floor to frame top
RACK_OU_PITCH_MM = 48.0                 # OpenU vertical pitch
RACK_OU_CAPACITY = 44                   # OpenU slots
RACK_MAX_LOAD_KG = 1400.0               # excludes rack frame's own weight
RACK_LOAD_KW = 130.0                    # Per compute rack, continuous (Primary Design tier)

# ---------------------------------------------------------------------------
# Primary Design tier — Two-Skid Architecture (locked 2026-09-29)
# Skid A: 40ft High-Cube container — compute + CDUs + switchgear.
# Skid B: standard flatbed — generator + adiabatic heat rejection unit.
# Doesn't fit in one box at this scale: a 5.8m generator + ~4.5m compute row
# leaves only 1.7m for switchgear in a 12.03m container -- a real, checked
# volumetric constraint, not a judgment call. Mated on-site via Cam-Lok power
# cables (paralleled per phase for the 1200A total), 3in grooved Victaulic
# fluid couplings, and a ruggedized Amphenol/MIL-spec multi-pin PLC
# connector -- deliberately mirroring already-proven industry (Crusoe-style)
# multi-skid deployment practice, not an invented scheme.
# ---------------------------------------------------------------------------
MINICENTER_RACKS_PER_CONTAINER = 4      # scaled from 2 -> 4 racks, 2026-09-29
MINICENTER_TOTAL_LOAD_KW = MINICENTER_RACKS_PER_CONTAINER * RACK_LOAD_KW  # 520kW

MINICENTER_AC_OUTPUT_VOLTAGE_NOMINAL_V = 480.0  # 415VAC also supported per region
MINICENTER_AC_PHASES = 3
MINICENTER_SWITCHGEAR_RATING_A = 1200.0  # scaled from 600A for the 4-rack load
# No DC bus, no sidecar rectifier -- AC flows from ATS/PDU straight to
# whatever OEM rack the customer plugs in. Its own power shelves do AC/DC.

# Entrance SPD (locked 2026-09-29, FMEA 2.5) -- rural overhead utility/generator
# feeds carry materially higher lightning/switching-transient exposure than
# urban underground service, per the FMEA's own rural-siting assumption.
# 250kA/phase is sound engineering judgment matching common commercial-SPD
# sizing practice for this exposure class -- NOT a number IEEE C62.41 itself
# mandates (that standard defines the exposure category/test waveform, not a
# required product kA rating). Keep that distinction if this ever gets quoted
# as "IEEE-required."
MINICENTER_SPD_EXPOSURE_CATEGORY = "IEEE C62.41(.2) Category C -- service entrance / severe exposure"
MINICENTER_SPD_RATING_KA_PER_PHASE = 250.0
MINICENTER_SPD_MONITORING = "Form C dry contact, degradation alert to Skid A PLC/edge gateway"

# Motivair MCDU-25 (real vendor cutsheet, verified 2026-09-25/28) -- standard
# OCP BMQC-compliant POSITIVE-pressure CDU.
# HONEST TRADEOFF, not a clean swap: at the original 2-rack/260kW scale, a
# single MCDU-25 (625kW) was ~2.4x oversized vs. the tighter-fitting
# Chilldyne CF-CDU300 (300kW) it replaced. Scaling to 4 racks/520kW turns
# that into a genuine asset: 625kW vs. 520kW load is a ~17% N+1 margin --
# far more capital-efficient than the original 2-rack pairing, using the
# exact same CDU hardware.
MINICENTER_CDU_VENDOR = "Motivair MCDU-25"
MINICENTER_CDU_CAPACITY_KW = 625.0    # single-unit rated capacity (100% water basis)
MINICENTER_CDU_HEIGHT_IN = 73.625     # 73-5/8"
MINICENTER_CDU_LENGTH_IN = 42.5       # 42-1/2"
MINICENTER_CDU_WIDTH_IN = 31.5        # 31-1/2" -- matches the real 3in Victaulic connection size
MINICENTER_CDU_PUMPS_PER_UNIT = 2     # standard, not optional -- secondary loop only,
                                       # confirmed against the real cutsheet: "The redundant
                                       # dual pumps deliver a secondary coolant loop..."
                                       # primary/facility loop circulation is an EXTERNAL
                                       # facility pump, not the CDU (same pattern as the
                                       # Chilldyne unit this replaced) -- not yet sourced.
MINICENTER_CDU_PUMP_HEAD_PSI = 37.0
MINICENTER_CDU_FLA_460V_3PH = 9.1     # nameplate FLA @ 460V/3PH
MINICENTER_CDU_UNITS = 2              # 2 physical units for true unit-level N+1

# CDU ambient envelope -- Motivair publishes NO ambient operating range
# anywhere we've checked (unlike Chilldyne, which had one). Held as a
# CONSERVATIVE DESIGN ASSUMPTION, not a verified Motivair spec: adopt the
# same 5-40C floor/ceiling industry-standard for off-the-shelf PLC/VFD/HMI
# electronics. This is why the Climate-Kit strategy exists -- see
# docs/minicenter-basis-of-design.html Section 12 and the FMEA's climate
# rows for the full simulation this was built against.
MINICENTER_CDU_AMBIENT_MIN_C = 5.0    # conservative assumption, not vendor-verified
MINICENTER_CDU_AMBIENT_MAX_C = 40.0   # conservative assumption, not vendor-verified
MINICENTER_CDU_PRIMARY_SUPPLY_MIN_C = 2.0   # from the CDU this replaced; re-verify for Motivair
MINICENTER_CDU_PRIMARY_SUPPLY_MAX_C = 45.0  # from the CDU this replaced; re-verify for Motivair

# Operating envelope, formally bounded 2026-09-29: extreme remoteness and
# existing stranded-power infrastructure are anti-correlated -- the real
# customer (existing substation surplus, flared gas, curtailed renewables,
# or a decommissioned industrial site's idle interconnection) is unlikely to
# be at the planet's most extreme locations. Sahara-grade sandstorm and
# sub-PG60 extreme cold (below this envelope) are explicitly OUT of scope,
# not unsolved problems.
MINICENTER_AMBIENT_ENVELOPE_MIN_C = -40.0
MINICENTER_AMBIENT_ENVELOPE_MAX_C = 48.0
MINICENTER_ALTITUDE_DERATE_FT = 4000.0  # matches the real Chilldyne cutsheet derate figure

# --- Two-loop glycol strategy (Dow Dowfrost chart, verified directly) ---
MINICENTER_SECONDARY_LOOP_FLUID = "PG25 or DI water"  # never sees outdoor ambient
MINICENTER_PRIMARY_LOOP_FLUID_TEMPERATE_HOT = "PG30"  # freeze point ~-13C, per Dow chart
MINICENTER_PRIMARY_LOOP_FLUID_EXTREME_COLD = "PG60"   # freeze point ~-48C, per Dow chart

# --- OCP Blind Mate Manifold / BMQC (verified, generic -- also used by the
# original Pod repo; the Mini-Center's CDU-to-rack connectors follow the
# same positive-pressure standard) ---
OCP_MANIFOLD_MAX_WORKING_PRESSURE_PSIG = 50.0
OCP_MANIFOLD_FLUID_TYPE = "25% propylene glycol / water (Dowfrost LC25)"
OCP_MANIFOLD_MAX_FLUID_TEMP_C = 60.0
OCP_MANIFOLD_REFERENCE_VALVES_PER_SIDE = 12      # OCP Sec 11.2.2 reference
PROJECT_MANIFOLD_VALVES_PER_SIDE = 24            # this project's actual design (spec-permitted)
OCP_BMQC_MAX_WORKING_PRESSURE_PSIG = 50.0
OCP_BMQC_MAX_FLUID_TEMP_C = 60.0
OCP_BMQC_MAX_FLOW_LPM = 9.0
TCS_LOOP_DELTA_T_F = 18.0  # placeholder design assumption, not OCP-specified

WATER_GPM_CONSTANT = 500.0       # 1 GPM water carries ~500 BTU/hr per degF delta-T
PG25_GPM_CONSTANT = 475.0        # industry approximation for PG25 vs. water
KW_TO_BTUH = 3412.142
LPM_TO_GPM = 0.264172
NEC_CONTINUOUS_FACTOR = 1.25     # NEC 210.19(A)(1) -- continuous loads sized at 125%


def kw_to_btuh(power_kw):
    return power_kw * KW_TO_BTUH


def nec_required_ampacity(continuous_load_a, factor=NEC_CONTINUOUS_FACTOR):
    """Minimum conductor/OCPD ampacity per NEC 210.19(A)(1)."""
    return continuous_load_a * factor


def tcs_flow_rate_gpm(heat_load_kw, delta_t_f, fluid_gpm_constant=PG25_GPM_CONSTANT):
    """Required TCS loop flow rate in GPM for a given heat load and loop delta-T."""
    if delta_t_f <= 0:
        raise ValueError("delta_t_f must be > 0")
    btuh = kw_to_btuh(heat_load_kw)
    return btuh / (fluid_gpm_constant * delta_t_f)


def manifold_flow_capacity_gpm(valves_per_side=PROJECT_MANIFOLD_VALVES_PER_SIDE,
                                max_flow_lpm_per_valve=OCP_BMQC_MAX_FLOW_LPM):
    """Max total branch flow (GPM) one manifold side can deliver."""
    return valves_per_side * max_flow_lpm_per_valve * LPM_TO_GPM


def check_rack_flow_capacity(rack_load_kw, delta_t_f,
                              fluid_gpm_constant=PG25_GPM_CONSTANT,
                              valves_per_side=PROJECT_MANIFOLD_VALVES_PER_SIDE,
                              max_flow_lpm_per_valve=OCP_BMQC_MAX_FLOW_LPM):
    """Compare a rack's required TCS flow against the manifold's rated branch
    flow capacity -- independent of whether the CDU has enough kW budget."""
    required_gpm = tcs_flow_rate_gpm(rack_load_kw, delta_t_f, fluid_gpm_constant)
    capacity_gpm = manifold_flow_capacity_gpm(valves_per_side, max_flow_lpm_per_valve)
    margin_gpm = capacity_gpm - required_gpm
    return {
        "required_gpm": required_gpm,
        "capacity_gpm": capacity_gpm,
        "margin_gpm": margin_gpm,
        "compliant": margin_gpm >= 0,
    }


def check_cdu_thermal_margin(rack_count, rack_load_kw, cdu_capacity_kw):
    """Compare total compute heat load against CDU capacity.

    Generic: pass a SINGLE unit's capacity for true N+1 semantics (one unit
    must carry everything alone), or a summed multi-unit capacity if the
    design runs units simultaneously rather than N+1 -- see
    minicenter_cdu_thermal_margin() below for how the Mini-Center uses this.
    """
    total_load_kw = rack_count * rack_load_kw
    margin_kw = cdu_capacity_kw - total_load_kw
    return {
        "total_load_kw": total_load_kw,
        "capacity_kw": cdu_capacity_kw,
        "margin_kw": margin_kw,
        "compliant": margin_kw >= 0,
    }


def minicenter_cdu_thermal_margin():
    """N+1 thermal margin for the Primary Design tier (4 racks / 520kW).

    Checks a SINGLE Motivair MCDU-25's capacity against the full load, since
    the design intent is unit-level N+1: one unit must be able to carry
    everything alone while the second sits standby.
    """
    return check_cdu_thermal_margin(
        rack_count=MINICENTER_RACKS_PER_CONTAINER,
        rack_load_kw=RACK_LOAD_KW,
        cdu_capacity_kw=MINICENTER_CDU_CAPACITY_KW,  # single unit, N+1 semantics
    )


def adiabatic_effective_air_temp_c(dry_bulb_c, wet_bulb_c, pad_effectiveness=0.85):
    """Effective air temperature entering the dry coil after adiabatic
    pre-cooling. 85% is a typical industry saturation-effectiveness figure
    for wetted-media adiabatic pads -- see the Phoenix/Sahara/Singapore
    climate simulation in docs/minicenter-fmea.html. NOTE: the 21C Phoenix
    coincident wet-bulb figure used there is this project's OWN ESTIMATE,
    not yet checked against real ASHRAE 169 design-day data -- that
    verification is still an open checklist item (Phase 1, heat rejection
    section). Corrected 2026-09-29: an earlier version of this docstring
    claimed the estimate had already been matched against real ASHRAE data;
    it had not -- don't let that claim resurface until the real lookup
    actually happens.
    """
    return dry_bulb_c - pad_effectiveness * (dry_bulb_c - wet_bulb_c)


def adiabatic_water_consumption_upper_bound_gal_hr(heat_load_kw, h_vap_kj_kg=2260.0):
    """100%-evaporative worst-case water consumption upper bound. Real V-coil
    units split load between the dry coil and the wetted pre-cool stage, so
    actual consumption is lower than this bound -- use this for supply-line
    and storage-tank sizing, not as an expected average draw."""
    kg_per_hr = (heat_load_kw / h_vap_kj_kg) * 3600.0
    return kg_per_hr / 3.785  # 1 US gal water ~= 3.785 kg


def adiabatic_required_airflow_cfm(heat_load_kw, air_side_delta_t_f):
    """First-principles sensible-heat airflow estimate: CFM = BTU/hr / (1.08 x dT_F).

    air_side_delta_t_f (the air's own temperature rise passing through the
    coil, NOT the fluid approach temperature) is a REQUIRED, project-supplied
    assumption -- typical dry/adiabatic coolers run roughly 8-18 F rise, and
    picking a value inside that range swings the answer by more than 2x (see
    docs/minicenter-checklist.md, heat rejection section, 2026-09-29 note).
    This is why real fan count/model/footprint stays a vendor-selection-
    software item, not something this function can responsibly assert.
    """
    if air_side_delta_t_f <= 0:
        raise ValueError("air_side_delta_t_f must be > 0")
    btuh = kw_to_btuh(heat_load_kw)
    return btuh / (1.08 * air_side_delta_t_f)


# ---------------------------------------------------------------------------
# Presentation-only colors (RGB 0-255), matching the original Pod repo's
# convention for visual consistency across any future 3D modeling.
# ---------------------------------------------------------------------------
RACK_COLOR_RGB = (60, 60, 65)          # dark graphite
CDU_COLOR_RGB = (70, 120, 170)         # steel blue
FEED_A_COLOR_RGB = (200, 30, 30)       # red -- PDU-A / redundant feed A
FEED_B_COLOR_RGB = (30, 150, 60)       # green -- PDU-B / redundant feed B
