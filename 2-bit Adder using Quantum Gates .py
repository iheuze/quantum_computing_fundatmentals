from qiskit import *
from qiskit.tools.visualization import plot_histogram
from math import pi
%matplotlib inline


circuit = QuantumCircuit(4, 2) 
circuit.x(0)
circuit.x(1)
circuit.barrier()

circuit.cx(0, 2)
circuit.cx(1, 2)
circuit.ccx(0, 1, 3)

circuit.barrier()
circuit.measure(2,0)  #measure SUM
circuit.measure(3, 1) # measure CARRY OUT
circuit.draw(output = 'mpl') 
