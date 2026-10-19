# Background

## How scalp cooling works

Many chemotherapy drugs damage fast-dividing cells, including hair follicle cells, which causes alopecia. Cooling the
scalp before, during and after infusion has two effects:

- **Vasoconstriction:** scalp blood vessels narrow, so less drug reaches the follicles.
- **Reduced follicle metabolism:** colder cells take up less drug and are less vulnerable to it.

Cooling has to cover a **pre-cooling period** (about 30 minutes), the **infusion**, and a **post-infusion period**
(commonly 60 to 90 minutes). A full session therefore needs stable cooling for roughly **3 to 6 hours**.

Effectiveness varies with the drug regimen, dose and patient, and this project makes no efficacy claims. Treatment
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

A circulating system keeps replenishing cold, so it can hold a **moderate, steady temperature** instead. The working
assumption is a scalp contact temperature of roughly 15 °C, within a 14 to 16 °C band, and the project's source notes
cite a 15 to 22 °C range at follicle depth (1 to 2 mm). These figures are **assumptions to be checked against the
clinical literature** and are tracked in [open questions](open-questions.md).

## Prior art to study

- Commercial systems such as Paxman and DigniCap (closed-loop, compressor-cooled, wheeled consoles).
- Passive cold caps such as Elastogel-type frozen gel caps.
- Open-source medical hardware projects, which show that low-cost devices can succeed when safety and documentation
  are taken seriously.

Pointers to peer-reviewed studies and regulatory documents are welcome as contributions.
