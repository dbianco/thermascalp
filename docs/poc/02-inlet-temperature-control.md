# PoC 2: Inlet temperature control options

**Hypothesis:** helmet inlet temperature can be held at setpoint without ever delivering fluid colder than the
register's minimum, even on component failure.

| Option | How | Pros | Cons / failure mode |
|--------|-----|------|---------------------|
| A. 3-way proportional valve | Mixes tank water with return | Simple, standard parts | Stuck valve can pass full-cold fluid |
| B. Bypass loop + second pump | Recirculates warm return to inlet | No servo valve | Two pumps, more plumbing, tuning harder |
| C. Peltier trim stage | Fine temperature adjust after coarse mix | Fast, fine control | Heat rejection, extra power, cost |

**Method:** build A and B on the bench with a resistive load standing in for the dummy head. Inject faults: valve
stuck at cold, sensor open circuit, pump stop, power loss. Log inlet temperature for each.

**Pass:** no fault drives inlet temperature below the minimum. Option C is only prototyped if A or B cannot meet the
control accuracy.

**Decision output:** ranked comparison by failure mode first, cost second.
