import pyglet

map_file = open('map.txt').read().split()

dirt = pyglet.image.load('tiles/Dirt Block.png')
brown = pyglet.image.load('tiles/Brown Block.png')
grass = pyglet.image.load('tiles/Grass Block.png')
stone = pyglet.image.load('tiles/Stone Block.png')
water = pyglet.image.load('tiles/Water Block.png')

bg_batch = pyglet.graphics.Batch()

line1 = pyglet.graphics.OrderedGroup(1)
line2 = pyglet.graphics.OrderedGroup(2)
line3 = pyglet.graphics.OrderedGroup(3)
line4 = pyglet.graphics.OrderedGroup(4)
line5 = pyglet.graphics.OrderedGroup(5)
line6 = pyglet.graphics.OrderedGroup(6)
line7 = pyglet.graphics.OrderedGroup(7)
line8 = pyglet.graphics.OrderedGroup(8)


def render_map(map):
	walls = []
	map_sprites = []
	tile_y = 509
	for line in map:
		tile_x = 0
		for char in line:
			new_tile = which_tile(char, tile_x, tile_y, walls)
			map_sprites.append(new_tile)
			tile_x += 100
		tile_y -= 84
	return map_sprites, walls

def which_tile(char, tile_x, tile_y, walls):
	if char == 'B':
		new_tile = pyglet.sprite.Sprite(brown, batch = bg_batch, x=tile_x, y=tile_y)
		new_tile = which_line(new_tile, 509, 84)
		return new_tile
	elif char == 'D':
		new_tile = pyglet.sprite.Sprite(dirt, batch = bg_batch, x=tile_x, y=tile_y)
		new_tile = which_line(new_tile, 509, 84)
		return new_tile
	elif char == 'G':
		new_tile = pyglet.sprite.Sprite(grass, batch = bg_batch, x=tile_x, y=tile_y)
		new_tile = which_line(new_tile, 509, 84)
		return new_tile
	elif char == 'S':
		new_tile = pyglet.sprite.Sprite(stone, batch = bg_batch, x=tile_x, y=tile_y)
		new_tile = which_line(new_tile, 509, 84)
		return new_tile
	elif char == 'W':
		walls.append({'x': tile_x, 'y': tile_y + 41, 'h': 84, 'w': 84})
		new_tile = pyglet.sprite.Sprite(water, batch = bg_batch, x=tile_x, y=tile_y)
		new_tile = which_line(new_tile, 509, 84)
		return new_tile




def which_line(s, height, dist):
	if s.y == height - dist*0:
		s.group = line1
	if s.y == height - dist*1:
		s.group = line2
	if s.y == height - dist*2:
		s.group = line3
	if s.y == height - dist*3:
		s.group = line4
	if s.y == height - dist*4:
		s.group = line5
	if s.y == height - dist*5:
		s.group = line6
	if s.y == height - dist*6:
		s.group = line7
	if s.y == height - dist*7:
		s.group = line8
	return s



map_tiles, walls = render_map(map_file)



if __name__ == "__main__":
	root = Game()
	pyglet.app.run()
