from qiskit import *
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
%matplotlib inline


qr = QuantumRegister(2)
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)
circuit.h(qr)
circuit.measure(qr, cr)

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 1024).result()
plot_histogram(result.get_counts())

simulator2 = Aer.get_backend('statevector_simulator')
result2 = execute(circuit, backend = simulator2).result()
statevector = result2.get_statevector()
array_to_latex(statevector)

plot_bloch_multivector(statevector)

# not measuring and specifying which qubit the Hadamard gate acts on

from qiskit import *
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
%matplotlib inline

circuit = QuantumCircuit(2)
circuit.h(0)   # acts on first qubit

simulator2 = Aer.get_backend('statevector_simulator')
result2 = execute(circuit, backend = simulator2).result()
statevector = result2.get_statevector()
array_to_latex(statevector)

plot_bloch_multivector(statevector)

# measuring
from qiskit import *
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector, array_to_latex
%matplotlib inline

circuit = QuantumCircuit(2)
circuit.h(0)   # acts on first qubit
circuit.measure_all()    # measure both qubits

simulator2 = Aer.get_backend('qasm_simulator')  # now looking at circuit
result2 = execute(circuit, backend = simulator2).result()
counts = result2.get_counts()   # get counts instead of state vector

plot_histogram(counts)   # plot histogram instead of Bloch sphere
