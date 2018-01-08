import unittest
import ps3


print('Creating 5x5 room')
room = ps3.RectangularRoom(5,5,20)
print('get_dirt_amopunt(1,3)',room.get_dirt_amount(1,3))
print('get_num_cleaned_tiles',room.get_num_cleaned_tiles())
print('is_tile_cleaned(1,3)',room.is_tile_cleaned(1,3))
botpos = ps3.Position(1,3)
room.clean_tile_at_position(botpos,15)
print('1,3 after 15 cleaning (5)', room.is_tile_cleaned(1,3),room.get_dirt_amount(1,3))
room.clean_tile_at_position(botpos,5)
print('1,3 after 5 more cleaning (0)',room.is_tile_cleaned(1,3))
room.clean_tile_at_position(botpos,5)
print('1,3 after 5 more cleaning (-5)',room.is_tile_cleaned(1,3))

# create robot
for i in range(0,15):
    helper = ps3.Robot(room,1,1)
    print(str(helper), str(helper.get_robot_true_position()))
j = 0
check = False
while check == False:
    j += 1
    helper = ps3.Robot(room,1,1)
    x,y = helper.get_robot_true_position()
    if x > room.width or y > room.height:
        print(str(helper), str(helper.get_robot_true_position()))
        print(j)
        check = True