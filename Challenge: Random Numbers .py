from qiskit import *
from qiskit.tools.visualization import plot_histogram
from math import pi
%matplotlib inline

circuit = QuantumCircuit(3) 
circuit.x(0)
circuit.h(1)
circuit.rx(pi/3,2)
circuit.measure_all()
circuit.draw(output = 'mpl') 


simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 1024000).result()
plot_histogram(result.get_counts())
