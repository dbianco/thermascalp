# Conceptual bill of materials

This is a **concept-level BOM**. Part numbers, quantities and costs will be filled in as prototypes are built.

| Subsystem | Component | Description | Function |
|---|---|---|---|
| Helmet | Shell | TPU filament, FDM printed in sections | Ergonomic, flexible structure |
| Helmet | Channels | Medical-grade silicone tubing or molded silicone | Conduct fluid next to the scalp |
| Helmet | Manifolds | Printed or molded symmetric inlet and outlet | Split and recombine flow evenly |
| Helmet | Sensors | 2 or more waterproof contact temperature sensors | Scalp temperature monitoring |
| Helmet | Strap | Adjustable chin strap | Retention and fit |
| Line | Hoses | 2 x silicone hose, about 2 m | Supply and return |
| Line | Insulation | Neoprene or foam sleeves | Reduce heat gain from room |
| Line | Couplings | Dry-break quick disconnects | Spill-free detach |
| Cart | Tank | 10 to 15 L insulated container (polyurethane foam or similar) | Thermal mass, ice and water |
| Cart | Pump | 12 V submersible or diaphragm pump with PWM control | Circulation |
| Cart | Frame | Wheeled trolley or caddy | Mobility, 30 kg or less total |
| Electronics | Microcontroller | ESP32 or Arduino Nano class | Control and monitoring |
| Electronics | Driver | Logic-level MOSFET or motor driver, flyback diode | Pump speed control |
| Electronics | Display | 0.96" OLED plus buttons | Local interface |
| Electronics | Safety | Independent thermostat or comparator, buzzer, leak and level sensors | Hardware backstop and alarms |
| Power | PSU | Certified isolated mains to 12 V DC supply | Patient-side circuit at low voltage |
| Power | Backup (optional) | 12 V battery with protection | Resilience, outlet independence |

## Cost

A target budget will be set once a first prototype exists. The aim is a bill of materials that is a small fraction of
the cost of a commercial scalp cooling console.
