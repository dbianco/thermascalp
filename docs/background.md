# Background

## How scalp cooling works

Many chemotherapy drugs damage fast-dividing cells, including hair follicle cells, which causes alopecia. Cooling the
scalp before, during and after infusion has two effects:

- **Vasoconstriction:** scalp blood vessels narrow, so less drug reaches the follicles.
- **Reduced follicle metabolism:** colder cells take up less drug and are less vulnerable to it.

Cooling has to cover a **pre-cooling period** (about 30 minutes), the **infusion**, and a **post-infusion period**
(commonly 60 to 90 minutes). A full session therefore needs stable cooling for roughly **3 to 6 hours**.

Effectiveness varies a lot with the **drug regimen**, dose, cap fit and the scalp temperature actually reached. Clinical
trials and regulatory submissions for commercial systems report significant hair preservation in roughly 40 to 50% of
patients, or more, in certain groups, but scalp cooling does not work equally well for all drugs. (These figures come
from the project's source notes and still need proper citations.) This project makes **no efficacy claims**. Treatment
protocols should come from the patient's oncology team.

## Current options

| | Hospital machines | Frozen gel caps | ThermaScalp (concept) |
|---|---|---|---|
| Cooling | Compressor chiller, circulating coolant | Passive, pre-frozen at about -15 to -20 °C | Ice water, pump-dosed |
| Temperature control | Closed loop | None (cap warms steadily) | Closed loop |
| Logistics | Fixed at the clinic | 5 to 6 caps per session, frozen transport, swap about every 30 min | One cart, ice loaded at the clinic |
| Cost | High | Low | Low (target) |
| Availability | Limited to clinics that can afford them | Widely available | Not yet buildable or validated |

## Why a controlled temperature instead of "as cold as possible"

A frozen gel pack must start far below 0 °C because it is a static block of cold: it heats up the moment it touches
the head, so it has to start extreme to still be effective 30 minutes later. That is uncomfortable and carries a risk
of cold injury to the skin.

A circulating system keeps replenishing cold, so it can hold a **moderate, steady temperature** instead. The early
concept used a scalp contact temperature of roughly 15 °C (14 to 16 °C band) as a working value, with source notes
citing 15 to 22 °C at follicle depth (1 to 2 mm). **15 °C is a placeholder, not a universal medical setpoint.** The
literature speaks of reaching a sufficiently low temperature at the scalp or follicle zone (a commonly cited target is
below about 22 °C at 1 to 2 mm depth). In a randomized study of 47 patients
([Ekwall et al., 2013](references.md)), a 3 °C coolant was more effective than 8 °C at reaching that target, but it
produced **no significant difference in hair preservation** and caused more headache and coldness. The top of the head
cooled least. The
right value must come from the clinical literature and an oncologist, and is tracked in
[open questions](open-questions.md) and the [risk register](risk-register.md) (R-20, R-21).

## Prior art to study

- Commercial systems such as Paxman and DigniCap (closed-loop, compressor-cooled, wheeled consoles).
- Passive cold caps such as Elastogel-type frozen gel caps.
- Open-source medical hardware projects, which show that low-cost devices can succeed when safety and documentation
  are taken seriously.

Pointers to peer-reviewed studies and regulatory documents are welcome as contributions.
