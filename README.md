# Quantum Harmonic Oscillator

## Usage
### Poetry

Open the root directory of this repository and issue the following command:
```
$ poetry install
```
This creates a python virtual environment with all of the required python modules.
To enter the environment, issue the command
```
$ poetry shell
```

## Physics Details

### Background

In physics, the simple harmonic oscillator (SHO) is one of the most important systems one can study, since it is a good approximation for most other potentials that allow for bound states.
The potential for the SHO is given by
$$U(\hat{x}) = \frac{1}{2} m \omega^2 \hat{x}^2,$$
where $\omega$ is the angular frequency of the oscillations.

### Energy Eigenstates

The fact that this potential is useful for study in quantum mechanics shouldn't be a surprise, given that it's so important everywhere else in physics, so this repository is used to visualize interesting states of a quantum system in a SHO potential.
If one solves the time independent Schroedinger equation,
$$
\hat{H}\psi = E\psi,
$$
where, for the SHO,
$$
\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2\hat{x}^2,
$$
one can find the spatial wave functions for energy eigenstates of the system.

### Coherent States

However, somethings that might be a bit more interesting than energy eigenstates are coherent states.
These states are ones that are eigenstates of the anihillation operator:
$$
a^\dagger \psi' = \lambda \psi',
$$
where $\lambda \in \mathrm{C}$.
One can solve this eigenvalue problem to find the coherent states.

However, if one wants to time evolve the coherent states, it would be easier to write them as a linear combination of the energy eigenstates, since time evolutions are very easy to work with in the energy eigenstate basis.

