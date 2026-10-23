# MVP cost estimate

> Rough, order-of-magnitude estimate for **non-clinical bench prototypes**, with prices based on the Argentine market
> as of **15 October 2026**. Figures are planning assumptions, not quotes. Budget in USD, because the exchange rate
> moves quickly. Nothing here covers medical approval or human use (see [safety and regulatory notes](safety-and-regulatory.md)).

## Cost by prototype level

| Level | Scope | Approx. cost (USD) |
|---|---|---|
| Proof of concept | Pump, ice tank, basic sensors, hoses, controller | 500 to 1,000 |
| **Recommended functional prototype** | Cart, designed helmet, manifolds, parallel channels, alarms, multiple sensors, multi-hour tests | **1,500 to 3,500** |
| Advanced pre-clinical prototype | Improved helmet, medical-grade materials, instrumentation, thermal, electrical and leak testing | 5,000 to 12,000 |

At a reference rate of about ARS 1,500 per USD, the functional prototype is roughly **ARS 2.25 to 5.25 million**.

## Functional prototype breakdown

| Item | Cost (USD) |
|---|---|
| Helmet, manifolds and channels | 250 to 700 |
| Pump, tank, fittings and hoses | 150 to 400 |
| Sensors, microcontroller, display and alarms | 100 to 300 |
| Power supply and protections | 100 to 250 |
| Cart or mobile frame | 100 to 300 |
| Thermal insulation and enclosure | 100 to 250 |
| CAD design and 3D printing | 200 to 600 |
| Instrumentation and testing | 300 to 800 |
| Spares, mistakes and redesigns | 200 to 500 |
| **Sum of line items** | **1,500 to 4,100** |

The line items sum to a slightly wider range than the 1,500 to 3,500 headline figure. Treat 1,500 to 3,500 as the
planning range and the upper line-item sum as a contingency ceiling.

3D printing is not the main expense. In Argentina, TPU filament runs roughly ARS 25,000 to 50,000 per kg, and an
insulated cooler of about 15 L costs around ARS 100,000. The real costs are design, testing, the helmet itself and
the number of iterations.

## Most likely budget

**USD 2,000 to 3,000** (about ARS 3 to 4.5 million), excluding fees for a biomedical engineer or oncologist,
certifications and clinical trials.

| Scenario | Estimate (USD) |
|---|---|
| Builder already has a 3D printer, tools, electronics skills and can design the helmet | 1,200 to 1,800 |
| Base case, as described in this repository | 2,000 to 3,000 |
| Mechanical design, electronics, fabrication and testing are outsourced | 4,000 to 6,000 |

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

1. **Simple circuit:** tank, pump and hose, to measure flow and ice-water runtime.
2. **Test helmet** with 4 to 6 parallel channels.
3. **Final version with 8 to 12 branches**, only if measurements show hot spots.

This matches the [roadmap](../ROADMAP.md): bench models first, then the controller, then the helmet.

## Not included

- Fees for biomedical engineering, clinical, legal or regulatory advice
- Certification and independent testing (electrical safety, biocompatibility)
- Clinical investigation
- **Regulatory approval.** If the product is intended for therapeutic use, ANMAT can require safety documentation,
  risk management, good manufacturing practice and registration as a medical product.

## Caveats

These numbers are a high-level estimate gathered from general market reference prices and have not been verified
against supplier quotes. Please contribute corrections, real quotes and other countries' prices through an issue
(see [CONTRIBUTING.md](../CONTRIBUTING.md)).
