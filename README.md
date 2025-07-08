# 🚀 Temperature Toolkit – Python Project

I'm excited to share my recent Python project – a **Temperature Toolkit** developed using core Python! 🌡️📊

## 🔍 Project Highlights

✅ Built an interactive **Temperature Toolkit** with a **menu-driven CLI**  
✅ Records are stored in memory using Python **lists/arrays**  
✅ The tool allows users to:
- Create, update, and delete temperature records  
- Convert temperatures for specific dates  
- Analyze trends, averages, and temperature spikes  
- Display summaries, hottest day, extreme days, and more!

## 🛠️ Tools & Skills Used

- Python  
- Data Structures (Lists)  
- Control Flow (Loops, Conditionals)  
- CLI (Command-Line Interface) Design

## 📁 Project Structure
```text
Temperature-Toolkit/
│
├── main.py                                   # Main script to run the CLI Temperature Toolkit
├── Test-Temperature-Toolkit.ipynb            # Jupyter Notebook for testing or demo
│
├── temperature_toolkit/                      # Core package directory
│   ├── __init__.py                           # Makes the folder a Python package
│   ├── analytics.py                          # Functions for analyzing temperature data
│   ├── converter.py                          # Handles temperature unit conversions
│   ├── crud_temperature_records.py           # CRUD operations for temperature records
│   ├── generalutils.py                       # Shared utility/helper functions
│   ├── record.py                             # Defines the Temperature Record class
📝 Note: .ipynb_checkpoints/ and __pycache__/ are auto-generated and can be ignored.
```


## 📄 **File Description**
```text
| `main.py`                                         | Entry point for the CLI program. Displays the menu and handles user input. |
| `Test-Temperature-Toolkit.ipynb`                  | Jupyter notebook to test and demonstrate toolkit functionality.            |
| `temperature_toolkit/__init__.py`                 | Initializes the package so it can be imported as a module.                 |
| `temperature_toolkit/analytics.py`                | Analyzes temperature records (e.g., averages, trends, spikes).             |
| `temperature_toolkit/converter.py`                | Handles temperature unit conversion logic.                                 |
| `temperature_toolkit/crud_temperature_records.py` | Manages create, read, update, and delete (CRUD) operations.                |
| `temperature_toolkit/generalutils.py`             | Utility functions shared across different modules.                         |
| `temperature_toolkit/record.py`                   | Defines the structure of a temperature record using a class.               |


```