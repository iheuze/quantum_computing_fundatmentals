from qiskit import *
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
from math import pi
%matplotlib inline

circuit = QuantumCircuit(1, 1) 
circuit.h(0)
circuit.draw(output = 'mpl') 

simulator2 = Aer.get_backend('statevector_simulator')
result2 = execute(circuit, backend = simulator2).result()
statevector = result2.get_statevector()
array_to_latex(statevector)

plot_bloch_multivector(statevector)

circuit.measure(0, 0)
circuit.draw(output = 'mpl') 

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 1024).result()
plot_histogram(result.get_counts())
