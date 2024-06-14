from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Japlin' work?"""
    formatted_name = get_formatted_name("Janis", "Joplin")
    assert formatted_name == "Janis Joplin"

def test_first_last_middle_name():
    """Do names like Olamide Michael Adu work?"""
    formatted_name = get_formatted_name("Olamide", "Adu", "Michael")
    assert formatted_name == "Olamide Michael Adu"