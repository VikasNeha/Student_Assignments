def move_snake(Snake):
    point_to_move = [0, 0]
    for x in range(0, len(Snake)):
        temp_point = Snake[x]
        Snake[x] = point_to_move
        point_to_move = temp_point

Snake = [[0, 3], [0, 2], [0, 1]]
move_snake(Snake)
print(Snake)


















































