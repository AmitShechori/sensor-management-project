
import random 
import uuid
import json
import csv
import time
from datetime import datetime
from sensors import Sensor


class EventManager:
    def create_event(self,sensor: Sensor) -> dict:
        if sensor.battery_level <= 0:
            print(f"Error: Cannot access sensor {sensor.sensor_id} ({sensor.location}) - Battery is DEAD (0%).")
            return None
        current_battery = sensor.battery_level 
        # Create a random value (with some offset to test min/max)
        sampled_value = round(random.uniform(sensor.min_val -5, sensor.max_val + 5), 2)
        # Get status from sensor 
        status = sensor.validate_value(sampled_value)
        # Battery drop: decrease by 1 each time we read data
        
        sensor.battery_level -= 1
          
        if 0 < sensor.battery_level <= 10 :
            print(f"ALERT! Sensor {sensor.sensor_id} battery is low ({sensor.battery_level}%). Please replace soon!")     
        elif sensor.battery_level == 0: 
            print(f"NOTICE: sensor {sensor.sensor_id} just ran out of battery!")
        # Create the event dictionary with all info    
        event = {
            "event_id": str(uuid.uuid4()), #Unique ID for each log
            "sensor_id": sensor.sensor_id,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "location": sensor.location,
            "value" : sampled_value,
            "status": status,
            "battery_level": f"{current_battery}%"
        }
        return event
    

    def run_simulation(self, sensors_list: list, iterations: int):
        # Runs the simulation for all sensors and collects all events

        all_events = []  # List to store all the results
       
        # Go through each sensor in our list 
        for sensor in sensors_list:
            # Run the check multiple times for each sensor 
            for i in range(iterations):
                delay = round(random.uniform(0.1, 0.5),2)
                time.sleep(delay)
                # Create anew event using the sensor's data
                event = self.create_event(sensor)
                if event is not None:
                # Add the event to our big list
                    all_events.append(event)
        return all_events        
    

    def calculate_statistics(self, events: list):
        # Calculate and print the summary of all collcted data

        # If the list is empty, stop here
        if not events:
            print("No events to analyze.")
            return
        # Create a simple list of just the values
        values = [e['value'] for e in events]
        #  Basic math for average, max, and min
        total_avg = sum(values) / len(values)
        max_val = max(values)
        min_val = min(values)
        # Find the specific event with the highst and lowest value
        max_event = max(events, key=lambda x: x['value'])
        min_event = min(events, key=lambda x: x['value'])
        # Print the final report
        print("\n--- Final Statistics Report ---")
        print(f"Total events processed: {len(events)}")
        print(f"Overall Average: {total_avg:.2f}")
        print(f"Highest Temperature: {max_val} (at {max_event['location']})")
        print(f"Lowest Temperature: {min_val} (at {min_event['location']})")
        print("-------------------------------\n")

    def export_to_json(self, events: list, filename: str = "sensor_data.json"):
        # Save all event data into a JSON file  

        # Open the file in write mode
        with open(filename, 'w') as f:
            # Save the list as a formatted JSON (indent=4 makes it readable)
            json.dump(events, f, indent=4)
        print(f"Successfully saved to {filename}")


    def export_to_csv(self, events: list, filename: str = "sensor_data.csv"):
        # Save all event data into a CSV file 

        # If there is no data, don't do anything
        if not events:
            return    
        # Get the column names (keys) from the first event
        keys = events[0].keys()
        # Open the file and set up the CSV writer
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader() # Write the top header row
            dict_writer.writerows(events) # Write all the data rows
            
        print(f"Successfully saved to {filename}")

    def validate_event_structure(self, event: dict) -> bool:
        
        # Verify that the event dictionary contains all necessary information,
        
        # List of all keys that MUST be present in every event
        required_fields = ["event_id", "sensor_id", "timestamp", "location", "value", "status", "battery_level"]
        
        for field in required_fields:
            # Check if the key is missing or if the value is empty
            if field not in event or event[field] is None:
                return False
        
        return True # Everything is present    