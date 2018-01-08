import unittest
import ps3
import random


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
room = ps3.EmptyRoom(5,5,20)
for i in range(0,15):
    helper = ps3.Robot(room,1,1)
    print(str(helper), str(helper.get_robot_true_position()))
upperboundscheck = 0
normal_check = 0
err_check = 0
count = 0
err_list = []
while count < 1000:
    count += 1
    helper = ps3.Robot(room,1,1)
    x,y = helper.get_robot_true_position()
    if x > room.width or y > room.height:
        #print(str(helper), str(helper.get_robot_true_position()))
        upperboundscheck += 1
    if x >= 0 and x < room.width +1 and y >= 0 and y < room.height +1:
        normal_check += 1
    else:
        err_list.append(str(x)+', '+str(y))
        err_check += 1
print('Robot creation test')
print('Sims run:', count, 'Upper bounds:', upperboundscheck, 'Errors:',err_check)
print('Error list:', err_list, '\n')

count = 0
normal_check = 0
err_check = 0
err_list = []
while count < 10000:
    pos = room.get_random_position()
    x,y = pos.get_x(), pos.get_y()
    count += 1
    if x >= 0 and x < room.width +1 and y >= 0 and y < room.height +1:
        normal_check += 1
    else:
        err_list.append(str(x)+', '+str(y))
        err_check += 1
print('Random position test')
print('Sims run:', count, 'Good runs:', normal_check, 'Errors:',err_check)
print('Error list:', err_list, '\n')

### start trials on furnished room
room = ps3.FurnishedRoom(5,5,2)
list_furnished = []
room.add_furniture_to_room()

for i in room.tiles.keys():
    # print(i, float(i[0]), float(i[1]))
    x,y = i[0],i[1]
    # print(room.is_tile_furnished(x,y))
    if room.is_tile_furnished(x,y):
        list_furnished.append((x,y)) #(str(x)+', '+ str(y))
print("Furnished tile:\n", room.furniture_tiles)
print("is_tile_furnished:\n", sorted(list_furnished))
check = room.furniture_tiles == sorted(list_furnished)
print('sorted lists match:',check)

### pos trials on furnished room
print('Furniture takes up '+ str(len(list_furnished)) + '/25: ' + str(len(list_furnished)/.25) +'%')
count = 0
for i in range(0,1000):
    pos = room.get_random_position_any() 
    if room.is_position_furnished(pos):
        count += 1
print('Numb of pos inside furniture: ' + str(count) + ' ' + str(count/10) + '%\n')
print('Multiple random rooms:')
for trials in range(0,20):
    count = 0
    width = random.randint(2,7)
    height = random.randint(2,7)
    area = (width +1) * (height + 1)
    room = ps3.FurnishedRoom(width,height,2)
    room.add_furniture_to_room()
    percFurn = (len(room.furniture_tiles)/area) * 100
    percFurn = round(percFurn,1)
    for i in range(0,1000):
        pos = room.get_random_position_any() 
        if room.is_position_furnished(pos):
            count += 1
    percCount = round((count/1000) * 100,1)
    print('Amount furnished: ' + str(percFurn) + '% test: ' + str(percCount))