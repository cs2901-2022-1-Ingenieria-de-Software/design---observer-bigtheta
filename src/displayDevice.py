from observer import Observer
from sklearn.linear_model import LinearRegression
from numpy import reshape,array,append


class Forecast(Observer):
	def __init__(self):
		self.past_temperature = array([])
		self.past_humidity  = array([])
		self.past_pressure  = array([])
		self.xs  = array([])
		
	def update(self ,temperature, humidity, pressure):
		self.past_temperature =append(self.past_temperature,temperature)
		self.past_humidity =append(self.past_humidity,humidity)
		self.past_pressure =append(self.past_pressure,pressure)
		self.xs=append(self.xs,len(self.xs))
		print("Forecast: updated future values", self.get_future()) 

	def get_future(self):
		ft = LinearRegression()
		ft.fit(reshape(self.xs,newshape=(-1,1)), reshape(self.past_temperature,newshape=(-1,1)))
		fh = LinearRegression()
		ft.fit(reshape(self.xs,newshape=(-1,1)), reshape(self.past_humidity,newshape=(-1,1)))
		fp = LinearRegression()
		ft.fit(reshape(self.xs,newshape=(-1,1)), reshape(self.past_pressure,newshape=(-1,1)))
		return(ft.predict(len(self.xs)), fh.predict(len(self.xs)), fp.predict(len(self.xs)))

class CurrentConditions(Observer):
	def __init__(self):
		self.current_temperature = 0
		self.current_humidity = 0
		self.current_pressure = 0

	def update(self ,temperature, humidity, pressure):
		self.current_temperature = temperature
		self.current_humidity = humidity
		self.current_pressure = pressure
		print("Current_conditions: updated current conditions:",self.get_all())

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
		return (self.mean(self.past_temperature),self.mean(self.past_humidity),self.mean(self.past_pressure))

	def update(self ,temperature, humidity, pressure):
		self.past_temperature.append(temperature)
		self.past_humidity.append(humidity)
		self.past_pressure.append(pressure)
		print("Statistics: updated mean:",self.all_mean())
	
