# Double Pendulum Simulation

A high-fidelity physics simulation of a double pendulum implemented in Python.

## Features
- **Real-time Physics**: Uses `scipy.integrate.solve_ivp` with RK45 integration for accurate motion.
- **Interactive GUI**: Dynamic sliders to adjust parameters on the fly:
  - Masses ($m_1, m_2$)
  - Lengths ($l_1, l_2$)
  - Gravity ($g$)
  - Initial Angles ($\theta_{1,0}, \theta_{2,0}$)
- **Smooth Visualization**: Animated using `matplotlib` with a trace of the second bob's trajectory.

## Installation
Ensure you have the required dependencies installed:
```bash
pip install numpy scipy matplotlib
```

## Usage
Run the simulation with:
```bash
python pendulum_sim.py
```
