from qiskit import *
from qiskit.tools.visualization import plot_histogram
%matplotlib inline


circuit = QuantumCircuit(2) 
# Bell State
circuit.h(0)
circuit.cnot(0,1)
circuit.barrier()

# encode message
match message := '10':
  case '00':
    circuit.id(0)
  case '01':
    circuit.z(0)
  case '10':
    circuit.x(0)
  case '11':
    circuit.z(0)
    circuit.x(0)

circuit.barrier()

# decode message
circuit.cx(0,1)
circuit.h(0)

circuit.measure_all()
circuit.draw(output = 'mpl') 


simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 1000).result()
plot_histogram(result.get_counts())
