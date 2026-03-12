
import cirq

# ૧. ક્યુબિટ તૈયાર કરવું (આ આપણું કેન્સર ડિટેક્ટર છે)
qubit = cirq.GridQubit(0, 0)

# ૨. રિસર્ચ લોજિક (સર્કિટ) તૈયાર કરવી
# Hadamard Gate (H) ક્યુબિટને સુપરપોઝિશનમાં લાવે છે
circuit = cirq.Circuit(
    cirq.H(qubit),                    # એકસાથે અનેક શક્યતાઓ તપાસવા માટે
    cirq.measure(qubit, key='result') # અંતિમ માપણી લેવા માટે
)

# ૩. સિમ્યુલેટર પર ૧૦૦ વખત પ્રયોગ ચલાવવો
simulator = cirq.Simulator()
samples = simulator.run(circuit, repetitions=100)

# ૪. પરિણામો જોવું (હિસ્ટોગ્રામ)
print("કેન્સર સેલ વિશ્લેષણ રિપોર્ટ (૧૦૦ ટેસ્ટ):")
print(samples.histogram(key='result'))
