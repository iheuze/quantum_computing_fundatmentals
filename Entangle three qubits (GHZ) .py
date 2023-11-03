from qiskit import *
from qiskit.tools.visualization import plot_histogram
from math import pi
%matplotlib inline


circuit = QuantumCircuit(3) 
circuit.h(0)
circuit.cnot(0,1)
circuit.ccx(0,1, 2)

circuit.barrier()
circuit.draw(output = 'mpl') 
circuit.measure_all()
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 1000).result()
plot_histogram(result.get_counts())
