from qiskit import *
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
from math import pi
%matplotlib inline


circuit = QuantumCircuit(3) 
circuit.h([0, 1, 2])
circuit.s(1)
circuit.sdg(2)
circuit.draw(output = 'mpl') 

simulator2 = Aer.get_backend('statevector_simulator')
result2 = execute(circuit, backend = simulator2).result()
statevector = result2.get_statevector()
array_to_latex(statevector)

plot_bloch_multivector(statevector)
