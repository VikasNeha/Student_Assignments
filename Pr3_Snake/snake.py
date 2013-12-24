import random
import math

def createArray(size):
    return [None] * size


def createBoard(rows, cols):
    m = createArray(rows)
    for i in range(rows):
        m[i] = createArray(cols)
    return m


def displayBoard(m):
    rows = len(m)
    cols = len(m[0])
    for r in range(0, rows):
        for c in range(0, cols):
            if m[r][c]:
                print(m[r][c], end=" ")
            else:
                print("_", end=" ")
        print()


def add_random_point_to_snake(Snake, Board):
    valid_points = []
    tail_point = Snake[-1]

    all_four_points = []
    all_four_points.append([tail_point[0], tail_point[1]-1])
    all_four_points.append([tail_point[0], tail_point[1]+1])
    all_four_points.append([tail_point[0]-1, tail_point[1]])
    all_four_points.append([tail_point[0]+1, tail_point[1]])

    # Check Valid Points
    for point in all_four_points:
        if 0 <= point[1] < 30 and 0 <= point[0] < 20 and point not in Snake:
            valid_points.append(point)

    if len(valid_points) == 0:
        Snake.append([-1, -1])
    else:
        Snake.append(random.choice(valid_points))


def move_snake(Snake, Board, Player):
    valid_points = []
    head_point = Snake[0]

    all_eight_points = []
    all_eight_points.append([head_point[0], head_point[1]-1])
    all_eight_points.append([head_point[0], head_point[1]+1])
    all_eight_points.append([head_point[0]-1, head_point[1]])
    all_eight_points.append([head_point[0]+1, head_point[1]])
    all_eight_points.append([head_point[0]-1, head_point[1]-1])
    all_eight_points.append([head_point[0]+1, head_point[1]-1])
    all_eight_points.append([head_point[0]-1, head_point[1]+1])
    all_eight_points.append([head_point[0]+1, head_point[1]+1])

    for point in all_eight_points:
        if 0 <= point[1] < 30 and 0 <= point[0] < 20 and point not in Snake:
            valid_points.append(point)

    if len(valid_points) > 0:
        point_to_move = None
        minDistance = determine_distance([20,30], [0,0])
        for point in valid_points:
            distance = determine_distance(point, Player)
            if distance < minDistance:
                minDistance = distance
                point_to_move = point
        Board[Snake[-1][0]][Snake[-1][1]] = None
        for x in range(0, len(Snake)):
            temp_point = Snake[x]
            Snake[x] = point_to_move
            point_to_move = temp_point
    else:
        Snake.append([-1, -1])


def determine_distance(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]

    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def main():
    Board = createBoard(20, 30)
    Player = [0, 0]
    Snake = [[19, 29], [19, 28], [19, 27]]

    moves_count = 0
    stay_alive_count = 0
    while True:
        Board[Player[0]][Player[1]] = 'i'
        for point in Snake:
            Board[point[0]][point[1]] = 'x'
        displayBoard(Board)
        user_input = input("Enter j to move left, k to move right, i to move up, and m to move down: ")
        if user_input not in ['j', 'k', 'i', 'm']:
            print("Invalid Key Pressed")
            continue
        if user_input == 'j':   # Move Left
            if Player[1] - 1 < 0:
                print("Invalid Move")
            else:
                Board[Player[0]][Player[1]] = None
                Player[1] -= 1
        elif user_input == 'k':   # Move Right
            if Player[1] + 1 >= 30:
                print("Invalid Move")
            else:
                Board[Player[0]][Player[1]] = None
                Player[1] += 1
        elif user_input == 'i':   # Move Up
            if Player[0] - 1 < 0:
                print("Invalid Move")
            else:
                Board[Player[0]][Player[1]] = None
                Player[0] -= 1
        elif user_input == 'm':   # Move Down
            if Player[0] + 1 >= 20:
                print("Invalid Move")
            else:
                Board[Player[0]][Player[1]] = None
                Player[0] += 1

        stay_alive_count += 1

        if Player in Snake:
            print("You touched Snake. You Lost !!!")
            print("You stayed alive for: ", end="")
            print(stay_alive_count)
            break

        moves_count += 1

        if moves_count == 5:
            add_random_point_to_snake(Snake, Board)
            moves_count = 0
        move_snake(Snake, Board, Player)

        if Snake[-1] == [-1, -1]:
            print("Snake Lost")
            break

        if Player in Snake:
            print("Snake touched you. You lost !!!")
            break

if __name__ == "__main__":
    main()