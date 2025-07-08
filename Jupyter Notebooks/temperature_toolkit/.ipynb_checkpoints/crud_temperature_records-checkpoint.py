from temperature_toolkit.record import TemperatureRecord
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter.ttk import Label
from tkinter import messagebox
from datetime import date, datetime

# Started consolidated i/p for temperature capture
def get_full_temperature_input(records,record_index=None, existing_date=None, existing_readings=None, existing_scale="celsius"):

    result = None
    # This code runs on click of submit button in the dialogox
    def on_submit():
        nonlocal result
        try:
            selected_date = cal.get_date().strftime("%Y-%m-%d")
            # Check for duplicates excluding the current record
            if records:
                for i, rec in enumerate(records):
                    if rec.date == selected_date and i != record_index:
                        raise ValueError(f"A record already exists for date {selected_date}.")

          
            scale_val = scale_var.get()

            # Extract values and validate
            temp_vals = []
            for i, e in enumerate(temp_entries):
                val = e.get().strip()
                if val == "":
                    raise ValueError(f"Temperature reading {i+1} is empty.")

                try:
                    temp_vals.append(float(val))
                except ValueError:
                    raise ValueError(f"Temperature reading {i+1} is not a valid number.")
            
            
            if len(temp_vals) != 6:
                raise ValueError("Exactly 6 temperature readings are required.")         
          
            result = (selected_date, temp_vals, scale_val)
            root.destroy()
        except Exception as e:
            messagebox.showerror("Input Error", str(e))
    
    # To Handle Record updation
    if record_index is not None:
        try:
            existing_record = records[record_index]
            existing_date = existing_record.date
            existing_readings = existing_record.readings
            existing_scale = existing_record.scale
        except IndexError:
            print("Invalid record index.")
            return None
            
    # Preparing Dialoag Window to capture Date, Temperature Reading and Scale
    root = tk.Tk()
    root.title("Enter Temperature Record")
    root.geometry("500x600")

    # Add Date picker
    tk.Label(root, text="Select Record Date:").pack()
    cal = DateEntry(root, maxdate=date.today(), width=20)
    cal.pack(pady=5)

    # Ensure existing_date is defined
    if existing_date:
        try:
            # Convert string to datetime object if necessary
            if isinstance(existing_date, str):
                date_obj = datetime.strptime(existing_date, "%Y-%m-%d").date()
            else:
                date_obj = existing_date
            cal.set_date(date_obj)
        except Exception as e:
            print(f"Invalid date format for existing_date: {e}")
            # Optionally: set to today or skip setting
            pass
    else:
        cal.set_date(datetime.today().date())

    # Temperature inputs
    tk.Label(root, text="Enter 6 Temperature Readings:").pack()
    temp_entries = []
    for i in range(6):
        e = tk.Entry(root)
        e.pack(pady=2)
        if existing_readings and i < len(existing_readings):
            e.insert(0, str(existing_readings[i]))
        temp_entries.append(e)

    # Scale dropdown
    tk.Label(root, text="Select Temperature Scale:").pack()
    scale_var = tk.StringVar()
    #scale_var.set("celsius")  # default
    scale_var.set(existing_scale if existing_scale else 'celsius')
    # tk.OptionMenu(root, scale_var, "celsius", "fahrenheit", "kelvin").pack(pady=10)
   
    options = ['celsius', 'fahrenheit', 'kelvin']

    dropdown = ttk.Combobox(root, values=options, state="readonly", textvariable=scale_var)
    if existing_scale in options:
        dropdown.current(options.index(existing_scale))
    else:
        dropdown.current(0)    

    dropdown.pack(pady=5)
    
    # Submit
    tk.Button(root, text="Submit", command=on_submit).pack(pady=20)

    root.mainloop()
    return result


# Creates a new temperature record.
def create_new_record(records):
    result = get_full_temperature_input(records)
    if result is not None:
        date, readings, scale = result
        record = TemperatureRecord(date, readings, scale)
        records.append(record)
        print("Record added successfully for the date: ", date)
    
# View all temperature records
def view_available_records(records):
    print("\nAvailable Records:")
    for idx, record in enumerate(records):
        print(f"{idx}: Date = {record.date}, Readings = {record.readings}, Scale = {record.scale}")

# Update an existing temperature record
def update_existing_record(records,index):
    new_date, new_readings, new_scale = get_full_temperature_input(records,record_index=index)

    records[index].date = new_date
    records[index].readings = new_readings
    records[index].scale = new_scale.lower()
    print("Record updated successfully for the date: ", new_date)

# Delete an existing temperature record
def delete_existing_record(records,index):
    deleted = records.pop(index)
    print(f"Record for {deleted.date} deleted successfully.")
        