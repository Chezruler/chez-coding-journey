while True:
    unit = input("Please enter the unit (C/F): ")
    temp = float(input("Please enter temperature: "))

    try:
        if unit == "C":
            temp = round((9 * temp) / 5 + 32, 1)
            print(f"the temperature in Fahrenheit is {temp} F°")
        elif unit == "F":
            temp = round((temp - 32) * 5 / 9)
            print(f"the temperature in Celcius is {temp} C°")
        else:
            print(f"Please enter a right unit, {unit} is not a right unit.")
    except ValueError:
        print("In my system a problem got in the way, please try again or contact the coder.")
        break
