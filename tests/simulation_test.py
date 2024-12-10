import unittest
from simulation import Simulation
from virus import Virus

class TestSimulation(unittest.TestCase):
    def test_initialization(self):
        """Tests and initialization of the Simulation class."""
        virus = Virus("Sniffles", 0.5, 0.12)
        sim = Simulation(1000, 0.05, virus, 50)
        self.assertEqual(sim.pop_size, 1000)
        self.assertEqual(sim.vacc_percentage, 0.05)
        self.assertEqual(sim.virus.name, "Sniffles")
        self.assertEqual(sim.virus.repro_rate, 0.5)
        self.assertEqual(sim.virus.mortality_rate, 0.12)
        self.assertEqual(sim.initial_infected, 50)

if __name__ == "__main__":
    unittest.main()