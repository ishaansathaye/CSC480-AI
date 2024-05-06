import argparse

map = {
    'Western Australia': ['Northern Territory', 'South Australia'],
    'Northern Territory': ['Western Australia', 'South Australia', 'Queensland'],
    'South Australia': ['Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Victoria'],
    'Queensland': ['Northern Territory', 'South Australia', 'New South Wales'],
    'New South Wales': ['Queensland', 'South Australia', 'Victoria'],
    'Victoria': ['South Australia', 'New South Wales'],
    'Tasmania': []
}

colors = ['Red', 'Green', 'Blue']

def is_safe(state, color, coloring):
    for neighbor in map[state]:
        if coloring.get(neighbor) == color:
            return False
    return True

# Generator function to recursively assign colors to regions
def color_regions(state_index, coloring):
    if state_index == len(map):
        yield coloring
    else:
        region = list(map.keys())[state_index]
        for color in colors:
            if is_safe(region, color, coloring):
                coloring[region] = color
                yield from color_regions(state_index + 1, coloring.copy())
                coloring.pop(region)

def main():
    parser = argparse.ArgumentParser(description='Map Coloring')
    parser.add_argument('--all', action='store_true', help='Show all solutions')
    args = parser.parse_args()

    coloring = {}
    solutions = list(color_regions(0, coloring))

    if args.all:
        if solutions:
            print("All solutions:")
            for idx, solution in enumerate(solutions, start=1):
                print(f"Solution {idx}:")
                for state, color in solution.items():
                    print(f"    {state}: {color}")
            print(f"Total solutions: {len(solutions)}")
        else:
            print("No solution found")
    else:
        if solutions:
            print("First solution found:")
            for state, color in solutions[0].items():
                print(f"    {state}: {color}")
            print(f"Total solutions: {len(solutions)}")
        else:
            print("No solution found")

if __name__ == "__main__":
    main()
    