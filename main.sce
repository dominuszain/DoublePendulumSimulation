// code of zain ul abideen
clear; clc;

// defining some constants.
m1 = 2; m2 = 1
l1 = 2; l2 = 1

g = 10

// time range for our solution.
t = [0 : 0.001 : 25]

// implementation of the governing differential equations.
function [dxdt]=f(t, x)
    dxdt = [x(3,:); x(4,:);
    -(g .* m1 .* sin(x(1,:)) + g .* m2 .* sin(x(1,:)) + l2 .* m2 .* x(4,:) .* x(4,:) .* sin(x(1,:) - x(2,:)) + l1 .* m2 .* x(3,:) .* x(3,:) .* cos(x(1,:) - x(2,:)) .* sin(x(1,:) - x(2,:)) - g .* m2 .* cos(x(1,:) - x(2,:)) .* sin(x(2,:))) ./ (l1 .* (m1 + m2 - m2 .* cos(x(1,:) - x(2,:)) .* cos(x(1,:) - x(2,:))));
    (g .* m1 .* cos(x(1,:) - x(2,:)) .* sin(x(1,:)) + g .* m2 .* cos(x(1,:) - x(2,:)) .* sin(x(1,:)) + l1 .* m1 .* x(3,:) .* x(3,:) .* sin(x(1,:) - x(2,:)) + l1 .* m2 .* x(3,:) .* x(3,:) .* sin(x(1,:) - x(2,:)) + l2 .* m2 .* x(4,:) .* x(4,:) .* cos(x(1,:) - x(2,:)) .* sin(x(1,:) - x(2,:)) - g .* m1 .* sin(x(2,:)) - g .* m2 .* sin(x(2,:))) ./ (l2 .* (m1 + m2 - m2 .* cos(x(1,:) - x(2,:)) .* cos(x(1,:) - x(2,:))))]
endfunction

// initial conditions.
to = 0;
xo = [1; 0; 0; 0;]
// xo = [theta1, theta2, theta1dot, theta2dot]

// solving the differential equations.
x = ode(xo, to, t, f)

// converting from angular to cartesian co-ordinates.
posx1 = l1 .* sin(x(1,:))
posy1 = -l1 .* cos(x(1,:))

posx2 = l1 .* sin(x(1,:)) + l2 .* sin(x(2,:))
posy2 = -l1 .* cos(x(1,:)) - l2 .* cos(x(2,:))

//plotting
scatter(0, 0)
//scatter(posx1, posy1)
//scatter(posx2, posy2)

// animating the results.
comet([posx1', posx2'], [posy1', posy2'])

// see the relevant paper for more information.




















