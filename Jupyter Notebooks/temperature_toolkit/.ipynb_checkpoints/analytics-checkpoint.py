'''
def convert_temperature_record():
    if not records:
        print("No temperature records found.")
        return

    print("\nAvailable Records:")
    for idx, record in enumerate(records):
        print(f"{idx}: Date = {record.date}, Scale = {record.scale}, Readings = {record.readings}")

    try:
        index = int(input("Enter the index of the record to convert: "))
        if index < 0 or index >= len(records):
            print("Invalid record index.")
            return

        target_scale = input("Enter the target temperature scale (celsius/fahrenheit/kelvin): ").strip().lower()
        if target_scale not in ['celsius', 'fahrenheit', 'kelvin']:
            print("Invalid temperature scale.")
            return

        selected_record = records[index]
        selected_record.convert_to(target_scale)

        print(f"Record updated successfully to {target_scale}:")
        print(f"Updated Readings: {selected_record.readings}")

    except ValueError:
        print("Invalid input. Please enter numeric index and valid temperature values.")


def show_summary():
    if not records:
        print("No records to show.")
        return

    print("\nTemperature Record Summaries:")
    for record in records:
        summary = record.get_summary()
        print(f"Date: {summary['date']}, Scale: {summary['scale']}, "
              f"Min: {summary['min']}, Max: {summary['max']}, Avg: {summary['avg']}")


def check_above_threshold():
    if not records:
        print("No records available.")
        return

    print("\nAvailable Records:")
    for idx, record in enumerate(records):
        print(f"{idx}: Date = {record.date}, Scale = {record.scale}")

    try:
        index = int(input("Enter the index of the record to check: "))
        if index < 0 or index >= len(records):
            print("Invalid index.")
            return

        threshold = float(input("Enter the threshold temperature: "))
        selected_record = records[index]
        result = selected_record.is_above_threshold(threshold)

        if result:
            print(f"All readings in the record for {selected_record.date} are above {threshold}.")
        else:
            print(f"Not all readings in the record for {selected_record.date} are above {threshold}.")

    except ValueError:
        print("Invalid input.")

def show_average_temperature():
    if not records:
        print("No records available to calculate average.")
        return

    avg_temp = average_temperature_across_days(records)
    print(f"\nOverall average temperature across all records: {avg_temp}")

def show_hottest_day():
    if not records:
        print("No records available to determine the hottest day.")
        return

    hottest = hottest_day(records)
    print(f"The hottest day based on average temperature is: {hottest}")

def show_extreme_days():
    if not records:
        print("No records available.")
        return

    try:
        threshold = float(input("Enter the temperature threshold: "))
        extreme_days = detect_extreme_days(records, threshold)

        if extreme_days:
            print(f"\nDays with temperatures above {threshold}:")
            for day in extreme_days:
                print(day)
        else:
            print(f"No days exceed the threshold of {threshold}.")

    except ValueError:
        print("Invalid threshold value.")

def show_temperature_ranges():
    if not records:
        print("No records available to show temperature ranges.")
        return

    ranges = temperature_range_for_each_day(records)
    if ranges:
        print("\nTemperature ranges for each day:")
        for date, (min_temp, max_temp) in ranges.items():
            print(f"Date: {date}, Min: {min_temp}, Max: {max_temp}")
    else:
        print("No temperature records available.")

def show_temperature_trend():
    if not records:
        print("No records available.")
        return

    print("\nAvailable Records:")
    for idx, record in enumerate(records):
        print(f"{idx}: Date = {record.date}, Scale = {record.scale}")

    try:
        index = int(input("Enter the index of the record to view the temperature trend: "))
        if index < 0 or index >= len(records):
            print("Invalid index.")
            return

        selected_record = records[index]
        trend = temperature_trend(selected_record.readings)

        if trend:
            print(f"\nTemperature trend for {selected_record.date}:")
            print(" -> ".join(trend))
        else:
            print("No temperature readings available to calculate trend.")

    except ValueError:
        print("Invalid input.")

def check_for_spike():
    if not records:
        print("No records available.")
        return

    print("\nAvailable Records:")
    for idx, record in enumerate(records):
        print(f"{idx}: Date = {record.date}, Scale = {record.scale}")

    try:
        index = int(input("Enter the index of the record to check for spike: "))
        if index < 0 or index >= len(records):
            print("Invalid index.")
            return

        selected_record = records[index]
        threshold = float(input("Enter the temperature difference threshold: "))

        has_spike = detect_spike(selected_record.readings, threshold=threshold)

        if has_spike:
            print(f"Temperature spike detected in record for {selected_record.date}.")
        else:
            print(f"No spike detected in record for {selected_record.date}.")

    except ValueError:
        print("Invalid input.")

'''

# Should be in Analytics.py file
def average_temperature_across_days(records):
    all_readings = [temp for record in records for temp in record.readings]
    if not all_readings:
        return 0
    return round(sum(all_readings) / len(all_readings), 2)

def hottest_day(records):
    if not records:
        return ''
    max_avg = float('-inf')
    hottest = ''
    for record in records:
        if record.readings:
            avg = sum(record.readings) / len(record.readings)
            if avg > max_avg:
                max_avg = avg
                hottest = record.date
    return hottest

def detect_extreme_days(records, threshold):
    return [record.date for record in records if any(temp > threshold for temp in record.readings)]

def temperature_range_for_each_day(records):
    return {record.date: (min(record.readings), max(record.readings)) if record.readings else (0, 0) for record in records}

def temperature_trend(temps):
    trend = []
    for i in range(1, len(temps)):
        if temps[i] > temps[i-1]:
            trend.append('up')
        elif temps[i] < temps[i-1]:
            trend.append('down')
        else:
            trend.append('same')
    return trend

# Purpose: Detects if there is a sudden jump or drop between consecutive readings.
# Use Case: Spikes, anomalies, or sensor glitches.
# Example Use: "Alert if temperature changes abruptly by ≥5°C between any two readings."
def detect_spike(temps, *, threshold=5):
    for i in range(1, len(temps)):
        if abs(temps[i] - temps[i-1]) >= threshold:
            return True
    return False