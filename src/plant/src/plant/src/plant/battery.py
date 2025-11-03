class Battery:
    def __init__(self, capacity_kwh=10.0, soc0=0.5, eff_charge=0.95, eff_discharge=0.95, max_charge_kw=5.0, max_discharge_kw=5.0):
        self.capacity = capacity_kwh
        self.soc = soc0  # fraction 0..1
        self.eff_c = eff_charge
        self.eff_d = eff_discharge
        self.max_c = max_charge_kw
        self.max_d = max_discharge_kw

    def charge(self, power_kw, dt_h):
        # limit charging power
        power = min(power_kw, self.max_c)
        energy = power * dt_h * self.eff_c
        added = energy / self.capacity
        self.soc = min(1.0, self.soc + added)
        return added * self.capacity

    def discharge(self, power_kw, dt_h):
        # limit discharge power
        power = min(power_kw, self.max_d)
        energy_needed = power * dt_h / self.eff_d
        available = self.soc * self.capacity
        used = min(available, energy_needed)
        self.soc = max(0.0, self.soc - used / self.capacity)
        return used * self.eff_d
