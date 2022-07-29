# int
  #number=10
# float
  #sum=100.5
# str
  #name='Abraham'
# bool
#   #status=False 

# import random


# random_number = random.randint(1,2)
# user_number = input('Guess the number from 1 to 3 :')

 
# if user_number == random_number:
#     print('You guessed it')
# else:

# 	print('вы не отгадали')
# 	print(f'было загадано число{random_number}')
# # 		# if user_number < random_number:
# # 		# 	print('это число меньше')
# #         # else:


import python_weather
import asyncio


async def getweather():
  # declare the client. format defaults to metric system (celcius, km/h, etc.)
  client = python_weather.Client(format=python_weather.IMPERIAL, locale='ru-RU')

  # fetch a weather forecast from a city
  weather = await client.find("latvia")

  # returns the current day's forecast temperature (int)
  celsius=(weather.current.temperature-32)/1.8
  print(round(celsius))
  # print(weather.current.temperature)

  # get the weather forecast for a few days
  for forecast in weather.forecasts:
    print(str(forecast.date), forecast.sky_text, forecast.temperature)

  # close the wrapper once done
  await client.close()

if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  loop.run_until_complete(getweather())
