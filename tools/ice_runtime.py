#!/usr/bin/env python3
"""PoC: ice-water tank runtime estimate (bench model only, not for human use).

Lumped model: the tank absorbs the dummy-head heat load plus pump heat and
ambient gain until all ice has melted and the water has warmed to the limit
temperature at which the loop can no longer hold the setpoint.

    runtime = (m_ice * L_fusion + m_water * c_w * (T_limit - T_start)) / Q_total

All numbers are placeholders to be replaced by the Milestone 1 tank test.
"""
import argparse

L_FUSION = 334.0   # J/g, latent heat of ice
C_WATER = 4.186    # J/(g K)


def runtime_hours(m_ice_g, m_water_g, q_head_w, q_pump_w, ua_w_per_k,
                  t_ambient_c, t_start_c=0.0, t_limit_c=8.0):
    # Ambient gain through the tank wall, evaluated at the mean tank temperature.
    t_mean = (t_start_c + t_limit_c) / 2
    q_total = q_head_w + q_pump_w + ua_w_per_k * (t_ambient_c - t_mean)
    energy_j = m_ice_g * L_FUSION + m_water_g * C_WATER * (t_limit_c - t_start_c)
    return energy_j / q_total / 3600, q_total


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--ice-kg", type=float, default=3.0)
    p.add_argument("--water-kg", type=float, default=3.0)
    p.add_argument("--ua", type=float, default=0.5, help="tank wall UA, W/K")
    p.add_argument("--pump-w", type=float, default=8.0)
    p.add_argument("--limit-c", type=float, default=8.0)
    a = p.parse_args()

    print(f"{'head load W':>11} {'ambient C':>9} {'total W':>8} {'runtime h':>9}")
    for q in (10, 20, 30, 40):
        for amb in (20, 25, 30):
            h, qt = runtime_hours(a.ice_kg * 1000, a.water_kg * 1000, q,
                                  a.pump_w, a.ua, amb, t_limit_c=a.limit_c)
            flag = "" if h >= 6 else "  < 6 h target"
            print(f"{q:>11} {amb:>9} {qt:>8.1f} {h:>9.1f}{flag}")


if __name__ == "__main__":
    main()
