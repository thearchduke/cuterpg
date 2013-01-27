import pyglet

###Collision detection!

##will_be_inside is much more useful right now for walls; can_touch probably good for doors & stuff.
def will_be_inside(player, direction, walls):
	collide = False
	if direction == "UP":
		for wall in walls:
			if (player.x + 30) >= wall['x'] and player.x <= (wall['x'] + wall['w']) and (player.y + player.walk_speed) >= (wall['y'] - 20) and player.y <= (wall['y'] + wall['h'] - 10):
				collide = True
	if direction == "DOWN":
		for wall in walls:
			if (player.x + 30) >= wall['x'] and player.x <= (wall['x'] + wall['w']) and player.y >= (wall['y'] - 20) and (player.y - player.walk_speed) <= (wall['y'] + wall['h'] - 10):
				collide = True
	if direction == "LEFT":
		for wall in walls:
			if (player.x + 30) >= wall['x'] and (player.x - player.walk_speed) <= (wall['x'] + wall['w']) and player.y >= (wall['y'] - 20) and player.y <= (wall['y'] + wall['h'] - 10):
				collide = True
	if direction == "RIGHT":
		for wall in walls:
			if (player.x + 30 + player.walk_speed) >= wall['x'] and player.x <= (wall['x'] + wall['w']) and player.y >= (wall['y'] - 20) and player.y <= (wall['y'] + wall['h'] - 10):
				collide = True
	return collide

def is_inside(player, walls):
	collide = False
	for wall in walls:
		if (player.x + 30) >= wall['x'] and player.x <= (wall['x'] + wall['w']) and player.y >= (wall['y'] - 20) and player.y <= (wall['y'] + wall['h'] - 10):
			collide = True
	return collide

def can_touch(player, objects):
	touches = {}
	for item in objects:
		if (player.x + 30) >= wall['x'] and player.x <= (wall['x'] + wall['w']) and (player.y + player.walk_speed) >= (wall['y'] - 20) and player.y <= (wall['y'] + wall['h'] - 10):
			touches = True
		if (player.x + 30) >= wall['x'] and player.x <= (wall['x'] + wall['w']) and player.y >= (wall['y'] - 20) and (player.y - player.walk_speed) <= (wall['y'] + wall['h'] - 10):
			collide = True
		if (player.x + 30) >= wall['x'] and (player.x - player.walk_speed) <= (wall['x'] + wall['w']) and player.y >= (wall['y'] - 20) and player.y <= (wall['y'] + wall['h'] - 10):
			collide = True
		if (player.x + 30 + player.walk_speed) >= wall['x'] and player.x <= (wall['x'] + wall['w']) and player.y >= (wall['y'] - 20) and player.y <= (wall['y'] + wall['h'] - 10):
			collide = True
	return touches
