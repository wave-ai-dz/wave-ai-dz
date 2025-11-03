# Wave-AI-Sim 🌊🤖
A simple simulation of a **hybrid wave energy system** combining:
- **Oscillating Water Column (OWC)**  
- **Point Absorber (PA)**  
Both controlled by an **AI-based wave prediction system**.

## 🔍 Features
- Predicts upcoming wave height using simple AI (moving average)
- Hybrid control logic adjusts how much each converter works
- Surplus energy stored in a virtual battery
- Deficit energy compensated automatically

## ⚡ How it works
1. AI predicts the next wave.
2. Hybrid controller allocates power generation between OWC & PA.
3. Surplus energy → stored in battery.
4. Energy deficit → covered from battery.

## 🧠 Goal
Demonstrate how **AI can optimize renewable ocean energy** by improving prediction accuracy and storage efficiency.

## 🖥️ Simulation Code
The simulation is available in Python.  
You can run it locally using:
```bash
python run_demo.py
