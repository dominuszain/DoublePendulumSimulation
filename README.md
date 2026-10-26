# Double pendulum simulation

**Chaotic motion from Lagrangian mechanics, in Scilab and Python**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Scilab](https://img.shields.io/badge/Scilab-6.x-D35400)](https://www.scilab.org/)

This project solves the equations of motion for a double pendulum and animates
the result. The original Scilab code integrates the equations with `ode`; the
Python version uses `solve_ivp` and adds sliders for the masses, lengths,
gravity, and initial angles. The equations themselves are derived symbolically
in `Derivation/lagrange.ipynb`.

**Author:** Zain Ul Abideen
**GitHub repository:** [dominuszain/DoublePendulumSimulation](https://github.com/dominuszain/DoublePendulumSimulation)

![Double pendulum animation](docs/pendulum.gif)

The initial configuration is shown in [`docs/diagram.png`](docs/diagram.png).

## Python simulation

```bash
cd python
pip install numpy scipy matplotlib
python pendulum_sim.py
```

See [`python/README.md`](python/README.md) for the controls.

## Original Scilab code

Open `main.sce` in Scilab and run it. The state vector is
`[θ₁, θ₂, θ̇₁, θ̇₂]`, and the script converts the angles to Cartesian
coordinates before animating the two bobs. The course report is
[`main.pdf`](main.pdf).

## Derivation

`Derivation/lagrange.ipynb` derives the governing equations with SymPy using the
Lagrangian

```
L = T - V
```

for two point masses connected by massless rods.

## Repository layout

```
.
├── python/           # interactive Python simulation
├── Derivation/       # symbolic derivation with SymPy
├── docs/             # animation and figures
├── main.sce          # original Scilab code
├── main.pdf          # course report
├── CITATION.cff
└── LICENSE
```

## Citation

```bibtex
@software{ulabideen_doublependulum_2026,
  author = {Ul Abideen, Zain},
  title  = {Double pendulum simulation},
  year   = {2026},
  url    = {https://github.com/dominuszain/DoublePendulumSimulation}
}
```

## License

Released under the [MIT License](LICENSE).
