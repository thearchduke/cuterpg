import pyglet


###Landscape tiles
dirt = pyglet.image.load('cuterpg/tiles/Dirt Block.png')
brown = pyglet.image.load('cuterpg/tiles/Brown Block.png')
grass = pyglet.image.load('cuterpg/tiles/Grass Block.png')
stone = pyglet.image.load('cuterpg/tiles/Stone Block.png')
water = pyglet.image.load('cuterpg/tiles/Water Block.png')
talltree = pyglet.image.load('cuterpg/tiles/Tree Tall.png')
shorttree = pyglet.image.load('cuterpg/tiles/Tree Short.png')


###Building tiles
roofsouth = pyglet.image.load('cuterpg/tiles/Roof South.png')
roofsouthwest = pyglet.image.load('cuterpg/tiles/Roof South West.png')
doorclosed = pyglet.image.load('cuterpg/tiles/Door Tall Closed.png')
dooropen = pyglet.image.load('cuterpg/tiles/Door Tall Open.png')
stonetall = pyglet.image.load('cuterpg/tiles/Stone Block Tall.png')


###Object tiles
chestclosed = pyglet.image.load('cuterpg/tiles/Chest Closed.png')

bg_batch = pyglet.graphics.Batch()

line1 = pyglet.graphics.OrderedGroup(1)
line2 = pyglet.graphics.OrderedGroup(2)
line3 = pyglet.graphics.OrderedGroup(3)
line4 = pyglet.graphics.OrderedGroup(4)
line5 = pyglet.graphics.OrderedGroup(5)
line6 = pyglet.graphics.OrderedGroup(6)
line7 = pyglet.graphics.OrderedGroup(7)
line8 = pyglet.graphics.OrderedGroup(8)
line9 = pyglet.graphics.OrderedGroup(9)
line10 = pyglet.graphics.OrderedGroup(10)
line11 = pyglet.graphics.OrderedGroup(11)
line12 = pyglet.graphics.OrderedGroup(12)
line13 = pyglet.graphics.OrderedGroup(13)
line14 = pyglet.graphics.OrderedGroup(14)
line15 = pyglet.graphics.OrderedGroup(15)
line16 = pyglet.graphics.OrderedGroup(16)
line17 = pyglet.graphics.OrderedGroup(17)
line18 = pyglet.graphics.OrderedGroup(18)
line19 = pyglet.graphics.OrderedGroup(19)
line20 = pyglet.graphics.OrderedGroup(20)
line21 = pyglet.graphics.OrderedGroup(21)


def render_map(map):
	walls = []
	objects = []
	map_sprites = []
	chests = []
	tile_y = 509
	layer = 1
	for line in map:
		tile_x = 0
		for char in line:
			new_tile = which_tile(char, tile_x, tile_y, walls, layer, objects)
			map_sprites.append(new_tile)
			tile_x += 100
		tile_y -= 84
		layer += 1
		if tile_y < 5:
			tile_y = 509
	return map_sprites, walls, objects

