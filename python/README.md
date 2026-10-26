# Interactive double pendulum

`pendulum_sim.py` integrates the double-pendulum equations with
`scipy.integrate.solve_ivp` and animates the motion.

## Features

- Sliders for both masses, both lengths, gravity, and the initial angles.
- RK45 integration and a fixed plotting window.
- A trace of the second bob, which makes the chaotic sensitivity visible.

## Run

```bash
pip install numpy scipy matplotlib
python pendulum_sim.py
```
