# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов
class City:
    def __init__(self, name: str, population: int):
        self._name = name
        self._population = population

    def get_name(self):
        return self._name

    def get_population(self):
        return self._population


class Person:
    def __init__(self, room_number: int, street: str, country: str, planet: str):
        self._room_number = room_number
        self._street = street
        self._city = city.get_name()
        self._city_population = city.get_population()
        self._country = country
        self._planet = planet

    def get_person_planet(self):
        return self._planet

    def get_person_country(self):
        return self._country

    def get_person_city(self):
        return self._city

    def get_city_population(self):
        return self._city_population

    def get_person_street(self):
        return self._street

    def get_person_room(self):
        return self._room_number

    def person_data(self):
        return {"planet": self.get_person_planet(),
                "country": self.get_person_country(),
                "city": self.get_person_city(),
                "city population": self.get_city_population(),
                "street": self.get_person_street(),
                "room": self.get_person_room()
                }


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.


city = City("Moscow", 10_000_000)
person = Person(221, "Lenina", "Russia", "Earth")
print(person.person_data())
