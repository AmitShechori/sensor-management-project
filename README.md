# 🏠 Smart Home Sensor System
A modular Python simulation designed to model smart home data streams, featuring automated analytics, data validation and fault-tolerant processing.

## 🛠 Features
- **Object-Oriented Design:** Clean encapsulation of sensor logic and event management for a maintainable and modular codebase.
- **Optimized data Pipeline:** Implemented real-time grouping using Hash Maps (Python dictionaries) to achieve O(n) efficiency for multi-file JSON exports, avoiding costly sorting post-simulation.
- **High-Precision Timing:** Engineered a robust sampling loop that handles floating-point arithmetic precision and ensures exact timing intervals using remainder-compensation logic.
- **Fault simulation:** Models real-time hardware glitches, packet loss and data corruption to test system resilience.
- **Data Integrity & Cleaning:** Automatic filtering of anomalies and corrupted data to ensure accurate analytics.
- **Global Insights:** Leverages Python's 'max()' function with **Lambda Expressions** to pinpoint extreme values (Hottest Point) across the entire distributed sensor network.
- **Scalable Analytics:** Designed to handle multiple sensor files simultaneously using glob pattern matching

---


## 📖 Usage

1. **Generate Data:**
   Run the main simulation to create sensor logs:
   ```bash
   python3 main.py <total_second> <interval_secondes>

   # Example: 60 seconds simulation with a sample every 2 seconds
   python3 main.py 60 2
    ```
2. **Analyze results:**
   Run the analyzer to filter anomalies, calculate averages and find the hottest point:
   ```bash
   python3 analyzer.py 
    ```

## 🚀 Setup & Installation  

### 1. Prerequisites
- **Python 3.10+** is recommended.
- **Dependencies:** No external libraries required (Uses Python Standard Library).

### 2. Create a Virtual Environment (Optional)
Virtual environments keep your project dependencies isolated.
- **Windows:** `python -m venv venv`
- **macOS/Linux:** `python3 -m venv venv`

### 3. Activate the Environment
You must activate the environment every time you open a new terminal.
- **Windows (CMD):** `venv\Scripts\activate`
- **Windows (PowerShell):** `.\venv\Scripts\activate`
- **macOS/Linux:** `source venv/bin/activate`

## 📊 Sample Output

The analyzer.py script provides a comprehensive system report after filtering out simulated hardware errors, battery failures and packet loss:
```text
We have 5 files to analyze.
Analyzing file: sensor_01.json
Results for Kitchen:
  - Total events: 4
  - Anomalies blocked: 0
  - Average temperature: 22.68C
----------------------------------------
Analyzing file: sensor_02.json
Results for Living Room:
  - Total events: 8
  - Anomalies blocked: 1
  - Average temperature: 21.12C
... [Additional sensors processed] ...
========================================
 GLOBAL HOTTEST POINT DETECTED
Hottest event in: Bathroom
Temperature: 30.68C
Timestamp: 2026-01-13 16:13:20
========================================
```

