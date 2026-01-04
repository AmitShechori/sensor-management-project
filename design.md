Python Coding Task – Company-Relevant Exercise (Estimated time: 20 hours):
The task 
•	Python Coding Task – Company-Relevant Exercise 
o	Write a Python script that simulates a basic event stream from sensor/camera of your choice. 
o	The script should: 
	Generate events with event id, timestamp, location, and value 
	Perform basic validation (missing fields, invalid values) 
	Aggregate statistics (min / max / average over time window) 
	Output results to console and to a local JSON or CSV file 
o	Additional Deliverables:
	python-basics-notes.md 
	Key concepts learned 
	Code examples 
	Topics that were new or challenging 
o	Focus areas: 
	Clean Python code 
	Functions and basic data structures 
	Readability and correctness



design 
1
sensors.py- Defining the "Hardware" (attributes and internal validation)
2
event_manager.py- The "Brain" (samping logic, data packaging, math/stats, and saving to files)
3
main.py- The "control panel"- setup,user interaction, and connecting all pieces


sensors.py:
1. Define sensor class: type, sensor_id, location, min, max, battery level 
2. Internal Validtion: compares the sampled value against the sensor's min and max boundaries  

event_manager.py:
1. event_manager define events class: event id, sensor id, timestamp, location, value, battery level, status
2. Create event: takes a sensor, pulls a sample, and wraps it into a "Package"
3. Run simulation: a loop that itertes through a list of sensors for a predefined number of time 
4. Statistics: (min / max / average over time window)
5. Export: Output results to console and to a local JSON or CSV file
6. Validtion: missing fileds, missing events

main.py:
1. Instantiates the EvenetManager
2. Create a list of sensor objects
3. A while loop that presents a menu to the user
4. Captures user input and passes the sensors list to the EventManager
5. Displays the final summary results on the screen before closing



