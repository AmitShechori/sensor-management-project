import sys
import glob
import os
from sensors import Sensor
from event_manager import EventManager

def main():
    # Remove old JSON sensor files to ensure a clean state for the nem simulation run
    for f in glob.glob("sensor_*.json"):
        try:
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
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <total_seconds>")
        return

    try:
        # Convert input to unteger and validate that its a positive number
        total_seconds = int(sys.argv[1])
        if total_seconds <= 0:
            raise ValueError("Please provide a positive number of seconds.")
        # Start the sampling process and capture events from all sensors
        all_captured_events = manager.run_simulation(sensors, total_seconds)

                                             
        # Only proceed to export if data was actually collected
        if all_captured_events:
            manager.export_each_sensor_to_json(all_captured_events)
            manager.export_to_csv(all_captured_events)
        else:
            print("No events were captured, skipping files export.")

    except ValueError as e:
        # Catch non-integer input or negative numbers
        print(f"Error: {e}")
# Entry point: ensures main() runs only when script is executed directly
if __name__ == "__main__":
    main()



