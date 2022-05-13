from publisher import Publisher

class WeatherStation(Publisher):
    def __init__(self):
        super().__init__()
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def notify(self, *args, **kwargs):
        for subscriber in self.subscribers:
            subscriber.update(self.temperature, self.humidity, self.pressure)

    def set_attributes(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify()

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

    def get_attributes(self):
        return (self.temperature, self.humidity, self.pressure)
