import random
from person import Person
from logger import Logger
from virus import Virus

class Simulation(object):
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        """Initializes a new simulation intance."""
        self.logger = Logger('simulation_log.txt')
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.newly_infected = []

        self.logger.write_metadata(pop_size, vacc_percentage, virus.name, virus.mortality_rate, virus.repro_rate)

    def _create_population(self):
        """Creates the initial population with a mix of healthy, vaccinated, and infected individuals."""
        population = []
        for i in range(self.pop_size):
            if i < self.initial_infected:
                person = Person(i, False, self.virus)
                print(f"Initial infected: Person {person._id} is infected with {self.virus.name}")
                population.append(person)
            elif i < self.pop_size * self.vacc_percentage:
                person = Person(i, True)
                print(f"Vaccinated person: {person._id}")
                population.append(person)
            else:
                person = Person(i, False)
                print(f"Healthy unvaccinated person: {person._id}")
                population.append(person)
        return population

    def _simulation_should_continue(self):
        """Determines if a simulation should continue."""
        alive_infected = sum(1 for person in self.population if person.is_alive and person.infection)
        alive_not_vaccinated = sum(1 for person in self.population if person.is_alive and not person.is_vaccinated)
        should_continue = alive_infected > 0 and alive_not_vaccinated > 0
        return should_continue

    def run(self):
        """Runs the simulation until it should no longer continue."""
        time_step_counter = 0
        should_continue = True

        while should_continue:
            time_step_counter += 1
            self.time_step(time_step_counter)
            should_continue = self._simulation_should_continue()

        final_alive_count = len([p for p in self.population if p.is_alive])
        final_dead_count = len([p for p in self.population if not p.is_alive])
        self.logger.log_infection_survival(time_step_counter, final_alive_count, final_dead_count)

    def time_step(self, time_step_counter):
        """Simulates a single time step in the simulation"""
        interactions = 0
        new_fatalities = 0

        for person in self.population:
            if person.infection:
                for _ in range(100):  
                    other_person = random.choice(self.population)
                    interactions += 1
                    if other_person.is_alive:
                        self.interaction(person, other_person)

        new_infections = len(self.newly_infected)
        self._infect_newly_infected()
        self.logger.log_interactions(time_step_counter, interactions, new_infections)

        for person in self.population:
            if person.infection and person.is_alive:
                survived = person.did_survive_infection()
                if not survived:
                    new_fatalities += 1

        self.logger.log_infection_survival(time_step_counter, len(self.population), new_fatalities)

    def interaction(self, infected_person, random_person):
        """Simulates an interaction between an infected person and a random person."""
        if random_person.is_alive:
            if random_person.is_vaccinated or random_person.infection:
                return
            else:
                infection_chance = random.random()
                if infection_chance < self.virus.repro_rate:
                    self.newly_infected.append(random_person)

    def _infect_newly_infected(self):
        """Infects all newly infected individuals."""
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = []

if __name__ == "__main__":
    # Testing simulation here
    virus_name = "Sniffles"
    repro_num = 0.5  
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Sets some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Makes a new instance of the imulation
    sim = Simulation(pop_size, vacc_percentage, virus, initial_infected)
    sim.run()
