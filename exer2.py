class Temperature:
    unit = "Celsius"

    def __init__(self, value):
        self.value = value
    def display(self):
        print(self.unit, self.value)

    @classmethod
    def change_unit(cls, new_unit):
        cls.unit = new_unit

    @staticmethod
    def to_fahrenheit(celsius):
        return celsius * (9/5) + 32

t1 = Temperature(100)
t1.display()

print(Temperature.to_fahrenheit(100))

Temperature.change_unit("Kelvin")
t1.display()

# D: Because 'unit' is a Class attribute