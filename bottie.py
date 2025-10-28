from datetime import datetime

bot_name="Bottie"
print(f"Hello! My name is {bot_name}. Please tell me what's your name?")
name = input("Type name here: ")
print(f"nice to meet you, {name}!")

print(f"how old are you, {name}?")
age=input("Type age here: ")
bot_creation_year=2025
bot_age=datetime.now().year - bot_creation_year
print(f"Oh, you're {int(age)-int(bot_age)} oder than me, because you see, I'm just {bot_age} years old, I was created in {bot_creation_year}.")
print(f"{name}, what is your favorite color?")
color=input("Type color here: ")
print(f"wow, {color} is a beautiful color. ")
print(f"thanks for talking to me, {name}, seeya again!")