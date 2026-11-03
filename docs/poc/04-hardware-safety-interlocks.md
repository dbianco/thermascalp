# PoC 4: Hardware safety interlocks

Goal: show safety does not depend on firmware being correct.

1. **Independent thermal cutoff on the inlet line.** A bimetal or thermal-fuse style switch, or a comparator circuit
   with its own sensor, that cuts the pump or opens the bypass below a hard minimum. No microcontroller in the path.
2. **Dual redundant sensors with disagreement alarm.** Two sensor types at the inlet; if they differ by more than a
   threshold, alarm and move to the safe state.
3. **Mechanical minimum on the mixing valve.** A stop that prevents the valve reaching full-cold.
4. **Fail-warm default.** De-energized state routes through the warm/bypass path.
5. **Watchdog.** Controller stops commanding if the control loop stalls.

**Test:** on the PoC 2 rig, trigger each failure (unplug sensor, hang firmware, cut power, jam valve) and record the
resulting inlet temperature and time to safe state.

**Pass:** every single-point failure ends in a safe state with no firmware involvement for items 1 to 4.
