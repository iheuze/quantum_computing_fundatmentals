# Pauli X gate
from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector, array_to_latex
%matplotlib inline


circuit = QuantumCircuit(1)
circuit.x(0)   # acts on first and only qubit
# apply another X gate here to undo operation
print(circuit) 
circuit.draw(output = 'mpl')  # 2 ways of displaying

simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
statevector = result.get_statevector()
array_to_latex(statevector, prefix='\\text{statevector = }\n')

plot_bloch_multivector(statevector)


# Pauli Y gate
from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector, array_to_latex
from math import pi
%matplotlib inline


circuit = QuantumCircuit(2) # 2 qubits
circuit.ry(pi/4, [0,1])  # superposition
circuit.y(0)   # acts on first qubit

print(circuit) 
circuit.draw(output = 'mpl')  # 2 ways of displaying

simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
statevector = result.get_statevector()
array_to_latex(statevector, prefix='\\text{statevector = }\n')

plot_bloch_multivector(statevector)


# Pauli Z gate
from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector, array_to_latex
from math import pi
%matplotlib inline


circuit = QuantumCircuit(2) # 2 qubits
circuit.ry(pi/4, [0,1])  # superposition
circuit.z(0)   # acts on first qubit

print(circuit) 
circuit.draw(output = 'mpl')  # 2 ways of displaying

simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
statevector = result.get_statevector()
array_to_latex(statevector, prefix='\\text{statevector = }\n')

plot_bloch_multivector(statevector)
