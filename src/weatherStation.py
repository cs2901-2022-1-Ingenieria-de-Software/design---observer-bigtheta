from publisher import Publisher

class Weather_station(Publisher):
	def __init__(self):
		super().__init__()
		self.temperature = 0
		self.humidity = 0
		self.pressure = 0


	def notify(self, *args, **kwargs):
		for subscriber in self.subscribers:
			subscriber.update(self.temperature,self.humidity,self.pressure)

	def set_attributes(self, temperature, humidity, pressure):
		self.temperature = temperature
		self.humidity = humidity
		self.pressure = pressure
		self.notify()