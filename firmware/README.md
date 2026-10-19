# Firmware

Planned ESP32 controller firmware (not yet started). The intended behaviour is described in
[thermal control](../docs/architecture/thermal-control.md): sensor validation, PID or duty-cycle pump control, session
phases, alarms, and a safe default of pump off for every fault.

Toolchain candidates: PlatformIO with the Arduino framework, or ESP-IDF.
