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