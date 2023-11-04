#for a simulator
from qiskit import *
from qiskit.tools.visualization import plot_histogram
from math import pi
%matplotlib inline

#initialise 3 qubit circuit
q0 = QuantumRegister(1, name='q0')
q1 = QuantumRegister(1, name='q1')
q2 = QuantumRegister(1, name='q2')

crz = ClassicalRegister(1, name='crz')
crx = ClassicalRegister(1, name='crx')

circuit = QuantumCircuit(q0, q1, q2, crz, crx) 

# Initialise qubit 
circuit.x(q0)
circuit.barrier()

# create Bell state pair
circuit.h(q1)
circuit.cnot(q1, q2)
circuit.barrier()

# Bell state measurement 
circuit.cx(q0, q1)
circuit.h(q0)
circuit.barrier()
circuit.measure(q0, crz)
circuit.measure(q1, crx)
circuit.barrier()

# transform qubit based on measurement results 
circuit.x(q2).c_if(crx, 1)  # apply x gate if crx is 1
circuit.z(q2).c_if(crz, 1)  # apply z gate if crz is 1

# add final measurement
cr_result = ClassicalRegister(1, name='result')
circuit.add_register(cr_result)
circuit.measure(2, 2)

circuit.draw(output = 'mpl') 

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 1000).result()
plot_histogram(result.get_counts())
