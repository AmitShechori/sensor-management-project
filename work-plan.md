Work Plan 

Infrastructure & Environment Setup 
1. WSL & Ubunto - Installing a Linux distribution and configuring Python environment witihn the terminal.
2. GitHub Integration - Creating a remote repository and migrating the existing code using Git.
3. Source Control - Implementing a branch-based workflow to manage new features and version history.  

Transition to Non-Interactive System
1. CLI Arguments - Replacing input() calls with sys.argv to handle runtime parameters directly from the terminal. 
2. Main Execution - Refactoring the entry point into a standalone main(args) function for command-based execution.
3. Autonomous Operation - Removing interactive menus to allow the program to execute and terminate without manual intervention.

System Decoupling 
1. Producer Application - Developing a script that simulates sensors by writing randomized data into individual JSON files
2. Consumer Application - Developing a separate script to monitor these files, extract the latest data and perform statistical analysis.
3. Data Standards - Defining a uniform JSON schema to ensure seamless data transfer between the Producer and Consumer.

Error Handling & Logging 
1. Error Logger - Implementing an errors.log file record system exceptions and runtime failures in real-time.
2. Fault Injection - Adding intentional "chaos" code to test system resilience and recovery.
3. Enhanced Validation -  Strengtheing defensive programming by validating external file data before processing. 