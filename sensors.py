
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

        
        # Check if the value is within range and include the value in the returned string. 
        
    def validate_value(self, value: float) -> str:
        if value < self.min_val:
            return f"Too Low, the temperature is: {value}C"
        elif value > self.max_val:
            return f"Too High, the temperature is: {value}C"
        else:
            return f"Valid, the temperature is: {value}C"
             
