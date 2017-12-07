import pygameimport GameFiles.EngineScripts.Time as Timefrom GameFiles.EngineScripts.ContinueMover import ContinueMoverfrom GameFiles.EngineScripts.GameObject import GameObjectfrom GameFiles.EngineScripts.HitBox import HitBoxfrom GameFiles.EngineScripts.Vector2 import Vector2class Froger(GameObject):	def on_enter(self, other_game_object):		if other_game_object == ContinueMover:			self.on_log = True			self.difference = self.lead_vertex - other_game_object.lead_vertex			self.log_speed = other_game_object.speed	def on_exit(self, other_game_object):		pass	def __init__(self, game_display, main_class):		super().__init__(game_display)		# Vector2's		self.lead_vertex = Vector2(500, 500)		self.size = Vector2(20, 20)		self.difference = Vector2()		# Hitbox		self.hitbox = HitBox(self, self.lead_vertex, self.size)		# Main class		self.main_class_link = main_class		# Color		self.color = (0, 255, 0)		# Booleans		self.button_down = False		self.on_log = False		# Integers		self.speed = 100		self.direction = 0		self.log_speed = -1	def update(self):		# Loops through the list of events that have happened.		for event in self.main_class_link.event_list:			if event.type == pygame.KEYDOWN:				if event.key == pygame.K_UP:					self.button_down = True					self.direction = 0				elif event.key == pygame.K_LEFT:					self.button_down = True					self.direction = 1				elif event.key == pygame.K_RIGHT:					self.button_down = True					self.direction = 2			elif event.type == pygame.KEYUP:				if event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:					self.button_down = False		# Checks to see if a button is down, and if so, to move Froger in that direction.		if self.button_down:			if self.direction == 0:				self.lead_vertex.y -= self.speed * Time.deltaTime			elif self.direction == 1:				self.lead_vertex.x -= self.speed * Time.deltaTime			elif self.direction == 2:				self.lead_vertex.x += self.speed * Time.deltaTime		if self.on_log:		super().render()