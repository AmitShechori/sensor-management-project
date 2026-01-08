
import random 
import uuid
import json
import csv
import time
import logging
from datetime import datetime
from sensors import Sensor
# Initialize logging: 'filemode=w' ensures we start with a fresh log each run
logging.basicConfig(
    filename= 'errors.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)

class EventManager:
    def create_event(self,sensor: Sensor) -> dict:
        # If battery is dead, log the error and skip this sensor
        if sensor.battery_level <= 0:
            error_msg = f"Cannot access sensor {sensor.sensor_id} - Battery DEAD"
            logging.error(error_msg) 
            print(f"Error: {error_msg}")
            return None
        
        current_battery = sensor.battery_level 

        # Roll for a random chance to trigger sensor anomalies/errors
        chance = random.random()
        # 5% chance: Simulate a hardware glitch returnung extreme low values
        if chance < 0.05:
            sampled_value = round(random.uniform(-50, -200), 2)
            logging.warning(f"Sensor {sensor.sensor_id} ({sensor.location}): Hardware error - Extreme low value detected: {sampled_value}.")
        # 5% chance: Simulate a hardware glitch returnung extreme high values 
        elif chance < 0.1:
            sampled_value = round(random.uniform(50, 200), 2)
            logging.warning(f"Sensor {sensor.sensor_id} ({sensor.location}): Hardware error - Extreme high value detected: {sampled_value}.")
        # 2% chance: Simulate data corruption by returning a string instead of a number
        elif chance < 0.12:
            sampled_value = "ERR_DATA_CORRUPT"
            logging.error(f"Sensor {sensor.sensor_id} ({sensor.location}): Data corruption - Non-numeric value received")      
         # Standard operation: value is mostly within range with a small offset for testing
        else:  
            sampled_value = round(random.uniform(sensor.min_val -5, sensor.max_val + 5), 2)
        
        
        # Get status from sensor 
        status = sensor.validate_value(sampled_value)

        # Battery drop: decrease by 1 each time we read data
        sensor.battery_level -= 1

        # Alert the user if battery levels are getting critical  
        if 0 < sensor.battery_level <= 10 :
            print(f"ALERT! Sensor {sensor.sensor_id} battery is low ({sensor.battery_level}%). Please replace soon!")     
        elif sensor.battery_level == 0: 
            print(f"NOTICE: sensor {sensor.sensor_id} just ran out of battery!")

        # Package everything into an event dictionary    
        event = {
            "event_id": str(uuid.uuid4()), #Unique ID for each log
            "sensor_id": sensor.sensor_id,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "location": sensor.location,
            "value" : sampled_value,
            "status": status,
            "battery_level": f"{current_battery}%"
        }
        # 5% chance: Simulate Packet Loss (value field goes missing during transmission)
        if random.random() < 0.05:
            logging.warning(f"Sensor {sensor.sensor_id} ({sensor.location}): Packet loss - value field missing in transmission")
            del event["value"]
            event["status"] = "ERROR: Missing Value"        
        return event
    

    def run_simulation(self, sensors_list: list, total_seconds: int):
        # Configuration: sensors take a sample every 5 seconds 
        interval = 5
        time_passed = 0
        all_captured_events = []

        print(f"Starting simulation for {total_seconds} seconds. Sample every {interval} seconds.")
        
        # Main simulation loop: iterate as long as we haven't exceeded the total duration
        while time_passed <= total_seconds:
                print(F"Sampling at second: {time_passed}")
        
                # Generate an event for each sensor provided in the sensors_list
                for sensor in sensors_list:
                    event = self.create_event(sensor)
                    # If the sensor is active (not dead/None), store the event
                    if event:
                      all_captured_events.append(event)

                # Determine the wait time until the next sampling point
                if time_passed + interval <= total_seconds: 
                    # Normal interval wait       
                    time.sleep(interval)
                    time_passed += interval

                
                elif time_passed < total_seconds:
                    # Final wait: handle the remaining seconds to reach the exact total_seconds
                    remainder = total_seconds - time_passed
                    print(f"Waiting for the remainder of {remainder} seconds...")
                    time.sleep(remainder)
                    time_passed += remainder
               
                else:
                    # Stop if we have reached the exact total time
                    break
                              
           
        print(f"\nSimulation complete. Total time: {time_passed} seconds. Processed {len(all_captured_events)} events.")
        return all_captured_events        
    

    

    def export_each_sensor_to_json(self, events:list):
        # Group data by sensor ID and save each to a separate JSON file
        
        # If there is no data, dont do anything  
        if not events:
            return
        
        sensor_ids = set(e['sensor_id'] for e in events)
        for s_id in sensor_ids:
            sensor_events = [e for e in events if e['sensor_id'] == s_id]
            filename = f"sensor_{s_id:02d}.json"

            with open(filename, 'w') as f:
                json.dump(sensor_events, f, indent=4)
        print(f"Successfully saved {len(sensor_ids)} files.")    



    def export_to_csv(self, events: list, filename: str = "sensor_data.csv"):
        # Save the entire simulation result into a single CSV 

        # If there is no data, don't do anything
        if not events:
            return    
        # Hardcoded headers to ensure the CSV structure remains consistent even if value are missing
        keys = ["event_id", "sensor_id", "timestamp", "location", "value", "status", "battery_level"]
        try:
        
        # Open the file and set up the CSV writer
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                dict_writer = csv.DictWriter(f, fieldnames=keys)
                dict_writer.writeheader() # Write the top header row
                dict_writer.writerows(events) # Write all the data rows
            
            print(f"Successfully saved to {filename}")
        except IOError as e:
            # Catching errors if the file is locked 
            print(f"Error saving CSV file: {e}")
    