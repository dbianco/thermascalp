# Safety and regulatory notes

> ThermaScalp is a research concept. It must not be used on patients. This document lists hazards and the path any
> real medical use would require; it is not a compliance claim and not legal or regulatory advice.

## Regulatory context

A device that cools a patient's scalp during chemotherapy is a medical device in most jurisdictions (for example, a
Class II device in the United States for commercial scalp cooling systems). Putting one into clinical use requires
design controls, risk management, biocompatibility and electrical safety testing, and clinical evidence, followed by
approval from the local authority (for Argentina, ANMAT).

Standards that are likely to be relevant, to be confirmed with a regulatory professional:

| Area | Standard (indicative) |
|---|---|
| Medical electrical safety | IEC 60601-1 |
| Risk management | ISO 14971 |
| Biocompatibility of skin-contact materials | ISO 10993 series |
| Software lifecycle | IEC 62304 |
| Usability | IEC 62366-1 |
| Quality management | ISO 13485 |

## Hazard register (summary)

The full, numbered list with severity and status is in the [risk register](risk-register.md). This table is a summary.

| Hazard | Consequence | Mitigation direction |
|---|---|---|
| Over-cooling of the scalp | Cold injury, frostbite, pain, headache | Redundant sensors, hard minimum, hardware thermostat backstop, ramp limits |
| Under-cooling | Loss of protective effect | Alarms, visible temperature, session logging |
| Sensor failure or drift | Wrong control decisions | Redundancy, plausibility checks, calibration procedure |
| Firmware fault | Uncontrolled pump | Watchdog, safe default (pump off), independent hardware limit |
| Electrical shock | Injury | Certified isolated 12 V supply, no mains voltage near patient, sealed electronics bay |
| Leaks | Wet patient, shorted electronics | Dry-break couplings, leak sensor, electronics above the tank, IP-rated enclosure |
| Microbial growth in fluid path | Infection risk | Cleanable or disposable fluid path, defined fluid and cleaning protocol |
| Skin-contact material reaction | Irritation or allergy | Biocompatible, tested materials only |
| Cart tipping or hose trip hazard | Injury | Low centre of gravity, hose management, cable routing |
| Cold-related interaction with the clinical process | Reduced comfort, clinical errors | Clinical input on setpoints and workflow |

## What would be needed before human use

1. Clinical and regulatory advice, and a defined intended use.
2. A risk management file and design history.
3. Bench validation on instrumented thermal dummies.
4. Biocompatibility testing of all patient-contacting materials.
5. Independent electrical safety testing.
6. Ethics-approved clinical investigation under qualified medical supervision.

Until then, the project is limited to non-clinical bench work.
