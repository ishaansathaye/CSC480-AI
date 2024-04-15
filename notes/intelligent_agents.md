# Intelligent Agents


## Motivation
- Agents require essential skills to perform tasks that require intelligence
    - Provide a consistent viewpoint on various topics in AI

## What is an Agent?
- entity that interacts with its environment
    - perception through sensors
    - actions through effectors or actuators

## Agents and Environments
- agent perceives its env through sensors
    - percept - complete set of inputs at a given time
    - sequence of percepts - or current percept influence the actions of an agent
- can change the env through actuators
    - op. involving actuator is an action
    - actions can be grouped in action sequences

## Agents and their Actions
- Rational Agent - does the right thing
    - action that leads to best outcome under given circumstances
- Agent Function - maps percept sequences to actions
    - abstract mathematical description
- Agent Program - concrete implementation of respective function
    - runs on a specific agent architecture ("platform")

## Rationality - depends on 4 factors
- Performance measure
    - defines success
- Agent prior knowledge
- Agent possible actions
- Agent's sequence of percepts
    - defines current state of knowledge

## Performance of Agents
- Goals vs Outcome
- Expenses of the agent
    - resource consumption
    - time
- should be objective
- task dependent
- time may be important

## PEAS Description of Task Environments
- Performance Measures
- Environment
- Actuators - actions that agent can perform
- Sensors - info about current state of env.

## Environment Properties
- Fully vs partially observable
- Deterministic vs stochastic
- Episodic vs Sequential
- Static vs Dynamic
- Discrete vs Continuous
- Single vs Multiple agents

## Environment Programs (architecture)
- env simulators for experiments with agents
    - gives percept to an agent
    - receives an action
    - updates the env

## Types of Agents

### Simple reflex agents
- selects action based on current percept only
- can be implemented with condition-action rules
- function

### Model-based reflex agents
- agent has internal state, saving previous actions
- sensor model describes the state of the world in terms of percepts

### Goal-based agents
- goal info is needed to find appropriate actions
- search techniques help find actions, given goal information

### Utility-based agents
- uses a model of the world to evaluate actions
- uses utility function to measure preferences among world states

### Learning agents
- agent may start in an unknown environment
- learns as it operates
    - increases its own knowledge

### Software agents
- referred to as soft bots
- live in artificial environments where computers and networks provide infrastructure
- may be complex with strong requirements on the agent
    - e.g. world wide web, real time constraints
- natural and artificial environments may be merged
    - user interaction
    - sensors and actuators in the real world
