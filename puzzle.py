player_position = [1,3,6,8] #[black1, b;acl2, white1, white2]
finish_position = [6,8,1,3]
direction = {1:7,2:6,3:4,4:8,5:1,6:5,7:3,8:2}
step = 0
player_index = 0

while player_position != finish_position:
	next_place = player_position[player_index]
	player_position[player_index] = direction[next_place]

	if player_position[player_index] == finish_position[player_index]:
		player_index += 1

	step += 1

print('step taken:', step)