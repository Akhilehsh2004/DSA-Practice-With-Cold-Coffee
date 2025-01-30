def robotSim(commands, obstacles):
    # Directions: North, East, South, West
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0  # Initial position
    direction = 0  # Initially facing North
    max_distance = 0

    # Convert obstacles to a set for quick lookup
    obstacle_set = set(map(tuple, obstacles))

    for command in commands:
        if command == -2:  # Turn left
            direction = (direction - 1) % 4
        elif command == -1:  # Turn right
            direction = (direction + 1) % 4
        else:  # Move forward k steps
            dx, dy = directions[direction]
            for _ in range(command):
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in obstacle_set:  # Hit an obstacle
                    break
                x, y = next_x, next_y
                max_distance = max(max_distance, x**2 + y**2)

    return max_distance

# Example usage:
commands = [4, -1, 3]
obstacles = []
print(robotSim(commands, obstacles))  # Output: 25

commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]
print(robotSim(commands, obstacles))  # Output: 65