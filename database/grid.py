from database.room import Room

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

## N/S ROOMS
        # self.grid = None  # empty array used to track grid
        # self.capacity = capacity  # max capacity of rooms
        # self.count = 0  # keeps track of each room created
        # # self.rows = 10  # width of grid
        # # self.columns = 10  # height of grid
        # self.rooms = {}  # Creates rooms on the grid

    # establishes the grid
    # def create_grid(self, size_x, size_y, capacity):
    def create_grid(self, size_x, size_y, capacity=100):
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
        corner = 0  # used for giving corner a unique name
        inside = 0  # used for giving interior a unique name
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
            room = Room(f"Passage{x}", f"This is the only way", room_count)
            # If it has connections in all directions (n, s, e, w) = "green", "border", and "corner".
            if y == 0 and x == 0 or y == self.columns - 1 and x == 0 or y == 0 and x == self.rows - 1 or x == self.rows - 1 and y == self.columns - 1:
                room = Room(f"Corner{corner}",
                            f"Corner of map", room_count, x, y)
                corner += 1
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
                room = Room(f"Green{inside}",
                            f"Interior of map", room_count, x, y)
                inside += 1

            # Save the room in the World grid
            self.grid[x][y] = room
            self.rooms[self.grid[x][y]] = room
            # print(self.rooms[0][0])
            # print(room.name)
            # print("previous", previous_room)
            # print("\n\n\nName test --> ", room.name, "\n\n\n")
            # Connect the new room to the previous room
            opposite = {"w": "e", "e": "w", "s": "n", "n": "s"}
            if previous_room is not None:
                previous_room.connect_rooms(room, room_direction)
                room.connect_rooms(previous_room, opposite[room_direction])
            # Update iteration variables
            previous_room = room
            # print(room.name ,"Connects to ---> ", previous_room.name)
            room_count += 1

### N/S ROOMS
        # # self.grid = [None] * self.rows
        # self.grid = [None] * self.capacity
        # # self.rows = size_x
        # # self.columns = size_y

        # # for i in range(len(self.grid)):
        # #     self.grid[i] = [None] * size_x
        # # Start from lower-left corner (0,0)
        # x = -1  # (this will become 0 on the first step)
        # y = 0
        # room_count = 0
        # # Start generating rooms to the east
        # direction = 1  # 1: east, -1: west
        # # While there are rooms to be created...
        # corner = 0  # used for giving corner a unique name
        # inside = 0  # used for giving interior a unique name
        # previous_room = None
        # while room_count <= capacity - 1:
        #     # Calculate the direction of the room to be created
        #     if x < self.capacity:
        #         room_direction = "n"
        #         x += 1
        #     # elif direction < 0 and x > 0:
        #     #     room_direction = "w"
        #     #     x -= 1
        #     # else:
        #     #     # If we hit a wall, turn north and reverse direction
        #     #     room_direction = "n"
        #     #     y += 1
        #     #     direction *= -1

        #     # Name rooms based on location in the map
        #     room = Room(f"Passage{x}", f"This is the only way", room_count)
        #     # If it has connections in all directions (n, s, e, w) = "green", "border", and "corner".
        #     # if y == 0 and x == 0 or y == self.columns - 1 and x == 0 or y == 0 and x == self.rows - 1 or x == self.rows - 1 and y == self.columns - 1:
        #     #     room = Room(f"Corner{corner}",
        #     #                 f"Corner of map", room_count, x, y)
        #     #     corner += 1
        #     # elif x == 0:
        #     #     room = Room(f"Southern_Border{y}",
        #     #                 f"Border of map", room_count, x, y)
        #     # elif x == self.rows - 1:
        #     #     room = Room(f"Northern_Border{y}",
        #     #                 f"Border of map", room_count, x, y)
        #     # elif y == self.columns - 1:
        #     #     room = Room(f"Eastern_Border{x}",
        #     #                 f"Border of map", room_count, x, y)
        #     # elif y == 0:
        #     #     room = Room(f"Western_Border{x}",
        #     #                 f"Border of map", room_count, x, y)
        #     # else:
        #     #     room = Room(f"Green{inside}",
        #     #                 f"Interior of map", room_count, x, y)
        #     #     inside += 1

        #     # Save the room in the World grid
        #     self.grid[x] = room
        #     # self.grid[x][y] = room
        #     self.rooms[self.grid[x]] = room
        #     # self.rooms[self.grid[x][y]] = room
        #     # print(self.rooms[0][0])
        #     # print(room.name)
        #     # if self.grid[0] == 0:
        #     # print("previous", previous_room)
        #     # print("\n\n\nName test --> ", room.name, "\n\n\n")
        #     # Connect the new room to the previous room
        #     # opposite = {"w": "e", "e": "w", "s": "n", "n": "s"}
        #     if previous_room is not None:
        #         previous_room.connect_rooms(room, "n")
        #         # previous_room.connect_rooms(room, direction)
        #         room.connect_rooms(previous_room, "s")
        #         # room.connect_rooms(previous_room, opposite[room_direction])
        #     # Update iteration variables
        #     previous_room = room
        #     # print(room.name ,"Connects to ---> ", previous_room.name)
        #     room_count += 1
### END OF N/S ROOMS
    
    # attaches each room (use .connect_rooms())
    def attach_rooms(self, grid):
        dirs = ['n_to', 'e_to', 's_to', 'w_to']
        grid_list = list(self.grid)
        print(grid_list)

               
        # for row in list(self.grid):
        #     print(row.room)

        # while x

        # shows if my rooms are connected

    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''

        # Add top border
        str = "# "
        str = "# " * ((3 + self.rows * 9) // 2) + "\n"
        # print("Grid", self.grid)

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
            str += "#"
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


g = Grid()
num_rooms = 100
width = 10
height = 10
g.create_grid(width, height, num_rooms)
# g.print_rooms()
# for i in g.rooms:
#     a = i.name
#     b = i.n_to
#     if b is None:
#         print("NONE")
#     else:
#         print(f"Room: {i.name} ----> {i.n_to.name}")
        


# print(g.rooms.name)
# g.attach_rooms(g)
# g.print_rooms()

