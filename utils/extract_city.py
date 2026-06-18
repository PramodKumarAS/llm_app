def extract_city(question):

    cities = [
        "hyderabad",
        "bangalore",
        "mumbai",
        "delhi"
    ]

    question = question.lower()

    for city in cities:
        if city in question:
            return city

    return None