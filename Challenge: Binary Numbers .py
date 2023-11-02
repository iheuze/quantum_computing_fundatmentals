from qiskit import *
from qiskit.tools.visualization import plot_state_qsphere
%matplotlib inline


circuit = QuantumCircuit(4) # 4 qubits
circuit.x([0,2,3])   # acts on first, third, fourth qubit

print(circuit) 
circuit.draw(output = 'mpl')  # 2 ways of displaying

simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
plot_state_qsphere(statevector)
