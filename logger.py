import datetime

class Logger(object):
    """Logs information about the simulation's progress and results."""

    def __init__(self, file_name):
        """Initializes the logger with the given file name."""
        self.file_name = file_name
        with open(self.file_name, 'w') as file:
            pass

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num, initial_infected):
        """Logs the initial metadata before the simulation begins."""
        with open(self.file_name, 'a') as file:
            file.write(f"Simulation run date: {datetime.datetime.now()}\n")
            file.write(f"Population size: {pop_size}\n")
            file.write(f"Initial number of infected people: {initial_infected}\n")
            file.write(f"Virus Name: {virus_name}\n")
            file.write(f"Mortality Rate: {mortality_rate}\n")
            file.write(f"Reproduction Rate: {basic_repro_num}\n\n")

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        """Logs the number of interactions and new infections at each step."""
        with open(self.file_name, 'a') as file:
            file.write(f"Step Number: {step_number}\n")
            file.write(f"Number of Interactions: {number_of_interactions}\n")
            file.write(f"Number of New Infections: {number_of_new_infections}\n\n")

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities, total_living, total_dead, total_vaccinated):
        """Logs the infection survival results at each step."""
        with open(self.file_name, 'a') as file:
            file.write(f"Step Number: {step_number}\n")
            file.write(f"Population Count: {population_count}\n")
            file.write(f"Number of New Fatalities: {number_of_new_fatalities}\n")
            file.write(f"Total Living: {total_living}\n")
            file.write(f"Total Dead: {total_dead}\n")
            file.write(f"Total Vaccinated: {total_vaccinated}\n\n")

    def write_final_summary(self, final_alive_count, final_dead_count, total_vaccinated, total_interactions):
        """Logs the final summary of the simulation results."""
        with open(self.file_name, 'a') as file:
            file.write("Summary of the simulation:\n")
            file.write(f"Total living: {final_alive_count}\n")
            file.write(f"Total dead: {final_dead_count}\n")
            file.write(f"Number of vaccinations: {total_vaccinated}\n")
            file.write(f"Total interactions: {total_interactions}\n")
            file.write("Simulation ended because there are no new infections.\n\n")
