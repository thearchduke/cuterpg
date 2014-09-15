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

def can_touch(player, direction, objects):
	obj = False
	if direction == "UP":
		for o in objects:
			if (player.x + 30) >= o['x'] and player.x <= (o['x'] + o['w']) and (player.y + player.walk_speed) >= (o['y'] - 20) and player.y <= (o['y'] + o['h'] - 10):
				obj = o
	if direction == "DOWN":
		for o in objects:
			if (player.x + 30) >= o['x'] and player.x <= (o['x'] + o['w']) and player.y >= (o['y'] - 20) and (player.y - player.walk_speed) <= (o['y'] + o['h'] - 10):
				obj = o
	if direction == "LEFT":
		for o in objects:
			if (player.x + 30) >= o['x'] and (player.x - player.walk_speed) <= (o['x'] + o['w']) and player.y >= (o['y'] - 20) and player.y <= (o['y'] + o['h'] - 10):
				obj = o
	if direction == "RIGHT":
		for o in objects:
			if (player.x + 30 + player.walk_speed) >= o['x'] and player.x <= (o['x'] + o['w']) and player.y >= (o['y'] - 20) and player.y <= (o['y'] + o['h'] - 10):
				obj = o
	return obj

'''
def can_touch(player, objects):
	touches = {}
	for item in objects:
		if (player.x + 30) >= wall['x'] and player.x <= (wall['x'] + wall['w']) and (player.y + player.walk_speed) >= (wall['y'] - 20) and player.y <= (wall['y'] + wall['h'] - 10):
			touches = True
		if (player.x + 30) >= wall['x'] and player.x <= (wall['x'] + wall['w']) and player.y >= (wall['y'] - 20) and (player.y - player.walk_speed) <= (wall['y'] + wall['h'] - 10):
			touches = True
		if (player.x + 30) >= wall['x'] and (player.x - player.walk_speed) <= (wall['x'] + wall['w']) and player.y >= (wall['y'] - 20) and player.y <= (wall['y'] + wall['h'] - 10):
			touches = True
		if (player.x + 30 + player.walk_speed) >= wall['x'] and player.x <= (wall['x'] + wall['w']) and player.y >= (wall['y'] - 20) and player.y <= (wall['y'] + wall['h'] - 10):
			touches = True
	return touches
'''