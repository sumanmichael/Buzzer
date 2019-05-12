import pyowm

owm = pyowm.OWM('') #OpenWeatherMap API_Key here

def get_data(txt_log,place):
	try:
		observation = owm.weather_at_place(place)
		w = observation.get_weather()
		data = "Location: "+place+"\nStatus: "+str(w.get_detailed_status())+"\n"+"Temp :"+str(w.get_temperature('celsius')['temp'])+" C\n"+"Max. Temp : "+str(w.get_temperature('celsius')['temp_max'])+" C\n"+"Min. Temp : "+str(w.get_temperature('celsius')['temp_min'])+" C\n"+"Wind Speed: "+str(w.get_wind()['speed'])+" \n"+"Humidity : "+str(w.get_humidity())+" \n"+"Pressure: "+str(w.get_pressure()['press'])+" \n"+"Sunrise at: "+str(w.get_sunrise_time('iso'))+" \n"+"Sunset at: "+str(w.get_sunset_time('iso'))+" \n"
		txt_log.AppendText("\nWeather Report:\n\n"+data)
		return data
	except:
		txt_log.AppendText("Connection Failed with Weather Server - II ...\n\n")

def loc(txt_log,place):
	try:
		obs_search = owm.weather_at_places(place,searchtype='like')[0]
		obs_list = owm.weather_around_coords(obs_search.get_location().get_lat(),obs_search.get_location().get_lon())
		txt_log.AppendText("Places Nearby:\n")
		for i in obs_list:
		    txt_log.AppendText(i.get_location().get_name()+'\n')

	except:
		txt_log.AppendText("Connection Failed with Weather Server - I ...\n\n")
