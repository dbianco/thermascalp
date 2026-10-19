# Roadmap

Dates are intentionally omitted until the project has contributors. Each milestone is gated by the previous one.

## Milestone 0: Concept (current)

- [x] Define the problem and the overall architecture
- [x] Document subsystems, control strategy and hydraulics
- [x] Draft the hazard register and open questions
- [ ] Redraw the concept illustrations in English and correct the annotation errors
- [ ] Literature review: effective scalp temperature, heat load, safety limits

## Milestone 1: Bench models

- [ ] Heated thermal dummy head with measurable heat load
- [ ] Tank thermal test: ice-water runtime versus room temperature and heat load
- [ ] Flat channel coupons: serpentine versus meshed, pressure drop and uniformity
- [ ] Pump and hose selection, with a measured flow curve

## Milestone 2: Controller prototype

- [ ] Breadboard ESP32 controller with sensors, MOSFET pump driver and OLED
- [ ] PID tuning on the dummy head
- [ ] Fail-safe implementation: hardware backstop, watchdog, sensor fault handling
- [ ] Session logging and alarm behaviour

## Milestone 3: Helmet prototype

- [ ] Printable TPU helmet shell with integrated manifolds
- [ ] Silicone channel integration, leak testing
- [ ] Fit tests on dummies of several sizes
- [ ] First end-to-end run: cart, line and helmet on the thermal dummy

## Milestone 4: Documentation and community

- [ ] Reproducible build guide, CAD files, wiring diagrams, firmware release
- [ ] Peer review by engineers and clinicians
- [ ] Decision point: whether and how to pursue clinical and regulatory validation with qualified partners

Human use is not part of any milestone above. See [safety and regulatory notes](docs/safety-and-regulatory.md).
