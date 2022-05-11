from weatherStation import Weather_station
from displayDevice import Forecast
from displayDevice import Statistics
from displayDevice import CurrentConditions


if __name__ == "__main__":
	ws = Weather_station()
	f = Forecast()
	s = Statistics()
	cc = CurrentConditions()
	ws.subscribe(f)
	ws.subscribe(s)
	ws.subscribe(cc)
	ws.set_attributes(10,20,30)
	ws.set_attributes(11,21,31)
	ws.set_attributes(12,22,32)
	ws.set_attributes(13,23,33)