# Endpoint Ransomware Behavior Analysis Engine

![Python](https://img.shields.io/badge/python-3.11+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Active-brightgreen)

A modular ransomware behavior monitoring system that watches folders for suspicious file activity like content changes or encrypted renaming.  
Built using Python with `watchdog`, a clean logging system, and flexible core logic — ideal for security awareness, labs, and research.

---

##  Features

- Real-time folder monitoring using watchdog  
- Detects file content modifications  
- Flags suspicious extensions (like `.locked`, `.enc`, `.crypto`)  
- Modular core logic for easy rule updates  
- Alerts shown in terminal and saved to log file  
- Clean file structure + testable components

---

##  Project Structure

Endpoint Ransomware Behavior Analysis Engine/  
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

##  Setup & Run Instructions

### 1. Install Python 3.11+

Download from: https://www.python.org/downloads/release/python-3110/  
 Be sure to enable **"Add Python to PATH"** during installation

---

### 2. Clone or Download the Project

cd into the project directory:

cd "D:\Projects\Endpoint Ransomware Behavior Analysis Engine"

---

### 3. (Optional) Create a Virtual Environment

python -m venv ransomware-env  
ransomware-env\Scripts\activate  

---

### 4. Install Dependencies

pip install -r requirements.txt

---

### 5. Create or Verify `activity_log.json`

Ensure there's a file named `activity_log.json` in the root folder.  
If not, create it manually with the following content:

[]

---

### 6. Start the Monitoring Engine

Run the main script:

python main.py

You should see output like:

=== Endpoint Ransomware Behavior Analysis Engine ===  
[+] Watching directory: sample_watch_dir  
[+] Monitoring started...  

---

### 7. Test It

Inside `sample_watch_dir`, try these actions:

- Edit and save a file → should trigger content modification alert  
- Rename a file to something like `file.locked` or `file.enc` → should trigger suspicious extension alert  

Alerts will show up in the console and get logged in `activity_log.json`

---

##  View Logs

All suspicious activities are saved in JSON format in:  

activity_log.json  

Open with any text editor or in VS Code for review.

---

##  Running Tests

You can run test cases from the `tests/` folder like this:

python -m unittest discover -s tests

---

##  Real-World Use Cases

- Simulate ransomware behavior for demos  
- Use as an educational tool for cybersecurity awareness  
- Build detection use cases in security labs  
- Collect log data for ML or research  

---

## ⚠ Disclaimer

This project is intended **for educational and research purposes only**.  
It does **not offer real-time ransomware protection**, and should not be used as a replacement for antivirus or EDR solutions.

---

##  License

This project is open-source and licensed under the **MIT License**.  
You're free to use, learn, and modify as needed.
