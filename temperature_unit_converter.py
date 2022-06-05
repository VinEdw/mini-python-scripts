# Temperature unit converter

class Temperature:
    def __init__(self, value: float, unit: str):
        if unit == 'C':
            self.celcius = value
        elif unit == 'F':
            self.celcius = (value - 32) / 1.8
        elif unit == 'K':
            self.celcius = value - 273.15
        elif unit == 'R':
            self.celcius = (value / 1.8) - 273.15
        else:
            raise ValueError('Invalid temperature unit entered. Unit must be C, F, K, or R.')
        
        self.fahrenheit = self.celcius * 1.8 + 32
        self.kelvin = self.celcius + 273.15
        self.rankine = self.kelvin * 1.8
    
    def getTemperatureDict(self):
        return {'C': self.celcius, 'F': self.fahrenheit, 'K': self.kelvin, 'R': self.rankine}


if __name__ == '__main__':
    print('Welcome')
    val = input('Input a temperature value with units:  ')
    num = float(val.split()[0])
    unit = val.split()[1]
    temp = Temperature(num, unit)
    print(temp.getTemperatureDict())