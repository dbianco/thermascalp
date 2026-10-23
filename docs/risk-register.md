# Risk register

A living list of the technical, clinical, regulatory and project risks identified so far. It consolidates the hazards
in [safety and regulatory notes](safety-and-regulatory.md) with the findings of a critical review of the original
concept. Severity and likelihood ratings are **preliminary judgements** for prioritisation, not the output of a formal
ISO 14971 analysis.

Legend: **Severity** H (harm to a person or invalidates the concept), M (degrades performance or the project),
L (inconvenience). **Status**: Open, Mitigated in design (planned, not yet verified), or Closed (verified by test).

## Corrections to the original concept

The review changed the design in four ways. Each is reflected in the architecture documents.

| # | Original assumption | Correction |
|---|---|---|
| C1 | "The microcontroller keeps the water at 15 °C by varying the pump speed" | A pump regulates **flow, not temperature**. Temperature control needs a mixing valve or bypass that blends warm return water with cold tank water, plus a sensor at the helmet inlet. |
| C2 | "15 °C is the therapeutic setpoint" | 15 °C is a **placeholder**, not a medical value. The target depends on the drug regimen and must come from clinical literature and an oncologist. |
| C3 | "A 3D-printed TPU helmet with microchannels is suitable for the skin" | Ordinary printed TPU should not be assumed to be skin-safe, watertight at channel scale, or suitable for prolonged use. Use a commercial cap or a medical-silicone interface first, and use printing for outer parts and supports. |
| C4 | "15 L of ice water covers a 4 to 6 hour session" | This is a **hypothesis**, not a conclusion. It must be measured against the real heat load, ambient gains and hose losses (see R-13). |

## Technical risks

| ID | Risk | Sev. | Mitigation direction | Status |
|---|---|---|---|---|
| R-01 | **Pump speed alone cannot control temperature.** Lower flow reduces average cooling but creates cold and warm zones and does not guarantee the scalp reaches the target. | H | Add mixing valve or bypass, helmet-inlet sensor and cascade control (see [thermal control](architecture/thermal-control.md)) | Mitigated in design |
| R-02 | **Non-uniform temperature** across the scalp (hot and cold zones). | H | Symmetric parallel channels, balanced flow, many distributed sensors, thermal mapping on a dummy | Open |
| R-03 | **Helmet fit and comfort** across head sizes; poor contact reduces effectiveness and causes pressure points. | H | Adjustable design, size range, fit tests on dummies first | Open |
| R-04 | **Leaks near the patient**, with wet skin and shorted electronics. | H | Dry-break couplings, leak sensor, electronics above the tank, leak testing | Open |
| R-05 | **Condensation** on cold surfaces and hoses. | M | Insulation, vapour-tight sleeves, drip management, humidity testing | Open |
| R-06 | **Cleaning and disinfection** of the fluid path between uses; microbial growth. | H | Cleanable or disposable circuit, defined fluid and cleaning protocol | Open |
| R-07 | **Sensor and alarm validity**: drift, wrong placement, undetected failure. | H | Redundant sensors, plausibility checks, calibration procedure, alarm testing | Open |
| R-08 | **Six-hour continuous operation** not demonstrated; pump, tank and controller reliability unknown. | M | Endurance tests on the scalp simulator | Open |
| R-09 | **Thermal capacity hypothesis** (15 L, 4 to 6 h) unproven. 15 L warming by 10 K absorbs about 0.63 MJ, and each kg of melting ice adds about 0.33 MJ, so it may suffice, but it depends entirely on real heat input and losses. | M | Measure heat load and tank runtime; size the tank from data | Open |
| R-10 | **Skin-contact materials**: unvalidated printed TPU, adhesives or sealants may irritate, leach, or leak. | H | Medical-grade silicone interface, tested materials only, biocompatibility review | Open |
| R-11 | **Printed TPU channels may not seal** or hold up over prolonged use. | M | Use molded or tubing channels for fluid; print only outer parts and supports | Mitigated in design |
| R-12 | **Power cut or pump failure** mid-session with no defined procedure. | M | Defined fail state, alarm, optional battery backup, written procedure | Open |
| R-13 | **Electrical shock** from mains near fluids and patient. | H | Certified isolated 12 V supply, no mains voltage on the patient side, sealed bay | Mitigated in design |
| R-14 | **Firmware fault** leaves the pump or valve in a harmful state. | H | Watchdog, safe default (pump off), independent hardware limit | Mitigated in design |
| R-15 | **Cart tipping or hose trip hazard** in a busy ward. | M | Low centre of gravity, hose and cable management | Open |

## Clinical risks

| ID | Risk | Sev. | Mitigation direction | Status |
|---|---|---|---|---|
| R-20 | **Excessive cold** causes cold injury, pain or headache. A colder coolant can be more effective but also less comfortable (one study cited in the review compared a 3 °C coolant with an 8 °C one). | H | Independent minimum-temperature cut-off, ramp limits, comfort feedback, oncologist-defined limits | Open |
| R-21 | **Setpoint not validated.** 15 °C is a placeholder; literature targets scalp or follicle-zone temperature and the right value varies by regimen. | H | Literature review, clinical advice, configurable parameters with validated limits | Open |
| R-22 | **Efficacy is regimen-dependent.** Clinical trials report significant hair preservation (roughly 40 to 50% or more in some groups) but not for all drugs. A device that works poorly could give false reassurance. | H | Make no efficacy claims; state limits in all documentation | Open |
| R-23 | **Under-cooling** loses the protective effect without the user noticing. | M | Visible temperature, alarms, session logging | Open |

## Regulatory and project risks

| ID | Risk | Sev. | Mitigation direction | Status |
|---|---|---|---|---|
| R-30 | **Premature human testing**, including on a friend or family member, with an unvalidated device. | H | Project policy: **no human use**; first MVP is a scalp simulator | Mitigated by policy |
| R-31 | **Clinic use without oncologist approval** or regulatory assessment. | H | Clear disclaimers; any clinical path via qualified partners | Mitigated by policy |
| R-32 | **Therapeutic claims** ("prevents hair loss") create legal and ethical exposure. | H | Claims restricted to research and engineering language | Mitigated by policy |
| R-33 | **Regulatory scope**: a therapeutic device may need safety documentation, risk management, good manufacturing practice and registration (ANMAT in Argentina). | H | Obtain regulatory advice before any move toward use | Open |
| R-34 | **Missing expertise**: no biomedical engineer, oncologist or regulatory adviser involved yet. | M | Seek reviewers and partners; document everything openly | Open |
| R-35 | **Budget underestimate** as scope and validation needs grow (see [cost estimate](cost-estimate.md)). | L | Staged purchasing, validate before building more | Open |

## Review recommendations

**Do**
- Build a closed-loop laboratory prototype.
- Use a mains-powered cart, with a battery only as backup.
- Publish designs, measurements and software as open source.
- Treat the first MVP as a **scalp simulator**: an instrumented artificial head that must hold uniform temperature for
  six hours with no leaks and no dangerous cold spots.

**Do not**
- Test on a patient at this stage.
- Promise hair-loss prevention.
- Fix 15 °C as a therapeutic temperature without medical validation.
- Use it in a clinic without oncologist approval and regulatory assessment.

After the simulator milestone, the next step is to involve a biomedical engineer, an oncologist and regulatory advice.
