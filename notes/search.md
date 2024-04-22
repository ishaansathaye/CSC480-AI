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

## Searching for Solutions
- traversal of the search space
    - from initial to goal
    - legal sequence of actions as defined by successor function
- procedure
    - check for goal state
    - expand the current state
        - determine set of reachable states
        - return failure if set is empty
    - select one from reachable states -> apply evaluation here
    - move to the selected state
- search tree is generated
    - nodes are added as more states are visited

## Search Terminology
- search tree
    - generated as the search spaces is traversed
        - search space is not necessarily a tree, can be a graph
        - tree specifies possible paths through the search space
- expansion of nodes
    - nodes are expanded by applying the successor function -> generates new set of child nodes
    - fringe (frontier): nodes that have not been visited yet
- search strategy
    - determines selection of the next node to be expanded
    - can be achieved by ordering the nodes in the fringe
        - FIFO, LIFO, random, etc.

## Evaluation Criteria
- Completeness
    - if there is a solution, it will be found
- optimality
    - best solution will be found
- time complexity
    - time required to find the solution
    - does not include time to perform actions
- space complexity
    - memory required to find the solution
    - main factors:
        - branching factor b
        - depth d of the shallowest goal node
        - max path length m

## Search Strategies
- uninformed search (blind search)
    - number of steps, path cost unknown
    - agent knows it is at a global only after it reaches a goal
        - goals not visible from a distance
- informed search (heuristic search)
    - agent has background info about the problem
        - map, costs of action
        - hints about the location of the goal
        - evaluating hints can be costly

### Uninformed Search
- breadth-first vs uniform cost search
    - breadth-first: always expands the shallowest node
        - only optimal if all step costs are equal
    - uniform cost: considers the overall path cost
        - optimal for any (reasonable) cost function
            - non-zero, positive
        - gets bogged down in trees with many fruitless, short branches
            - low path cost, but no goal node
    - both are complete for non-extreme problems
        - finite number of branches
        - strictly positive cost function
- depth-first: depth-limited search, iterative deepening
- bidirectional search

### Informed Search
- best-first search
- search with heuristic function
- memory-bounded search
- iterative improvement search

### Other Search Strategies
- Local Search and Optimization
    - hill climbing, simulated annealing, genetic algorithms, constraint
    satisfaction
- search in continuous spaces
- non-deterministic actions
- partial observations
- online search