import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

class DoublePendulumSim:
    def __init__(self):
        # Default parameters from main.sce
        self.params = {
            'm1': 2.0,
            'm2': 1.0,
            'l1': 2.0,
            'l2': 1.0,
            'g': 10.0,
            'theta1_0': 1.0,
            'theta2_0': 0.0,
            'omega1_0': 0.0,
            'omega2_0': 0.0
        }

        self.t_span = (0, 100)
        self.t_eval = np.arange(0, 100, 0.01)

        self.setup_gui()
        self.solve_and_update()

    def derivs(self, t, state):
        theta1, theta2, omega1, omega2 = state
        m1, m2, l1, l2, g = self.params['m1'], self.params['m2'], self.params['l1'], self.params['l2'], self.params['g']
        delta = theta1 - theta2
        denom = (m1 + m2 - m2 * np.cos(delta)**2)

        num1 = (-g * (m1 + m2) * np.sin(theta1)
                - m2 * l2 * omega2**2 * np.sin(delta)
                - m2 * l1 * omega1**2 * np.sin(delta) * np.cos(delta)
                - g * m2 * np.cos(delta) * np.sin(theta2)) / (l1 * denom)

        num2 = (g * (m1 + m2) * np.cos(delta) * np.sin(theta1)
                + l1 * m1 * omega1**2 * np.sin(delta)
                + l1 * m2 * omega1**2 * np.sin(delta)
                + l2 * m2 * omega2**2 * np.cos(delta) * np.sin(delta)
                - g * m1 * np.sin(theta2)
                - g * m2 * np.sin(theta2)) / (l2 * denom)

        return [omega1, omega2, num1, num2]

    def solve_and_update(self):
        y0 = [self.params['theta1_0'], self.params['theta2_0'],
              self.params['omega1_0'], self.params['omega2_0']]

        sol = solve_ivp(self.derivs, self.t_span, y0, t_eval=self.t_eval, method='RK45')

        theta1, theta2 = sol.y[0], sol.y[1]

        self.x1 = self.params['l1'] * np.sin(theta1)
        self.y1 = -self.params['l1'] * np.cos(theta1)
        self.x2 = self.x1 + self.params['l2'] * np.sin(theta2)
        self.y2 = self.y1 - self.params['l2'] * np.cos(theta2)

        max_reach = (self.params['l1'] + self.params['l2']) * 1.2
        self.ax.set_xlim(-max_reach, max_reach)
        self.ax.set_ylim(-max_reach, max_reach)

        # Update animation data
        self.line.set_data(np.append(0, np.append(self.x1, self.x2)),
                          np.append(0, np.append(self.y1, self.y2)))

    def setup_gui(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        plt.subplots_adjust(left=0.35, bottom=0.1)

        self.ax.set_aspect('equal')
        self.ax.grid()

        self.fig.suptitle("Code of Zain Ul Abideen\nModernized by Claude Code + Gemma4",
                           fontsize=14, fontweight='bold')

        self.line, = self.ax.plot([], [], 'o-', lw=2, color='blue')
        self.trace, = self.ax.plot([], [], '-', lw=1, color='gray', alpha=0.5)

        self.sliders = {}
        slider_configs = [
            ('m1', 0.1, 5.0),
            ('m2', 0.1, 5.0),
            ('l1', 0.1, 5.0),
            ('l2', 0.1, 5.0),
            ('g', 0.1, 20.0),
            ('theta1_0', -np.pi, np.pi),
            ('theta2_0', -np.pi, np.pi),
        ]

        for i, (name, start, end) in enumerate(slider_configs):
            ax_slider = plt.axes([0.1, 0.7 - i*0.08, 0.2, 0.03])
            self.sliders[name] = Slider(ax_slider, name, start, end,
                                        valinit=self.params[name])
            self.sliders[name].on_changed(self.on_slider_change)

    def on_slider_change(self, val):
        for name, slider in self.sliders.items():
            self.params[name] = slider.val
        self.solve_and_update()

    def update_plot(self, frame):
        # Pendulum rods
        x_coords = [0, self.x1[frame], self.x2[frame]]
        y_coords = [0, self.y1[frame], self.y2[frame]]
        self.line.set_data(x_coords, y_coords)

        # Trace of the second bob
        self.trace.set_data(self.x2[:frame], self.y2[:frame])

        return self.line, self.trace

    def run(self):
        self.ani = FuncAnimation(self.fig, self.update_plot, frames=len(self.t_eval),
                                 interval=4, blit=True)
        plt.show()

if __name__ == "__main__":
    sim = DoublePendulumSim()
    sim.run()
