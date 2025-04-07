import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

# Parameters
num_neurons = 100  # Number of neurons to simulate
steps = 200        # Number of steps in the simulation
fire_probability = 0.1  # Probability that a neuron will fire at each step

# Initialize random positions for neurons in 3D space
neuron_positions = np.random.rand(num_neurons, 3) * 10

def plot_neurons(positions, sizes):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot neurons with varying size and color based on firing status
    active_neurons = sizes > 0
    inactive_neurons = ~active_neurons
    
    ax.scatter(positions[inactive_neurons, 0], positions[inactive_neurons, 1], positions[inactive_neurons, 2],
               c='blue', s=sizes[inactive_neurons], alpha=0.5)
    ax.scatter(positions[active_neurons, 0], positions[active_neurons, 1], positions[active_neurons, 2],
               c='red', s=sizes[active_neurons]*10, alpha=0.9)  # Firing neurons are larger and red

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)
    plt.draw()
    plt.pause(0.3)

# Initialize sizes (all neurons start inactive)
neuron_sizes = np.zeros(num_neurons)

plt.ion()  # Turn on interactive mode for real-time plotting

for step in range(steps):
    # Randomly decide which neurons fire based on the probability
    firing_indices = [i for i in range(num_neurons) if random.random() < fire_probability]
    
    # Update sizes: inactive neurons remain at size 0, firing neurons increase size temporarily
    neuron_sizes[firing_indices] = 50
    
    # Plot current state of neurons
    plot_neurons(neuron_positions, neuron_sizes)
    
    # Reset the sizes for next step (simulate that they stop being active)
    neuron_sizes *= 0.9

plt.ioff()  # Turn off interactive mode
plt.show()