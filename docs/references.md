# References

Literature that informs the design. Entries are summarised from the published abstract; read the full paper before
relying on any detail. Contributions are welcome through pull requests.

## Scalp temperature and coolant setpoint

**Ekwall EM, Nygren LML, Gustafsson AO, Sorbe BG.** *Determination of the most effective cooling temperature for the
prevention of chemotherapy-induced alopecia.* Molecular and Clinical Oncology 2013;1(6):1065-1071.
[PubMed 24649294](https://pubmed.ncbi.nlm.nih.gov/24649294/) · [PMC3915696](https://pmc.ncbi.nlm.nih.gov/articles/PMC3915696/) ·
DOI [10.3892/mco.2013.178](https://doi.org/10.3892/mco.2013.178)

| Aspect | Finding |
|---|---|
| Design | Pre-study with 5 healthy female volunteers measuring scalp temperature at 3 and 8 °C coolant; randomized main study of 47 patients (43 evaluable after cycle 1) on paclitaxel/carboplatin |
| Working target | Earlier studies suggest a temperature **below 22 °C at 1 to 2 mm depth** in the scalp is needed to prevent alopecia |
| Coolant temperature | A pre-set coolant temperature of 3 °C **tended to be more efficient** at bringing the follicle region below 22 °C than 8 °C |
| Clinical result | **No significant difference in alopecia prevention** between 3 °C and 8 °C in the main study |
| Side effects | **Headache and a feeling of coldness were more common** at 3 °C |
| Site variation | **The top of the head was less responsive** to cooling; temperatures varied between scalp sites and between individuals |
| System | Computer-controlled scalp cooling |

### What it means for ThermaScalp

- The commonly quoted target is a **follicle-depth temperature (below about 22 °C at 1 to 2 mm)**, not a coolant or
  skin-surface value. The coolant setpoint in this study (3 or 8 °C) is a different quantity from the temperature the
  scalp reaches. ThermaScalp's early "15 °C" figure mixed these ideas and remains a placeholder
  ([R-21](risk-register.md)).
- A colder coolant reached the physiological target more reliably but **did not translate into better hair
  preservation** in this small study, and it increased discomfort. "Colder is better" is not supported, which argues for
  a controlled, comfort-aware setpoint rather than minimum temperature ([R-20](risk-register.md)).
- **The top of the head cooled less.** Helmet design and sensor placement should check that region specifically
  ([R-02](risk-register.md)), and the helmet needs good contact there.
- **Limitations:** very small sample, a single chemotherapy regimen (paclitaxel/carboplatin), one commercial system.
  The findings cannot be generalised to other drugs or devices.

## To add

- Clinical trial evidence for scalp cooling efficacy by regimen (the SCALP trial and regulatory clearance documents
  mentioned in the project's source notes).
- Studies of scalp heat load and heat transfer, for sizing the tank.
- Cold-injury safety literature for sustained scalp cooling.
