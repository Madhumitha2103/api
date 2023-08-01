from weather_api import get_weather_data

def print_weather(data):
    print("Temperature:", data["main"]["temp"])
    print("Wind speed:", data["wind"]["speed"])
    print("Pressure:", data["main"]["pressure"])

def main():
    city = "London,us"
    while True:
        print("1. Get weather")
        print("2. Get wind speed")
        print("3. Get pressure")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            date = input("Enter the date: ")
            data = get_weather_data(city, date)
            print_weather(data)
        elif choice == "2":
            date = input("Enter the date: ")
            data = get_weather_data(city, date)
            print("Wind speed:", data["wind"]["speed"])
        elif choice == "3":
            date = input("Enter the date: ")
            data = get_weather_data(city, date)
            print("Pressure:", data["main"]["pressure"])
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
