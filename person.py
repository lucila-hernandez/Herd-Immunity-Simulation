import random
#random.seed(42)
from virus import Virus

class Person(object):
    """Represents a person in the simulation"""
    def __init__(self, _id, is_vaccinated, infection=None):
        self._id = _id  
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_alive = True

    def did_survive_infection(self):
        """Determines if the person survives the infection. Generates random number between 0.0-1.0, if number is less than mortality rate the person has passed away. Otherwise, the person has survived infection and are now vaccinated."""
        if self.infection: 
            survival_chance = random.random()
            print(f"Person {self._id} has an infection. Survival chance: {survival_chance}, Mortality rate: {self.infection.mortality_rate}")
            if survival_chance < self.infection.mortality_rate:
                self.is_alive = False
                self.infection = None
                print(f"Person {self._id} did not survive.")
                return False
            else:
                self.is_vaccinated = True
                self.infection = None
                print(f"Person {self._id} survived and is now vaccinated.")
                return True
        return True    

if __name__ == "__main__":
    """Section to test the Person Class"""

    # Defined a vaccinated person and checked their attributes
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Created an unvaccinated person and tested their attributes
    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    # Created a Virus object for testing
    virus = Virus("Dysentery", 0.7, 0.2)

    # Created an infected person and tested their attributes
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection == virus

    # Created a list of 100 infected people for survival tests
    people = []
    for i in range(1, 100):
        person = Person(i, False, virus)
        people.append(person)

    # Counted the people that survived and did not survived
    did_survive = 0
    did_not_survive = 0

    for person in people:
        survived = person.did_survive_infection()
        if survived:
            did_survive += 1
        else:
            did_not_survive += 1

    print(f"Survived: {did_survive}")
    print(f"Did not survive: {did_not_survive}")

    # Tested that a person who survives an infection becomes vaccinated
    virus = Virus("TestVirus", 0.3, 0.5)  # 50% mortality rate
    person = Person(5, False, virus)
    survived = person.did_survive_infection()

    if survived:
        person.infection = virus
        reinfection_result = person.did_survive_infection()
        assert reinfection_result is True
        assert person.is_alive is True
        assert person.is_vaccinated is True
        assert person.infection is None