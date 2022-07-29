import python_weather
# import asyncio


from asyncore import dispatcher
from aiogram import Bot,Dispatcher,executor,types

bot = Bot(token='5440672041:AAEQ7yKAYzt1aVWs8M3zAiAfj1Jcb1WZwKs')
dp=Dispatcher(bot)

client = python_weather.Client(format=python_weather.IMPERIAL, locale='ru-RU')

@dp.message_handler()
async def echo(message: types.Message):
	weather = await client.find(message.text)
	celsius = round((weather.current.temperature-32)/1.8)
    
	resp_msg=weather.location_name + '\n'
	resp_msg+=f'Температура воздуха: {celsius}\n'
	resp_msg+=f'Погода: {weather.current.sky_text}'
    
	await message.answer (resp_msg)

if __name__=="__main__":
	executor.start_polling(dp,skip_updates=True)

	# await client.close()
