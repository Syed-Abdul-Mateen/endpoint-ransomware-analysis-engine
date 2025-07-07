# Endpoint Ransomware Behavior Analysis Engine

This project is a simple file monitoring tool designed to detect suspicious ransomware-like behavior on a local folder. It watches for changes such as:

- File content modifications  
- File renaming to suspicious extensions (e.g., `.locked`, `.enc`, `.crypto`)  

It prints alerts to the console and logs the activity into a JSON file.

---

## 📁 Project Structure

```plaintext
Endpoint Ransomware Behavior Analysis Engine/
│
├── main.py                          # Main entry point to run the monitoring engine
├── requirements.txt                 # Project dependencies
├── activity_log.json                # Logs all detected suspicious activities
├── README.md                        # Project documentation
│
├── monitor/                         # Monitors filesystem changes using watchdog
│   └── file_watcher.py
│
├── engine/                          # Core logic to classify suspicious behavior
│   └── behavior_engine.py
│
├── reporter/                        # Handles logging of alerts
│   └── alert_logger.py
│
├── utils/                           # Utility functions (e.g., for saving logs)
│   └── log_utils.py
│
├── sample_watch_dir/               # Folder being monitored (add/edit files here to test)
│   └── (test files go here)
│
└── tests/                           # Unit tests for components
    └── test_file_watcher.py

---

## Requirements

- Python 3.11 or above  
- pip (Python package installer)  

---

## Step-by-Step Setup and Run Instructions

### 1. Install Python (if not already installed)

Download Python 3.11+ from the official website:  
https://www.python.org/downloads/release/python-3110/  

Make sure to select the checkbox:  
**"Add Python to PATH"** during installation.  

---

### 2. Clone or Download the Project

If you downloaded a ZIP, extract it.  
Open Command Prompt and go to the project folder:

cd "*Replace this with your project folder location*"

---

### 3. (Optional) Create a Virtual Environment

python -m venv ransomware-env  
ransomware-env\Scripts\activate  

---

### 4. Install Required Python Packages

pip install -r requirements.txt  

---

### 5. Create or Check the activity_log.json File

Make sure the activity_log.json file exists in the project root and is initialized as an empty list:

[]

If it doesn’t exist, create a file with the above content manually.

---

### 6. Run the Program

Use this command:

python main.py

You should see output like:

=== Endpoint Ransomware Behavior Analysis Engine ===  
[+] Watching directory: D:\Projects\Endpoint Ransomware Behavior Analysis Engine\sample_watch_dir  
[+] Monitoring directory: D:\Projects\Endpoint Ransomware Behavior Analysis Engine\sample_watch_dir  

Now the program is actively monitoring the folder.

---

### 7. Test It

Do one of the following inside the sample_watch_dir:

- Edit and save any existing file (modifies content)  
- Rename any file to something like `file.locked` or `file.enc`  

These actions will trigger alerts that appear in the console and also get saved into the log file.

---

### 8. View Logs

All suspicious activities are saved to:

activity_log.json  

You can open this file using any text editor or in VS Code to see a history of alerts.

---

##  Real-World Use Cases

- Demonstrating how ransomware changes files  
- Building educational tools for cybersecurity awareness  
- Testing ransomware detection methods in security labs  
- Logging suspicious activity for security teams  

---

##  Disclaimer

This project is designed for **educational purposes only**.  
It does **not offer real-time ransomware protection** and should not be used as a replacement for antivirus or endpoint detection systems.

---

##  License

This project is open-source and available for learning and modification under the **MIT License**.
