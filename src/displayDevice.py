from observer import Observer
from sklearn.linear_model import LinearRegression
import numpy as np

class Forecast(Observer):
    def __init__(self):
        self.past_temperature = np.array([])
        self.past_humidity = np.array([])
        self.past_pressure = np.array([])
        self.xs = np.array([])

    def update(self, temperature, humidity, pressure):
        self.past_temperature = np.append(self.past_temperature , temperature)
        self.past_humidity = np.append(self.past_humidity, humidity)
        self.past_pressure = np.append(self.past_pressure,  pressure)
        self.xs = np.append(self.xs, len(self.xs))
        print('Forecast: updated future values', self.get_future())
    
    def get_future(self):
        if len(self.xs) > 0:
            ft = LinearRegression()
            ft.fit(self.xs.reshape(-1, 1), self.past_temperature.reshape(-1, 1))
            fh = LinearRegression()
            fh.fit(self.xs.reshape(-1, 1), self.past_humidity.reshape(-1, 1))
            fp = LinearRegression()
            fp.fit(self.xs.reshape(-1, 1), self.past_pressure.reshape(-1, 1))

            future_temperature = ft.predict(self.xs.reshape(-1, 1))[len(self.xs) - 1][0]
            future_humidity = fh.predict(self.xs.reshape(-1, 1))[len(self.xs) - 1][0]
            future_pressure = fp.predict(self.xs.reshape(-1, 1))[len(self.xs) - 1][0]

            return (future_temperature, future_humidity, future_pressure)
        else:
            return (0, 0 , 0)

class CurrentConditions(Observer):
    def __init__(self):
        self.current_temperature = 0
        self.current_humidity = 0
        self.current_pressure = 0

    def update(self, temperature, humidity, pressure):
        self.current_temperature = temperature
        self.current_humidity = humidity
        self.current_pressure = pressure
        print('Current_conditions: updated current conditions:', self.get_all())

    def get_all(self):
        return (self.current_temperature, self.current_humidity, self.current_pressure)

class Statistics(Observer):
    def __init__(self):
        self.past_temperature = []
        self.past_humidity = []
        self.past_pressure = []

    def mean(self,values):
        return sum(values)/len(values)

    def all_mean(self):
        return (self.mean(self.past_temperature), self.mean(self.past_humidity), self.mean(self.past_pressure))

    def update(self ,temperature, humidity, pressure):
        self.past_temperature.append(temperature)
        self.past_humidity.append(humidity)
        self.past_pressure.append(pressure)
        print('Statistics: updated mean:', self.all_mean())
