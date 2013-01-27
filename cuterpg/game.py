import pyglet
import draw_tiles

from collision import will_be_inside, is_inside, can_touch

main_batch = pyglet.graphics.Batch()

###Load walking animation sheet for hero
walking = pyglet.image.load('tiles/claudius_crop.png')
walking_seq = pyglet.image.ImageGrid(walking, 4, 5)

map_file = open('map1.txt').read().split()
map_tiles, walls = draw_tiles.render_map(map_file)


class Hero(pyglet.sprite.Sprite):
	def __init__(self):
		super(Hero, self).__init__(walking_seq[0])
		self.batch = main_batch
		self.right_iter = 0
		self.left_iter = 10
		self.up_iter = 5
		self.down_iter = 15
		self.walk_speed = 2.5
		self.walk_iter = .1
		self.scale = 1.3
		self.x = 125
		self.y = 155

	def walk(self, direction):
		if direction == 'RIGHT':
			if will_be_inside(self, direction, walls):
				self.walk_speed = 0
				#self.x -= 5
			self.x += self.walk_speed
			self.right_iter += self.walk_iter
			frame = int(self.right_iter)
			self.image = walking_seq[frame]
			if self.right_iter > 5 - self.walk_iter:
				self.right_iter = 1
		if direction == 'LEFT':
			if will_be_inside(self, direction, walls):
				self.walk_speed = 0
				#self.x += 5
			self.x -= self.walk_speed
			self.left_iter += self.walk_iter
			frame = int(self.left_iter)
			self.image = walking_seq[frame]
			if self.left_iter > 15 - self.walk_iter:
				self.left_iter = 10
		if direction == 'UP':
			if will_be_inside(self, direction, walls):
				self.walk_speed = 0
				#self.y -= 5
			self.y += self.walk_speed
			self.up_iter += self.walk_iter
			frame = int(self.up_iter)
			self.image = walking_seq[frame]
			if self.up_iter > 10 - self.walk_iter:
				self.up_iter = 5
		if direction == 'DOWN':
			if will_be_inside(self, direction, walls):
				self.walk_speed = 0
				#self.y += 5
			self.y -= self.walk_speed
			self.down_iter += self.walk_iter
			frame = int(self.down_iter)
			self.image = walking_seq[frame]
			if self.down_iter > 20 - self.walk_iter:
				self.down_iter = 15




class Game(pyglet.window.Window):
	def __init__(self):
		super(Game, self).__init__()
		self.height = 775
		self.width = 1000
		self.player = Hero()
		self.keys_held = []
		pyglet.clock.schedule_interval(self.movement, 0.015)


	def on_draw(self):
		self.clear()
		draw_tiles.bg_batch.draw()
		main_batch.draw()


	def on_key_press(self, symbol, modifiers):
		self.keys_held.append(symbol)
	def on_key_release(self, symbol, modifiers):
		try:
			self.keys_held.pop(self.keys_held.index(symbol))
		except:
			pass

	def movement(self, dt):
		if pyglet.window.key.UP in self.keys_held:
			self.player.walk('UP')
		if pyglet.window.key.DOWN in self.keys_held:
			self.player.walk('DOWN')
		if pyglet.window.key.LEFT in self.keys_held:
			self.player.walk('LEFT')
		if pyglet.window.key.RIGHT in self.keys_held:
			self.player.walk('RIGHT')
		if pyglet.window.key.LSHIFT in self.keys_held:
			self.player.walk_speed = 4.0
		else:
			self.player.walk_speed = 2.5




if __name__ == "__main__":
	root = Game()
	pyglet.app.run()

