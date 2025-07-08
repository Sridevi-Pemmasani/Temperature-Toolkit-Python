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
