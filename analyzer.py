import glob 
import json

def analyzer():
    # Use glob to find all JSON files that start with 'sensor_'
    files = glob.glob("sensor_*.json")
    files.sort() # Ensure we process files in order 

    all_valid_events = []

    num_of_file = len(files)
    print(f"We have {(num_of_file)} files to analyze.")    
    
    for file in files:
        print(f"Analyzing file: {file}")

        #Load the sensor data from the JSON file
        with open(file, 'r') as f:
            data = json.load(f)
            
            if data:
                len_of_data = len(data)
                valid_readings = []
                anomalies_count = 0

                # Filter through each event to separate valid readings from errors/anomalies
                for event in data:
                    # Check 1: Was there a 'Packet Loss' (missing value field)?
                    if "value" not in event:
                        anomalies_count += 1
                    # Check 2: Is the value numeric?
                    elif not isinstance(event["value"], (int, float)):
                        anomalies_count += 1
                    # Check 3: Is the value physically realistic?
                    elif event["value"] < -50 or event["value"] > 50:
                        anomalies_count += 1
                    # Value is clean and safe to use for calculations
                    else:
                        valid_readings.append(event["value"])
                        all_valid_events.append(event)
                

                # Extract metadata and display results for this specific location
                location = data[0]["location"]
                print(f"Results for {location}:")
                print(f"  - Total events: {len_of_data}")
                print(f"  - Anomalies blocked: {anomalies_count}")

                # Calculate the average only if we have at least one valid reading      
                if valid_readings:
                    average = sum(valid_readings) / len(valid_readings)
                    print(f"  - Average temperature: {average:.2f}C")
                else:
                    print(f"  - Average temperature: N/A (No valid data)")
                print("-" * 40)

    # Find the maximun value 
    if all_valid_events:
          hottest_event = max(all_valid_events, key=lambda x: x["value"])  

          print("\n" + "="*40)
          print(f" GOLBAL HOTTEST POINT DETECTED")         
          print(f"Hottest event in: {hottest_event['location']}")
          print(f"Temperature: {hottest_event['value']}C")  
          print(f"Timestamp: {hottest_event['timestamp']}")    
          print("="*40)     

if __name__ == "__main__":
    analyzer()