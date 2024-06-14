from city_functions import get_city_country

def test_city_country():
    """Do a city + country name like Lagos, Nigeria works?"""
    format_city_country = get_city_country("lagos", "nigeria")
    assert format_city_country == "Lagos, Nigeria"

def test_city_country_population():
    """Do a city + country name + population like Lagos, Nigeria - Population 218000000 works?"""
    format_city_country = get_city_country("lagos", "nigeria", 218000000)
    assert format_city_country == "Lagos, Nigeria - Population 218000000"