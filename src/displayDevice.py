from observer import Observer

class Forecast(Observer):
	def __init__(self):
		self.future_temperature = 0
		self.future_humidity = 0
		self.future_pressure = 0
		
	def update(self ,temperature, humidity, pressure):
		self.future_temperature = temperature
		self.future_humidity = humidity
		self.future_pressure = pressure
		print("Forecast: updated")

class Current_conditions(Observer):
	def __init__(self):
		self.current_temperature = 0
		self.current_humidity = 0
		self.current_pressure = 0

	def update(self ,temperature, humidity, pressure):
		current_temperature = temperature
		current_humidity = humidity
		current_pressure = pressure
		print("Current_conditions: updated")

class Statistics(Observer):
	def __init__(self):
		self.past_temperature = 0
		self.past_humidity = 0
		self.past_pressure = 0

	def update(self ,temperature, humidity, pressure):
		past_temperature = temperature
		past_humidity = humidity
		past_pressure = pressure
		print("Statistics: updated")