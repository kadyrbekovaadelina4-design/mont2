class Distance:
    C0ONVERSION_TO_METERS = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0
    }

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return str(self.value)+ self.unit

    def to_meters(self):
        return self.value * self.C0ONVERSION_TO_METERS[self.unit]

    def from_meters(self, meters, target_unit):
        return meters/ self.C0ONVERSION_TO_METERS[target_unit]

    def __add__(self, other):
        total_meters = self.to_meters() + other.to_meters()
        new_value = self.from_meters(total_meters, self.unit)
        return Distance(new_value, self.unit)

    def __sub__(self, other):
        result_meters = self.to_meters() - other.to_meters()
        new_value = self.from_meters(result_meters, self.unit)
        return Distance(new_value, self.unit)

d1 = Distance(10, 'm')
d2 = Distance(2, 'km')
d3 = Distance(500, 'cm')
d4 = Distance(10000, 'mm')


print(d1,d2,d3,d4)

print(d1 + d2)
print(d3+d4)

print(d1 - d2)
print(d3-d4)
