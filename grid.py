from room import Room
import time
import random

# Grid is used to create the 10 x 10 grid that will be passed to


class Grid:
    def __init__(self, capacity=100):
        self.grid = None  # empty array used to track grid
        self.capacity = capacity  # max capacity of rooms
        self.count = 0  # keeps track of each room created
        self.rows = 10  # width of grid
        self.columns = 10  # height of grid
        self.rooms = {}  # Creates rooms on the grid

    # establishes the grid
    def create_grid(self, size_x, size_y, capacity):
        self.grid = [None] * self.rows
        self.rows = size_x
        self.columns = size_y

        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x
        # Start from lower-left corner (0,0)
        x = -1  # (this will become 0 on the first step)
        y = 0
        room_count = 0
        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west
        # While there are rooms to be created...
        previous_room = None
        while room_count < capacity:
            # Calculate the direction of the room to be created
            if direction > 0 and x < size_x - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else:
                # If we hit a wall, turn north and reverse direction
                room_direction = "n"
                y += 1
                direction *= -1

            # Name rooms based on location in the map
            # If it has connections in all directions (n, s, e, w) = "green", "border", and "corner".
            if y == 0 and x == 0 or y == self.columns - 1 and x == 0 or y == 0 and x == self.rows - 1 or x == self.rows - 1 and y == self.columns - 1:
                num = 0
                room = Room(f"Corner{num}", f"Corner of map", room_count, x, y)
                num += 1
            elif x == 0:
                room = Room(f"Southern_Border{y}",
                            f"Border of map", room_count, x, y)
            elif x == self.rows - 1:
                room = Room(f"Northern_Border{y}",
                            f"Border of map", room_count, x, y)
            elif y == self.columns - 1:
                room = Room(f"Eastern_Border{x}",
                            f"Border of map", room_count, x, y)
            elif y == 0:
                room = Room(f"Western_Border{x}",
                            f"Border of map", room_count, x, y)
            else:
                room = Room(f"Green{room_count}",
                            f"Interior of map", room_count, x, y)

            # Save the room in the World grid
            self.grid[x][y] = room
            self.rooms[self.grid[x][y]] = room.name
            # print(self.rooms[0][0])
            # print(room.name)
            # if self.grid[0] == 0:

            # print("\n\n\nName test --> ", room.name, "\n\n\n")
            # Connect the new room to the previous room
            opposite = {"w": "e", "e": "w", "s": "n", "n": "s"}
            if previous_room is not None:
                previous_room.connect_rooms(previous_room, room_direction)
                room.connect_rooms(previous_room, opposite[room_direction])
            # Update iteration variables
            previous_room = room
            room_count += 1

    # attaches each room (use .connect_rooms())

    def attach_rooms(self):
        pass

    # shows if my rooms are connected
    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''

        # Add top border
        str = "# " * ((3 + self.rows * 9) // 2) + "\n"

        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid)  # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            # str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.name}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
        # Add bottom border
        str += "# " * ((3 + self.rows * 9) // 2) + "\n"

        # Print string
        print(str)


# g = Grid()
# num_rooms = 100
# width = 10
# height = 10
# g.create_grid(width, height, num_rooms)

# g.print_rooms()

# print(g)
