def main():
    Fahrenheit= int(input("Enter temperature in Fahrenheit"))
    Celsius= (Fahrenheit-32)*5/9
    print("Fahrenheit", Fahrenheit)
    print("Celsius", Celsius)
    user = input("do you want to continue?")
    if user == "No" or user == 'no':
        print("Later")
    else:
        main()
main()