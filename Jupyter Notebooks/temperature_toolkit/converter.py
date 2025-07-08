# converts a single temperature value from one scale to another.
def convert(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit == to_unit:
        return round(value, 2)

    # Convert to Celsius first
    if from_unit == 'fahrenheit':
        value = (value - 32) * 5/9
    elif from_unit == 'kelvin':
        value = value - 273.15

    # Convert from Celsius to target
    if to_unit == 'fahrenheit':
        return round((value * 9/5) + 32, 2)
    elif to_unit == 'kelvin':
        return round(value + 273.15, 2)
    elif to_unit == 'celsius':
        return round(value, 2)
    else:
        raise ValueError("Invalid temperature scale")