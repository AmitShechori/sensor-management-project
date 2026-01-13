import sys
import glob
import os
from sensors import Sensor
from event_manager import EventManager

def main():
    # Define the files we want to clear before starting a new run
    # This includes individual sensor JSONs and the aggregate CSV file
    files_to_remove = glob.glob("sensor_*.json") + ["sensor_data.csv"]

    for f in files_to_remove:
        try:
           if os.path.exists(f):
               os.remove(f)
        except OSError :
            pass # Ignore errors if file is already gone or inaccessible

    # Create the manager and a list of sensors with specific thresholds and battery levels
    manager = EventManager()
    
    sensors = [
        Sensor("Temperature", 1, "Kitchen", 18.0, 25.0,4), # Sensor 1 starts with 4% battery to simulate battery depletion and errors
        Sensor("Temperature", 2, "Living Room", 20.0, 24.0, 100),
        Sensor("Temperature", 3, "Bedroom", 16.0, 22.0, 100),
        Sensor("Temperature", 4, "Bathroom", 19.0, 26.0, 100),
        Sensor("Temperature", 5, "Child Room", 19.0, 26.0, 100),
    ]
    # Ensure the user provided the required 'total_seconds' argument via Command Line
    num_args =len(sys.argv)
    
    try:

        if num_args == 2:
           total_seconds = float(sys.argv[1])
           interval = 5.0
           print(f"No interval provided. Using default interval: {interval}s")
        elif num_args == 3:
           total_seconds = float(sys.argv[1])
           interval = float(sys.argv[2])
        else:
            print("\n[!] Error: Invalid input")
            print("please follow this format:")
            print("python3 main.py <total_seconds> <interval_seconds>")
            print("\nExample:")
            print("python3 main.py 10 0.5")
            return
        # validate that input are positive and interval fits within total time 

        if total_seconds <= 0 or interval <= 0:
            raise ValueError("All numbers must be positive")
        
        if interval > total_seconds:
            raise ValueError(f"Interval ({interval}s) cannot be larger than total time ({total_seconds}s)")
        # Start the sampling process and capture events from all sensors
        all_captured_events = manager.run_simulation(sensors, total_seconds, interval)

                                             
        # Only proceed to export if data was actually collected
        if all_captured_events:
            manager.export_each_sensor_to_json()
            manager.export_to_csv(all_captured_events)
        else:
            print("No events were captured, skipping files export.")

    except ValueError as e:
        # Catch non-integer input or negative numbers
        print(f"Error: {e}")
# Entry point: ensures main() runs only when script is executed directly
if __name__ == "__main__":
    main()