def which_tile(char, tile_x, tile_y, walls, layer, objects):
	if char == 'B':
		new_tile = pyglet.sprite.Sprite(brown, batch = bg_batch, x=tile_x, y=tile_y)
		new_tile = which_line(new_tile, 509, 84, layer)
		return new_tile
	elif char == 'D':
		new_tile = pyglet.sprite.Sprite(dirt, batch = bg_batch, x=tile_x, y=tile_y)
		new_tile = which_line(new_tile, 509, 84, layer)
		return new_tile
	elif char == 'G':
		new_tile = pyglet.sprite.Sprite(grass, batch = bg_batch, x=tile_x, y=tile_y)
		new_tile = which_line(new_tile, 509, 84, layer)
		return new_tile
	elif char == 'S':
		new_tile = pyglet.sprite.Sprite(stone, batch = bg_batch, x=tile_x, y=tile_y)
		new_tile = which_line(new_tile, 509, 84, layer)
		return new_tile
	elif char == 'W':
		walls.append({'x': tile_x, 'y': tile_y + 41, 'h': 84, 'w': 84})
		new_tile = pyglet.sprite.Sprite(water, batch = bg_batch, x=tile_x, y=tile_y)
		new_tile = which_line(new_tile, 509, 84, layer)
		return new_tile
	elif char == 'T':
		walls.append({'x': tile_x, 'y': tile_y + 41, 'h': 84, 'w': 84})
		new_tile = pyglet.sprite.Sprite(talltree, batch = bg_batch, x=tile_x, y=tile_y)
		new_tile = which_line(new_tile, 509, 84, layer)
		return new_tile
	elif char == 't':
		walls.append({'x': tile_x, 'y': tile_y + 41, 'h': 84, 'w': 84})
		new_tile = pyglet.sprite.Sprite(shorttree, batch = bg_batch, x=tile_x, y=tile_y + 20)
		new_tile = which_line(new_tile, 509, 84, layer)
		return new_tile
	elif char == 'R':
		walls.append({'x': tile_x, 'y': tile_y + 41, 'h': 84, 'w': 84})
		new_tile = pyglet.sprite.Sprite(roofsouth, batch = bg_batch, x=tile_x, y=tile_y)
		new_tile = which_line(new_tile, 509, 84, layer)
		return new_tile
	elif char == 'l':
		walls.append({'x': tile_x, 'y': tile_y + 41, 'h': 84, 'w': 84})
		new_tile = pyglet.sprite.Sprite(roofsouthwest, batch = bg_batch, x=tile_x, y=tile_y)
		new_tile = which_line(new_tile, 509, 84, layer)
		return new_tile
	elif char == 'O':
		objects.append({'x': tile_x, 'y': tile_y + 20, 'h': 84, 'w': 84, 'type': 'doorclosed'})
		walls.append({'x': tile_x, 'y': tile_y + 20, 'h': 84, 'w': 84})
		new_tile = pyglet.sprite.Sprite(doorclosed, batch = bg_batch, x=tile_x, y=tile_y)
		new_tile = which_line(new_tile, 509, 84, layer)
		return new_tile
	elif char == 's':
		walls.append({'x': tile_x, 'y': tile_y, 'h': 84, 'w': 84})
		new_tile = pyglet.sprite.Sprite(stonetall, batch = bg_batch, x=tile_x, y=tile_y)
		new_tile = which_line(new_tile, 509, 84, layer)
		return new_tile
	elif char == 'C':
		objects.append({'x': tile_x, 'y': tile_y + 41, 'h': 21, 'w': 84, 'type': 'chestclosed'})
		walls.append({'x': tile_x, 'y': tile_y + 41, 'h': 21, 'w': 84})
		new_tile = pyglet.sprite.Sprite(chestclosed, batch = bg_batch, x=tile_x + 14, y=tile_y - 42)
		new_tile = which_line(new_tile, 509, 84, layer)
		new_tile.scale = 0.75
		return new_tile




def which_line(s, height, dist, layer):
	if s.y == height - dist*0:
		if layer == 1:
			s.group = line1
		if layer == 8:
			s.group = line8
		if layer == 15:
			s.group = line15
	if s.y == height - dist*1:
		if layer == 2:
			s.group = line2
		if layer == 9:
			s.group = line9
		if layer == 16:
			s.group = line16
	if s.y == height - dist*2:
		if layer == 3:
			s.group = line3
		if layer == 10:
			s.group = line10
		if layer == 17:
			s.group = line17
	if s.y == height - dist*3:
		if layer == 4:
			s.group = line4
		if layer == 11:
			s.group = line11
		if layer == 18:
			s.group = line18
	if s.y == height - dist*4:
		if layer == 5:
			s.group = line5
		if layer == 12:
			s.group = line12
		if layer == 19:
			s.group = line19
	if s.y == height - dist*5:
		if layer == 6:
			s.group = line6
		if layer == 13:
			s.group = line13
		if layer == 20:
			s.group = line20
	if s.y == height - dist*6:
		if layer == 7:
			s.group = line7
		if layer == 14:
			s.group = line14
		if layer == 21:
			s.group = line21
	return s


if __name__ == "__main__":
	root = Game()
	pyglet.app.run()
