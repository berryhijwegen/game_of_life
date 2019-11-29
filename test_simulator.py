import unittest
from Simulator import *


class TestSimulator(unittest.TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self):
        self.sim = Simulator()

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        self.assertIsInstance(self.sim.update(), World)

    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)

    def test_update_cell(self):
        # using default "B3/S23"

        # check if birth, survival numbers are valid
        [self.assertLessEqual(num, 8) and self.assertGreaterEqual(num,0) for num in self.sim.birth]
        [self.assertLessEqual(num, 8) and self.assertGreaterEqual(num,0) for num in self.sim.survival]
        
        test_cell = [1,1]
        cells_around_test_cell = [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]

        cases = {}
                
        for num in self.sim.survival:
            cases[num] = 'unchanged'
        
        for num in self.sim.birth:
            cases[num] = '1'


        for number in cases.keys():
            self.setUp()
            count = 0

            for cell in cells_around_test_cell:
                self.sim.world.set_state(*cell,1)
                count+=1
                if count == number:
                    if cases[number] == 'unchanged':
                        prev = self.sim.world.get_state(*test_cell)
                        self.sim.update_cell(*test_cell)
                        self.assertEqual(self.sim.world.get_state(*test_cell), prev)
                    else:
                        self.sim.update_cell(*test_cell)
                        self.assertEqual(self.sim.world.get_state(*test_cell), 1)
                    break

if __name__ == '__main__':
    unittest.main()