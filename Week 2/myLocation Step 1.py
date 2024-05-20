class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country
loc = Location("Ercan", "United Kingdom")
print(loc.name)
print(loc.country)
print(type(loc))