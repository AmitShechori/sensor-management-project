# 🏠 Smart Home Sensor System
A modular Python simulation designed to model smart home data streams, featuring automated analytics, data validation and fault-tolerant processing.

## 🛠 Features
- **Object-Oriented Design:** Clean encapsulation of sensor logic and event management.
- **Fault simulation:** Models real-time hardware glitches, packet loss and data corruption to test system resilience.
- **Data Integrity & Cleaning:** Automatic filtering of anomalies and corrupted data to ensure accurate analytics.
- **Global Insights:** Leverages Python's 'max()' function with **Lambda Expressions** to pinpoint extreme values (Hottest Point) across the entire distributed sensor network.
- **Smart Export:** Outputs data to analysis-ready JSON and CSV formats.
- **Scalable Analytics:** Designed to handle multiple sensor files simultaneously using glob pattern matching

---


## 📖 Usage

1. **Generate Data:**
   Run the main simulation to create sensor logs:
   ```bash
   python main.py 
    ```
2. **Analyze results:**
   Run the analyzer to filter anomalies, calculate averages and find the hottest point:
   ```bash
   python analyzer.py 
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

The analyzer.py script provides a comprehensive system report:
Per-Location Analysis: Total events, anomalies blocked, and average temperature.
Global Hot Spot: The exact location, timestamp, and value of the highest recorded temperature across all sensors.

