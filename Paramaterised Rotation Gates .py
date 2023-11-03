from qiskit import *
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
from math import pi
%matplotlib inline


circuit = QuantumCircuit(3) 
circuit.rx(pi/3, 0)
circuit.ry(pi/3, 1)
circuit.rz(pi/3, 2)
circuit.draw(output = 'mpl') 

simulator2 = Aer.get_backend('statevector_simulator')
result2 = execute(circuit, backend = simulator2).result()
statevector = result2.get_statevector()
array_to_latex(statevector)

plot_bloch_multivector(statevector)
