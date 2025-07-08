from temperature_toolkit.record import TemperatureRecord
from temperature_toolkit.crud_temperature_records import *
from temperature_toolkit.analytics import *
import sys

# Process choosen operations from menu
def handle_menu_choice(choice,records):
    match choice:
        case "1": 
                create_new_record(records)
        case "2": 
                if not ensure_records_exist(records): return
                view_available_records(records)
        case "3":
                if not ensure_records_exist(records): return
                print_available_records(records)
                index = get_valid_index(records)
                if index is None: return
                update_existing_record(records,index)
        case "4":
                if not ensure_records_exist(records): return
                print_available_records(records)
                index = get_valid_index(records)
                if index is None: return
                delete_existing_record(records,index)
        case "5":
                if not ensure_records_exist(records): return
                print_available_records(records)
                index = get_valid_index(records)
                if index is None: return
                            
                # Input scale
                target_scale = input("Enter the temperature scale (celsius/fahrenheit/kelvin): ").strip().lower()
                if target_scale not in ["celsius", "fahrenheit", "kelvin"]:
                    print("Invalid scale. Must be 'celsius', 'fahrenheit', or 'kelvin'.")
                    return

                selected_record = records[index]
                selected_record.convert_to(target_scale)
                print(f"Record updated successfully to {target_scale}")
                print(f"Updated Readings: {selected_record.readings}")
        case "6":
                if not ensure_records_exist(records): return    
                print("\nTemperature Record Summaries:")
                for record in records:
                    summary = record.get_summary()
                    print(f"Date: {summary['date']}, Scale: {summary['scale']}, "
                    f"Min: {summary['min']}, Max: {summary['max']}, Avg: {summary['avg']}")
        case "7":
                if not ensure_records_exist(records): return
                print_available_records(records)
                index = get_valid_index(records)
                if index is None: return
                    
                threshold = float(input("Enter the threshold temperature: "))
                selected_record = records[index]
                result = selected_record.is_above_threshold(threshold)

                if result:
                    print(f"All readings in the record for {selected_record.date} are above {threshold}.")
                else:
                    print(f"Not all readings in the record for {selected_record.date} are above {threshold}.")
        case "8":
                if not ensure_records_exist(records): return
                avg_temp = average_temperature_across_days(records)
                print(f"\nOverall average temperature across all records: {avg_temp}")
        case "9":
                if not ensure_records_exist(records): return
                hottest = hottest_day(records)
                print(f"The hottest day based on average temperature is: {hottest}")
        case "10":
                if not ensure_records_exist(records): return
                    
                threshold = float(input("Enter the temperature threshold: "))
                extreme_days = detect_extreme_days(records, threshold)

                if extreme_days:
                    print(f"\nDays with temperatures above {threshold}:")
                    for day in extreme_days:
                        print(day)
                else:
                    print(f"No days exceed the threshold of {threshold}.")
        case "11":
                if not ensure_records_exist(records): return

                ranges = temperature_range_for_each_day(records)
                if ranges:
                    print("\nTemperature ranges for each day:")
                    for date, (min_temp, max_temp) in ranges.items():
                        print(f"Date: {date}, Min: {min_temp}, Max: {max_temp}")
                else:
                    print("No temperature records available.")
        case "12":
                if not ensure_records_exist(records): return
                print_available_records(records)
                index = get_valid_index(records)
                if index is None: return

                selected_record = records[index]
                trend = temperature_trend(selected_record.readings)

                if trend:
                    print(f"\nTemperature trend for {selected_record.date}:")
                    print(" -> ".join(trend))
                else:
                    print("No temperature readings available to calculate trend.")

        case "13":
                if not ensure_records_exist(records): return
                print_available_records(records)
                index = get_valid_index(records)
                if index is None: return

                selected_record = records[index]
                threshold = float(input("Enter the temperature difference threshold: "))

                has_spike = detect_spike(selected_record.readings, threshold=threshold)

                if has_spike:
                    print(f"Temperature spike detected in record for {selected_record.date}.")
                else:
                    print(f"No spike detected in record for {selected_record.date}.")
        case "14":
                print("Exiting program. Bye! Have a great day!")
                sys.exit()
        case _:
            print("Invalid choice. Please try again.")

# Common functions used throughout the other operations
def ensure_records_exist(records):
    if not records:
        print("No records available.")
        return False
    return True

def print_available_records(records):
    print("\nAvailable Records:")
    for idx, record in enumerate(records):
        print(f"{idx}: Date = {record.date}, Scale = {record.scale}")

def get_valid_index(records):
    try:
        index = int(input("Enter the index of the record: "))
        if index < 0 or index >= len(records):
            print("Invalid index.")
            return None
        return index
    except ValueError:
        print("Invalid input.")
        return None