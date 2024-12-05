class Logger(object):
    def __init__(self, file_name):
        """Logs information about the simulation's progress and results."""
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        """Shows the starting situation including: population, initial infected, the virus, and the initial vaccinated."""
        with open(self.file_name, 'w') as file:
            file.write(f"Population size: {pop_size}\n")
            file.write(f"Vaccination Percentage: {vacc_percentage}\n")
            file.write(f"Virus Name: {virus_name}\n")
            file.write(f"Mortality Rate: {mortality_rate}\n")
            file.write(f"Reproduction Rate: {basic_repro_num}\n")

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        """Shows person interactions"""
        with open(self.file_name, 'a') as file:
            file.write(f"Step Number: {step_number}\n")
            file.write(f"Number of Interactions: {number_of_interactions}\n")
            file.write(f"Number of New Infections: {number_of_new_infections}\n")

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        """Shows if the person either survived or died from infection"""
        with open(self.file_name, 'a') as file:
            file.write(f"Step Number: {step_number}\n")
            file.write(f"Population Count: {population_count}\n")
            file.write(f"Number of New Fatalities: {number_of_new_fatalities}\n")