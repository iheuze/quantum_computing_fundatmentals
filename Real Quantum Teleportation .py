# modify quantum teleportation code to run on real quantum computers
from qiskit import *
from qiskit.tools.visualization import plot_histogram
%matplotlib inline

#quantum teleportation circuit using deferred measurement
circuit = QuantumCircuit(3, 1) 

# Initialise quantum state to teleport 
circuit.h(2)
circuit.barrier()

# create Bell state pair
circuit.h(1)
circuit.cnot(1, 0)
circuit.barrier()

# Bell state measurement 
circuit.cx(2, 1)
circuit.h(2)
circuit.barrier()

# apply conditional operations 
circuit.cx(1, 0)
circuit.cz(2, 0)
circuit.barrier()

# measure destination qubit
circuit.measure(0, 0)

circuit.draw(output = 'mpl') 

