import math, random
import matplotlib.pyplot as plt
from ..plant.point_absorber import PointAbsorber
from ..plant.owc import OscillatingWaterColumn
from ..plant.battery import Battery
from ..controllers.hybrid_controller import HybridController
from ..models.wave_predictor import WavePredictor

def generate_wave_series(T_seconds, dt_seconds, seed=0):
    random.seed(seed)
    N = int(T_seconds / dt_seconds)
    t = [i * dt_seconds for i in range(N)]
    series = [1.0 + 0.8 * math.sin(2 * math.pi * (ti / 8.0)) + 0.4 * random.uniform(-1, 1) for ti in t]
    series = [max(0.0, s) for s in series]
    return t, series

def run_demo(duration_hours=0.1, dt_seconds=1):
    T = duration_hours * 3600.0
    times, waves = generate_wave_series(T, dt_seconds)
    pa = PointAbsorber(k2=50.0)
    owc = OscillatingWaterColumn(k1=30.0)
    batt = Battery(capacity_kwh=10.0, soc0=0.5)
    ctrl = HybridController()
    pred = WavePredictor(window=10)

    history = []
    power_pa_list = []
    power_owc_list = []
    power_total = []
    soc_list = []
    pred_list = []

    load_kw = 20.0  # constant load for demo

    for i, H in enumerate(waves):
        history.append(H)
        pred_H = pred.predict(history)
        alpha = ctrl.decide_alpha(pred_H)
        p_owc = owc.produce(H) * alpha
        p_pa = pa.produce(H) * (1 - alpha)
        total_gen = p_owc + p_pa
        surplus = max(0.0, total_gen - load_kw)
        deficit = max(0.0, load_kw - total_gen)
        dt_h = dt_seconds / 3600.0

        if surplus > 0.0:
            batt.charge(min(surplus, batt.max_c), dt_h)
        elif deficit > 0.0:
            batt.discharge(min(deficit, batt.max_d), dt_h)

        power_pa_list.append(p_pa)
        power_owc_list.append(p_owc)
        power_total.append(total_gen)
        soc_list.append(batt.soc)
        pred_list.append(pred_H)

    # Visualization
    plt.figure(figsize=(11, 6))

    ax1 = plt.subplot(311)
    ax1.plot(waves, label='Wave Height (m)')
    ax1.plot(pred_list, label='Predicted Height')
    ax1.legend()
    ax1.set_ylabel('H (m)')

    ax2 = plt.subplot(312)
    ax2.plot(power_owc_list, label='OWC Power (kW)')
    ax2.plot(power_pa_list, label='PA Power (kW)')
    ax2.set_ylabel('Power (kW)')
    ax2.legend()

    ax3 = plt.subplot(313)
    ax3.plot(soc_list, label='Battery SoC')
    ax3.set_ylabel('SoC')
    ax3.legend()

    plt.tight_layout()
    plt.show()
