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