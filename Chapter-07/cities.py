prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city_name = input(prompt)

    if city_name == 'quit':
        break
    else:
        print(f"I'd love to go to {city_name.title()}!")
