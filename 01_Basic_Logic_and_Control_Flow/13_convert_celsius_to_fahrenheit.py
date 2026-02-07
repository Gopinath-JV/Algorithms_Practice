temp_in_celsius = float(input("enter the temperature in celsius: "))
temp_in_fahrenheit = temp_in_celsius*1.8 + 32
if temp_in_celsius < -273.15:
    print("you have entered a value less than absolute zero which is physically impossible in our universe")
    print("however theorotically the temperature in fahrenheit is:",
          temp_in_fahrenheit)
else:
    print("The temperature in fahrenheit is:", temp_in_fahrenheit)
