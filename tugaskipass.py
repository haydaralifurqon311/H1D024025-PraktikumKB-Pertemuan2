import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


suhu = ctrl.Antecedent(np.arange(0, 41, 1), 'suhu')
kelembapan = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembapan')
kecepatan = ctrl.Consequent(np.arange(0, 101, 1), 'kecepatan')

suhu['Dingin'] = fuzz.trimf(suhu.universe, [0, 0, 20])
suhu['Normal'] = fuzz.trimf(suhu.universe, [15, 25, 35])
suhu['Panas'] = fuzz.trimf(suhu.universe, [30, 40, 40])

kelembapan['Kering'] = fuzz.trimf(kelembapan.universe, [0, 0, 50])
kelembapan['Lembap'] = fuzz.trimf(kelembapan.universe, [30, 50, 70])
kelembapan['Basah'] = fuzz.trimf(kelembapan.universe, [50, 100, 100])

kecepatan['Lambat'] = fuzz.trimf(kecepatan.universe, [0, 0, 50])
kecepatan['Sedang'] = fuzz.trimf(kecepatan.universe, [30, 50, 70])
kecepatan['Cepat'] = fuzz.trimf(kecepatan.universe, [50, 100, 100])

rule1 = ctrl.Rule(suhu['Panas'] | kelembapan['Basah'], kecepatan['Cepat'])
rule2 = ctrl.Rule(suhu['Normal'], kecepatan['Sedang'])
rule3 = ctrl.Rule(suhu['Dingin'] & kelembapan['Kering'], kecepatan['Lambat'])

kipas_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
simulasi = ctrl.ControlSystemSimulation(kipas_ctrl)

simulasi.input['suhu'] = 32
simulasi.input['kelembapan'] = 60

simulasi.compute()

print(f"Kecepatan Kipas: {simulasi.output['kecepatan']}")
kecepatan.view(sim=simulasi)
plt.show()