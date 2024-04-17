# Search in AI

## Search as Problem-Solving Strategy
- Problems viewed as reaching a goal from a given starting point
    - state space defines the problem and its possible solutions formally
    - space can be traversed by a successor function (operators)
        - go to one state to the next
- if possible, info about specific problem or the general domain is used to improve the search
    - experience from previous instances of problem
    - strategies expressed as heuristics
    - simpler versions of the problem
    - constraints on certain aspects of the problem

## Problem-Solving Agents
- agents whose task is to solve a particular problem
    - problem formulation
        - possible states of the word relevant to the problem
        - info accessible?
        - progress from state to state?
    - goal formulation
        - important characteristics
        - know it when reached?
        - several possible goal states?
            - equal or some preferred?

## Well-Defined Problems
- problems with a readily available formal specification
    - initial state
        - start state of the problem
    - actions (operators, successor functions)
    - state space
        - set of all possible states reachable from the initial state
    - path
        - sequence of states and operators that lead from initial to goal state
    - goal test
        - determines if a given state is a goal state
    - solution
        - path from initial to goal state
    - search cost
        - time and memory required to calculate the solution
    - path cost
        - expenses of the agent's actions
        - sum of individual costs of actions in a path
    - total cost
        - sum of search and path costs
        - overall cost of the solution

## Selecting States and Actions
- choice of suitable states and operators
    - make the difference between a problem that can be solved and one that cannot be solved
- states describe distinguishable points during problem-solving process
    - dependent on the task and domain
- actions move the agent from one state to another one
