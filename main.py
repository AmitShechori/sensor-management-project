
# main.py - Full Interactive Version

from sensors import Sensor
from event_manager import EventManager

manager = EventManager()

# Initial list of sensors
sensors = [
    Sensor("Temperature", 1, "Kitchen", 18.0, 25.0, 3),
    Sensor("Temperature", 2, "Living Room", 20.0, 24.0, 100),
    Sensor("Temperature", 3, "Bedroom", 16.0, 22.0, 90),
    Sensor("Temperature", 4, "Bathroom", 19.0, 26.0, 80),
    Sensor("Temperature", 5, "Child Room", 19.0, 26.0, 78),
]

all_captured_events = []

while True:
    print("\n--- Smart Home Sensor System ---")
    print("1. Sample all rooms (Batch)")
    print("2. Choose a specific room and amount")
    print("3. View statistics report")
    print("4. Save data and Exit")
    
    choice = input("Select an option (1-4): ")

    if choice == "1":
        try :
            # Ask the user for the number of samples per sensor
            num = int(input("How many samples for each room? "))
        
            # Run the simulation for everyone
            new_data = manager.run_simulation(sensors, num)
            all_captured_events.extend(new_data)
            print(f"Added {len(new_data)} total samples to the system.")
        except:
            print(f"Invalid input please enter a number")
    elif choice == "2":
        # Show all available rooms
        print("\nAvailable Rooms:")
        for i, s in enumerate(sensors):
            print(f"{i}. {s.location} (Current Battery: {s.battery_level}%)")
            
        # Get room choice and number of samples
        room_idx = int(input("Enter room number: "))
        
        if 0 <= room_idx < len(sensors):
            count = int(input(f"How many samples for {sensors[room_idx].location}? "))
            successful_samples = 0
            # Loop to create multiple samples for the selected room
            for _ in range(count):
                event = manager.create_event(sensors[room_idx])
                if event is not None:
                    all_captured_events.append(event)
                    successful_samples += 1
            print(f"Successfully added {successful_samples} samples for {sensors[room_idx].location}.")
            if successful_samples < count:
                print(f"Note: {count - successful_samples} samples failed due to empty battery.")
        else:
            print("Invalid room selection.")

    elif choice == "3":
        # Show stats for all data collected so far
        manager.calculate_statistics(all_captured_events)

    elif choice == "4":
        # Save to files and close the program
        manager.export_to_json(all_captured_events)
        manager.export_to_csv(all_captured_events)
        print("Saving data... Goodbye!")
        break
    else:
        print("Invalid option, please try again.")