
class Sensor:
    
    # A simple class representing a sensor.
    
    def __init__(self, sensor_type: str, sensor_id: int, location: str, min_val: float, max_val: float, battery_level: int):
        
        # The constructor method initializes the object's attributes.
        
        self.sensor_type = sensor_type
        self.sensor_id = sensor_id
        self.location = location
        self.min_val = min_val
        self.max_val = max_val 
        self.battery_level = battery_level

        
        # Validates the sampled value against the sensor's defined range
        # Returns a descriptive status string
        
    def validate_value(self, value: float) -> str:
        # Ensure the data is numeric to prevent comparison errors
        if not isinstance(value, (int, float)):
            return "ERROR: Invalid numeric data"
        # Check against minimum threshold
        if value < self.min_val:
            return f"Too Low, the temperature is: {value}C"
        # Check against maximum threshold
        elif value > self.max_val:
            return f"Too High, the temperature is: {value}C"
        # Value is within the safe operating range
        else:
            return f"Valid, the temperature is: {value}C"
             
