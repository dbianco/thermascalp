# MVP cost estimate

> Rough, order-of-magnitude estimate for **non-clinical bench prototypes**, with prices based on the Argentine market
> as of **15 October 2026**. Figures are planning assumptions, not quotes. Budget in USD, because the exchange rate
> moves quickly. Nothing here covers medical approval or human use (see [safety and regulatory notes](safety-and-regulatory.md)).

## Revision note

This estimate was first written for the original concept and has been revised to match the
[design review](risk-register.md). The market reference prices and the original line items come from the project's
source notes. **The review adjustments (marked "revised" below) are the maintainers' own estimates**, not sourced
prices. The changes are:

| Review change | Cost effect |
|---|---|
| First MVP is an instrumented **scalp simulator**, not a device for people | New test head, heaters and data logging; the simulator is the main test asset |
| Pump speed alone does not control temperature | New mixing valve or bypass and a flow sensor |
| More sensors (helmet inlet and outlet, distributed scalp sensors including the top of the head, leak, level, flow) plus an independent hardware cut-off | Higher sensing and safety electronics cost |
| Printed TPU is not assumed to be skin-safe or watertight | Silicone interface or a commercial cap replaces a fully printed helmet; printing is limited to outer parts and supports |
| Six-hour endurance, leak and thermal-uniformity tests are required | Higher instrumentation and testing cost |

## Cost by prototype level

| Level | Scope | Approx. cost (USD) |
|---|---|---|
| Proof of concept | Pump, ice tank, basic sensors, hoses, controller | 500 to 1,000 |
| **Recommended functional prototype** (revised) | Cart, helmet interface and manifolds, parallel channels, mixing valve, alarms, multiple sensors, **scalp simulator** and six-hour tests | **2,000 to 4,000** (was 1,500 to 3,500) |
| Advanced pre-clinical prototype | Improved helmet, medical-grade materials, instrumentation, thermal, electrical and leak testing | 5,000 to 12,000 |

At a reference rate of about ARS 1,500 per USD, the revised functional prototype is roughly
**ARS 3 to 6 million**.

## Functional prototype breakdown (revised)

| Item | Original (USD) | Revised (USD) |
|---|---|---|
| Helmet interface (commercial cap or silicone liner), manifolds and channels | 250 to 700 | 300 to 800 |
| Pump, tank, fittings and hoses | 150 to 400 | 150 to 400 |
| Mixing valve or bypass and flow sensor | not included | 50 to 150 |
| Sensors, microcontroller, display, alarms and hardware cut-off | 100 to 300 | 150 to 400 |
| Power supply and protections | 100 to 250 | 100 to 250 |
| Cart or mobile frame | 100 to 300 | 100 to 300 |
| Thermal insulation and enclosure | 100 to 250 | 100 to 250 |
| CAD design and 3D printing (outer shell, supports, manifold housings) | 200 to 600 | 200 to 600 |
| Scalp simulator, instrumentation and testing | 300 to 800 | 500 to 1,200 |
| Spares, mistakes and redesigns | 200 to 500 | 200 to 500 |
| **Sum of line items** | **1,400 to 4,100** | **1,850 to 4,850** |

The line items sum to a slightly wider range than the headline. Treat **2,000 to 4,000** as the planning range and the
upper line-item sum as a contingency ceiling. (The original table summed to 1,400 to 4,100 against a headline of
1,500 to 3,500; the earlier version of this document misstated the lower sum as 1,500.)

3D printing is still not the main expense. In Argentina, TPU filament runs roughly ARS 25,000 to 50,000 per kg, and an
insulated cooler of about 15 L costs around ARS 100,000. The real costs are the helmet interface, the design,
the simulator, testing and the number of iterations.

## Most likely budget (revised)

**USD 2,500 to 3,500** (about ARS 3.75 to 5.25 million), excluding fees for a biomedical engineer or oncologist,
certifications and clinical trials. The earlier base case was USD 2,000 to 3,000.

| Scenario | Original (USD) | Revised (USD) |
|---|---|---|
| Builder already has a 3D printer, tools, electronics skills and can design the helmet | 1,200 to 1,800 | 1,500 to 2,200 |
| Base case, as described in this repository | 2,000 to 3,000 | 2,500 to 3,500 |
| Mechanical design, electronics, fabrication and testing are outsourced | 4,000 to 6,000 | 5,000 to 7,000 |

## Effect of more channel branches

Going from a handful of channels to **10 to 12 internal branches** barely changes material cost, but raises design and
validation effort. Expect a **15 to 30% increase**, mainly from:

- more complex manifolds
- more connections
- flow balancing
- more sensors and measurement points
- more leak and thermal-uniformity tests

## Recommended staged purchasing

Avoid buying everything up front. Spend in stages, and let measurements justify the next one:

1. **Simple circuit and scalp simulator:** tank, pump, hose, mixing valve and inlet sensor on an instrumented artificial
   head, to measure flow, heat load and ice-water runtime.
2. **Test helmet** (commercial cap or silicone interface) with 4 to 6 parallel channels.
3. **Final version with 8 to 12 branches**, only if measurements show hot spots.

This matches the [roadmap](../ROADMAP.md): bench models first, then the controller, then the helmet.

## Not included

- Fees for biomedical engineering, clinical, legal or regulatory advice
- Certification and independent testing (electrical safety, biocompatibility)
- Clinical investigation, and any use on people
- **Regulatory approval.** If the product is intended for therapeutic use, ANMAT can require safety documentation,
  risk management, good manufacturing practice and registration as a medical product.

## Caveats

These numbers are a high-level estimate gathered from general market reference prices and the maintainers' review
adjustments, and have not been verified against supplier quotes. Please contribute corrections, real quotes and other
countries' prices through an issue (see [CONTRIBUTING.md](../CONTRIBUTING.md)).
