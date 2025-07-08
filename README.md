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
- **main.py**: Entry point for the CLI program. Displays the menu and handles user input.
- **Test-Temperature-Toolkit.ipynb**: Jupyter notebook to test and demonstrate toolkit functionality.
- **temperature_toolkit**
    - **__init__.py**: Initializes the package so it can be imported as a module.
    - **analytics.py**: Analyzes temperature records (e.g., averages, trends, spikes).
    - **converter.py**: Handles temperature unit conversion logic.
    - **crud_temperature_records.py**: Manages create, read, update, and delete (CRUD) operations.
    - **generalutils.py**: Utility functions shared across different modules.
    - **record.py**: Defines the structure of a temperature record using a class.
## ▶️ **Sample Usage**
- Run main.py, you will see a menu-driven interface like:

![Run main](Images/RunTemperatureToolkit-1.png)

- Menu Options avaiable:

![Run main](Images/TemperatureToolkit-MenuOptions.png)

🖊️ Just type the number for the desired operation and follow the prompts!

## 📸 **Feature Demonstration**
1️⃣ Create New Temperature Record

**Record-1:**
![Create New Temperature Record](Images/Option-1-CreateNewTemperatureRecord.png)

**Result Post Temperature Record Creation:**
![Result Post Temperature Record Creation](Images/Option-1-CreateNewTemperatureRecord-Result.png)

**Record-2:**
![Create New Temperature Record-2](Images/Option-1-CreateNewTemperatureRecord-2.png)

---

2️⃣ View All Temperature Records

![View All Records](Images/Option-2-ViewAllTemperatureRecords.png)

---

3️⃣ Modify Existing Temperature Record
**Select record for updation and modify record**
![Modify Record](Images/Option-3-ModifyExistingTemperatureRecord.png)

**Result Post Modification**
![Result Post Modification](Images/Option-3-ModifyExistingTemperatureRecord-Result.png)

---

4️⃣ Delete Existing Temperature Record

![Delete Record](Images/Option-4-DeleteExistingTemperatureRecord-Result.png)

---

5️⃣ Convert Temperatures of Selected Day

![Convert Temperature](Images/Option-5-ConvertTemperaturesScaleOfSelectedDay.png)

---

6️⃣ Show Temperature Summary - All Days

![Summary Report](Images/Option-6-ShowTemeraturesSummary-AllDays-Result.png)

---

7️⃣ Check If Temperatures Are Above a Threshold (Selected Day) 

![Check Threshold](Images/Option-7-CheckTemperaturesAboveaGivenThreshold.png)

----

8️⃣ Average Temperature - All Days  
![Average Temperature](Images/Option-8-AverageTemperature-AllDays.png)

---

9️⃣ Show Hottest Day  
![Hottest Day](Images/Option-9-ShowHottestDay.png)

---

🔟 Extreme Days Above a Threshold  
![Extreme Days](Images/Option-10-ShowDayswithRecordedTemperatureAboveaThreshold.png)

---

1️⃣1️⃣ Show Temperature Ranges - All Days  
![Temperature Ranges](Images/Option-11-ShowTemperatureRanges-AllDays.png)

---

1️⃣2️⃣ Show Temperature Trend  
![Temperature Trend](Images/Option-12-ShowTemperatureTrend.png)

---

1️⃣3️⃣ Detect Spike  
![Detect Spike](Images/Option-13-DetectSpike.png)

---

1️⃣4️⃣ Exit  
![Exit](Images/Option-14-Exit.png)



## ⚙️ **How to Run Locally**
1. **Clone the repository:**
    1. git clone https://github.com/username/temperature-toolkit.git
    2. cd temperature-toolkit
2. **Run the main script:**
    python main.py
3. **(Optional) Open the Jupyter Notebook for testing:**
    jupyter notebook Test-Temperature-Toolkit.ipynb
## 📚 **Learning Outcomes**
This project helped me:

🧠 Strengthen core Python skills

📋 Practice list-based data handling

🔁 Build reusable, modular code using OOP principles

💻 Design a user-friendly, menu-driven CLI tool