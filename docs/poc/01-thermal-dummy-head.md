# PoC 1: Thermal dummy head

**Hypothesis:** a heated, instrumented head form reproduces a realistic scalp heat load closely enough to evaluate the
cooling loop.

**Build**
- Mannequin or printed head, aluminum or copper-filled shell for spreading, silicone skin layer.
- Kapton/silicone heater films, total adjustable 10 to 40 W (placeholder range, to be set from the literature review).
- 6 to 10 NTC or DS18B20 sensors at the skin surface (crown, temples, forehead, nape, behind ears), plus 1 core.
- Heater driven by a separate supply with its own over-temperature cutoff.

**Measure:** surface temperature per sensor over 6 h at fixed loop settings; heat load from heater power at steady state.

**Pass:** all sensors within a stated band (e.g. spread under 3 K) with no sensor below the minimum set in the risk
register, and the heater power log reconciles with the tank energy balance within 15%.

**Outputs:** CAD, wiring diagram, calibration procedure, CSV log format (see [test report template](05-community-and-reporting.md)).
