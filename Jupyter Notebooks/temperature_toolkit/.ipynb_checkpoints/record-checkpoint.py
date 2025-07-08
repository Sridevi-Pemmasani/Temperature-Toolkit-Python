from temperature_toolkit.converter import convert

class TemperatureRecord:
    def __init__(self, date, readings, scale):
        self.date = date
        self.readings = readings if readings else []
        self.scale = scale.lower()

    def get_summary(self):
        if not self.readings:
            return {'date': self.date, 'scale': self.scale, 'min': 0, 'max': 0, 'avg': 0}
        return {
            'date': self.date,
            'scale': self.scale,
            'min': round(min(self.readings), 2),
            'max': round(max(self.readings), 2),
            'avg': round(sum(self.readings) / len(self.readings), 2)
        }

    # Converts all readings of a selected record to the target scale (in-place)
    def convert_to(self, target_scale):
        target_scale = target_scale.lower()
        if target_scale == self.scale:
            return
        self.readings = [convert(temp, self.scale, target_scale) for temp in self.readings]
        self.scale = target_scale

    # Purpose: Checks if every single reading is above a fixed threshold.
    def is_above_threshold(self, threshold):
        return all(temp > threshold for temp in self.readings)