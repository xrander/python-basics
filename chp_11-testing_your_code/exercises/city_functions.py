def get_city_country(city, country, population = ""):
    """A function to print city and country with a comma in between"""
    if population:  
        city_country = f"{city.title()}, {country.title()} - Population {population}"
    else:
        city_country = f"{city.title()}, {country.title()}"
    return city_country