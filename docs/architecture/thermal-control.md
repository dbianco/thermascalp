# Thermal control

## Principle

The tank is intentionally colder than needed (about 0 to 5 °C with ice). Pumping that water straight to the helmet
would over-cool the scalp, so the controller **doses the cold** instead of generating it.

> **Flow is not temperature.** A pump regulates flow rate, not temperature. Throttling the pump lowers the *average*
> cooling, but it can also produce cold and warm zones in the helmet and does not guarantee that the scalp reaches the
> target. The original concept assumed pump speed alone would hold the water at a set temperature; that was a design
> error (see [risk R-01](../risk-register.md)).

The corrected approach controls **helmet inlet temperature** and **flow** together:

- a **mixing valve or bypass** blends warm return water with cold tank water to set the inlet temperature,
- a **sensor at the helmet inlet** closes that inner loop,
- **several distributed scalp-contact sensors** in the helmet close the outer loop (cascade control),
- the **pump** sets flow so the channels stay supplied evenly, rather than being throttled to near zero,
- the **setpoint is a configurable parameter**, not a fixed value. The concept's working value of about 15 °C is a
  placeholder (see [risk R-02](../risk-register.md) and [open questions](../open-questions.md)).

```mermaid
flowchart LR
    SP["Setpoint<br/>(to be validated)"] --> E(("error"))
    S["Scalp temperature<br/>sensors"] --> E
    E --> PID["Cascade controller<br/>(PID)"]
    PID --> PWM["Pump PWM +<br/>mixing valve / bypass"]
    PWM --> HEL["Helmet + scalp<br/>thermal plant"]
    HEL --> S
    S --> SAFE{"Safety<br/>supervisor"}
    SAFE -->|"limit exceeded"| STOP["Pump off + alarm"]
```

## Control modes

| Mode | Behaviour |
|---|---|
| Continuous PWM | Pump speed varies with a PID output; smoother, better for stable temperature |
| Duty-cycled | Pump runs for a fixed time then rests (for example 20 s on, 40 s off), simpler to implement |

Starting point: PID on PWM, with duty-cycle as a fallback mode. Tuning must be done on a thermal dummy head before any
other use.

## Session phases

| Phase | Typical duration | Controller behaviour |
|---|---|---|
| Pre-cooling | about 30 min | Ramp scalp temperature down to the setpoint at a limited rate |
| Infusion | varies | Hold setpoint |
| Post-cooling | 60 to 90 min | Hold setpoint, then end session |

The session timer, setpoint and alarms are shown on the OLED so a companion or nurse can monitor the system at a
glance.

## Sensing

- **Several distributed sensors** in the helmet at representative locations (not just one), plus a sensor at the helmet
  inlet and one at the outlet, with plausibility checks between them. Include the **top of the head**, which responded
  least to cooling in the literature ([references](../references.md)).
- Candidates: DS18B20 (digital, waterproof probes, 0.5 °C accuracy class) or NTC thermistors with a calibrated ADC
  path. Final choice depends on accuracy and response time measured on the bench.
- Sensor fault (open circuit, short, out-of-range, disagreement) is treated as a **fault state**, never ignored.

## Fail-safes (design requirements)

These are requirements for the first prototype, not optional features:

1. **Over-cooling cut-off:** if any scalp sensor drops below a hard minimum, stop the pump and alarm.
2. **Independent hardware backstop:** a thermostat or comparator circuit that disables the pump regardless of
   firmware state, so a firmware crash cannot cause over-cooling.
3. **Sensor fault handling:** loss or disagreement of sensors leads to pump stop and alarm.
4. **Watchdog:** a hardware watchdog resets the controller on lock-up, with the pump defaulting to off.
5. **Leak, level and no-flow detection:** tank level, a leak sensor in the electronics bay, and a flow check that
   alarms if the pump is commanded on but no flow is measured.
6. **Fluid temperature limit:** never allow the supply line below a safe minimum at the helmet.
7. **Audible and visual alarms**, with a clear indication of the current state.
8. **Safe default:** every undefined state results in the pump off.
9. **Power loss and pump failure procedure:** a defined, documented behaviour (alarm, valve position, what the
   operator does) rather than an unhandled case.

All cut-offs are independent of the control loop: minimum temperature, leak, loss of flow and sensor failure each stop
the system on their own.

Numeric limits are intentionally not fixed here: they need clinical input and bench validation, and are tracked in
[open questions](../open-questions.md).

## Firmware outline (planned)

```text
loop every 1 s:
    read sensors, validate (range, rate of change, agreement)
    if fault or limit exceeded: pump = OFF, raise alarm
    else: output = PID(setpoint - scalp_temp), clamp to [min_flow, max_flow]
    pump.pwm(output)
    log, update display
```

Firmware lives in [`firmware/`](../../firmware/README.md) once implementation starts.
