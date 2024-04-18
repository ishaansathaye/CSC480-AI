from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.visualization.modules import CanvasGrid, TextElement
from mesa.visualization.ModularVisualization import ModularServer
from mesa.datacollection import DataCollector
import random

PLACEHOLDER_POS = (0, 0)

class AgentCounter(TextElement):
    def __init__(self):
        pass

    def render(self, model):
        prey_count = sum(isinstance(agent, Prey) for agent in model.schedule.agents)
        predator_count = sum(isinstance(agent, Predator) for agent in model.schedule.agents)
        caveman_count = sum(isinstance(agent, Caveman) for agent in model.schedule.agents)
        return f"Prey: {prey_count}, Predators: {predator_count}, Cavemen: {caveman_count}"

class Caveman(Agent):
    '''Cavemen eat predators and breed when they have enough energy. They lose energy every step.'''
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.energy = 100

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def eat(self):
        predator_neighbors = self.model.grid.get_cell_list_contents(
            [self.pos]
        )
        predator_agents = [agent for agent in predator_neighbors if isinstance(agent, Predator)]
        if predator_agents:
            predator_to_eat = random.choice(predator_agents)
            self.model.grid.remove_agent(predator_to_eat)
            self.model.schedule.remove(predator_to_eat)
            self.energy += 75

    def breed(self):
        if self.energy >= 200:
            self.energy -= 100
            new_caveman = Caveman(self.model.next_id(), self.model)
            self.model.grid.place_agent(new_caveman, PLACEHOLDER_POS)
            self.model.grid.move_to_empty(new_caveman)
            self.model.schedule.add(new_caveman)

    def step(self):
        self.move()
        self.eat()
        self.breed()
        self.energy -= 1

class Prey(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.energy = 100

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def eat(self):
        self.energy += 10

    def breed(self):
        if self.energy >= 200:
            self.energy -= 100
            new_prey = Prey(self.model.next_id(), self.model)
            self.model.grid.place_agent(new_prey, PLACEHOLDER_POS)
            self.model.grid.move_to_empty(new_prey)            
            self.model.schedule.add(new_prey)

    def step(self):
        if self.pos == None:
            return
        self.move()
        self.breed()
        self.energy -= 1

class Predator(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.energy = 100

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def eat(self):
        prey_neighbors = self.model.grid.get_cell_list_contents(
            [self.pos]
        )
        prey_agents = [agent for agent in prey_neighbors if isinstance(agent, Prey)]
        if prey_agents:
            prey_to_eat = random.choice(prey_agents)
            self.model.grid.remove_agent(prey_to_eat)
            self.model.schedule.remove(prey_to_eat)
            self.energy += 100

    def breed(self):
        if self.energy >= 200:
            self.energy -= 100
            new_predator = Predator(self.model.next_id(), self.model)
            self.model.grid.place_agent(new_predator, PLACEHOLDER_POS)
            self.model.grid.move_to_empty(new_predator)
            self.model.schedule.add(new_predator)

    def step(self):
        if self.pos == None:
            return
        self.move()
        self.eat()
        self.breed()
        self.energy -= 1

class PreyPredatorModel(Model):
    def __init__(self, height, width, prey_count, predator_count, caveman_count):
        super().__init__()
        self.height = height
        self.width = width
        self.grid = MultiGrid(height, width, torus=True)
        self.schedule = RandomActivation(self)
        self.running = True

        for i in range(prey_count):
            prey = Prey(self.next_id(), self)
            self.grid.place_agent(prey, PLACEHOLDER_POS)
            self.grid.move_to_empty(prey)
            self.schedule.add(prey)

        for i in range(predator_count):
            predator = Predator(self.next_id(), self)
            self.grid.place_agent(predator, PLACEHOLDER_POS)
            self.grid.move_to_empty(predator)            
            self.schedule.add(predator)

        for i in range(caveman_count):
            caveman = Caveman(self.next_id(), self)
            self.grid.place_agent(caveman, PLACEHOLDER_POS)
            self.grid.move_to_empty(caveman)
            self.schedule.add(caveman)

        # Data collector for collecting agent counts
        self.datacollector = DataCollector(
            model_reporters={"Prey": lambda m: sum(isinstance(agent, Prey) for agent in m.schedule.agents),
                             "Predators": lambda m: sum(isinstance(agent, Predator) for agent in m.schedule.agents),
                             "Cavemen": lambda m: sum(isinstance(agent, Caveman) for agent in m.schedule.agents)}
        )

    def step(self):
        prey_count = sum(isinstance(agent, Prey) for agent in self.schedule.agents)
        predator_count = sum(isinstance(agent, Predator) for agent in self.schedule.agents)
        caveman_count = sum(isinstance(agent, Caveman) for agent in self.schedule.agents)

        if prey_count == 0:
            if predator_count > 0:
                self.remove_predator()
            elif caveman_count > 0:
                self.remove_caveman()

        self.schedule.step()

    def remove_predator(self):
        '''Predators die if there are no more prey'''
        predator_agents = [agent for agent in self.schedule.agents if isinstance(agent, Predator)]
        if predator_agents:
            predator_to_remove = random.choice(predator_agents)
            self.grid.remove_agent(predator_to_remove)
            self.schedule.remove(predator_to_remove)

    def remove_caveman(self):
        '''Cavemen food source is predators, so they die if there are no more predators'''
        caveman_agents = [agent for agent in self.schedule.agents if isinstance(agent, Caveman)]
        if caveman_agents:
            caveman_to_remove = random.choice(caveman_agents)
            self.grid.remove_agent(caveman_to_remove)
            self.schedule.remove(caveman_to_remove)

model = PreyPredatorModel(height=10, width=10, prey_count=50, predator_count=10, caveman_count=5)

for i in range(75):
    model.step()
    
    # Print population counts
    prey_count = sum(isinstance(agent, Prey) for agent in model.schedule.agents)
    predator_count = sum(isinstance(agent, Predator) for agent in model.schedule.agents)
    caveman_count = sum(isinstance(agent, Caveman) for agent in model.schedule.agents)
    print(f"Step {i}: Prey={prey_count}, Predators={predator_count}, Cavemen={caveman_count}")

def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "Layer": 0, "r": 0.5}
    if isinstance(agent, Prey):
        portrayal["Color"] = "green"
    elif isinstance(agent, Predator):
        portrayal["Color"] = "red"
    elif isinstance(agent, Caveman):
        portrayal["Color"] = "black"
    return portrayal

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

server = ModularServer(PreyPredatorModel,
                       [grid, AgentCounter()],
                       "Prey-Predator-Caveman Model",
                       {"height": 10, "width": 10, "prey_count": 50,
                        "predator_count": 10, "caveman_count": 5})

server.port = 8521
server.launch()
