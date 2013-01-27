import pyglet

map_file = open('map.txt').read().split()

dirt = pyglet.image.load('tiles/Dirt Block.png')
brown = pyglet.image.load('tiles/Brown Block.png')

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
	map_sprites = []
	tile_y = 509
	for line in map:
		tile_x = 0
		for char in line:
			if char == 'B':
				new_tile = pyglet.sprite.Sprite(brown, batch = bg_batch, x=tile_x, y=tile_y)
				new_tile = which_line(new_tile, 509, 86)
				map_sprites.append(new_tile)
			elif char == 'D':
				new_tile = pyglet.sprite.Sprite(dirt, batch = bg_batch, x=tile_x, y=tile_y)
				new_tile = which_line(new_tile, 509, 86)
				map_sprites.append(new_tile)
			tile_x += 100
		tile_y -= 86
	return map_sprites


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


map_tiles = render_map(map_file)

class Game(pyglet.window.Window):
	def __init__(self):
		super(Game, self).__init__()
		self.height = 680
		self.width = 1000

	def on_draw(self):
		self.clear()
		bg_batch.draw()


if __name__ == "__main__":
	root = Game()
	pyglet.app.run()
