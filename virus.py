class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        # Define the attributes of your your virus
        # TODO Define the other attributes of Virus
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate



# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    ebola_virus = Virus("Ebola", 1.9, 0.6)
    chickenpox_virus = Virus("Chickenpox", 0.8, 0.1)
    hiv_virus = Virus("HIV", 0.8, 0.3)

    assert hiv_virus.name == "HIV"
    assert hiv_virus.repro_rate == 0.8
    assert hiv_virus.mortality_rate == 0.3

    assert chickenpox_virus.name == "Chickenpox"
    assert chickenpox_virus.repro_rate == 0.8
    assert chickenpox_virus.mortality_rate == 0.1

    assert ebola_virus.name == "Ebola"
    assert ebola_virus.repro_rate == 1.9
    assert ebola_virus.mortality_rate == 0.6

    print(f"Ebola Virus: {ebola_virus.name}")
    print(f"Reproduction Rate: {ebola_virus.repro_rate}")
    print(f"Mortality Rate: {ebola_virus.mortality_rate}")

    print(f"Chickenpox Virus: {chickenpox_virus.name}")
    print(f"Reproduction Rate: {chickenpox_virus.repro_rate}")
    print(f"Mortality Rate: {chickenpox_virus.mortality_rate}")

    print(f"HIV Virus: {hiv_virus.name}")
    print(f"Reproduction Rate: {hiv_virus.repro_rate}")
    print(f"Mortality Rate: {hiv_virus.mortality_rate}")


