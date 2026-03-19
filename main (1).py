from functions import (
    WeatherAppError,
    format_weather_output,
    get_city_coordinates,
    get_nsw_cities,
    get_weather,
)


def show_menu() -> None:
    print("NSW Cities Weather App")
    print("=" * 40)
    print("Choose a city by number or type a city name.\n")

    for index, city in enumerate(get_nsw_cities(), start=1):
        print(f"{index}. {city}")
    print()



def resolve_city_choice(user_input: str) -> str:
    cities = get_nsw_cities()

    if user_input.isdigit():
        city_number = int(user_input)
        if 1 <= city_number <= len(cities):
            return cities[city_number - 1]
        raise WeatherAppError("Invalid menu number selected.")

    if not user_input.strip():
        raise WeatherAppError("City input cannot be empty.")

    return user_input.strip()



def main() -> None:
    try:
        show_menu()
        user_input = input("Enter a city number or name: ")
        chosen_city = resolve_city_choice(user_input)

        location = get_city_coordinates(chosen_city)
        weather = get_weather(location["latitude"], location["longitude"])

        print(format_weather_output(location, weather))

    except WeatherAppError as exc:
        print(f"Error: {exc}")
    except KeyboardInterrupt:
        print("\nExited by user.")


if __name__ == "__main__":
    main()
