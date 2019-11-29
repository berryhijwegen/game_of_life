from World import *

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1
        #TODO: Do something to evolve the generation
        """
        REGELS:
        Elke levende cel met minder dan twee levende buren gaat dood (ook wel onderpopulatie of exposure genaamd);
        Elke levende cel met meer dan drie levende buren gaat dood (ook wel overpopulatie of overcrowding genaamd);
        Elke cel met twee of drie levende buren overleeft, onveranderd naar de volgende generatie (survival);
        Elke dode cel met precies drie levende buren komt tot leven (ook wel geboorte of birth genaamd).

        """

        self.update_cells()
        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world

    def update_cells(self):
        for row in range(self.world.height):
            for column in range(self.world.width):
                self.update_cell(row,column)
                
    def update_cell(self, row, column):
        alive_neighbours_n = self.world.get_number_of_alive_neighbours(row,column)
        alive = True if self.world.get_state(row,column) >= 1 else False

        if alive and (alive_neighbours_n < 2 or alive_neighbours_n > 3):
            self.world.set_state(row, column, 0)

        if not alive and alive_neighbours_n == 3:
            self.world.set_state(row, column, 1)