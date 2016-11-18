# -*- coding:utf-8 -*-
# Unit test using nosetests

class Room(object):
	"""docstring for Room"""
	def __init__(self, name, description):
		super(Room, self).__init__()
		self.name = name
		self.description = description
		self.paths = {}
	
	def go(self, direction):
		return self.paths.get(direction, None)

	def add_paths(self, paths):
		self.paths.update(paths)

central_corridor = Room('Central Corridor', 
"""
페르칼 25번 행성의 고던족은 여러분의 우주선에 침략하고 모든 승무원을 죽엿습니다. 당신은 마지막 생존자이며 마지막 임무로 무기고에서 중성자ㅏㄴ을 가져와 다리에 설치하고 구명정에 타기 전에 우주선을 폭파해야 합니다.
"""
)

laser_weapon_armory = Room('Laser Weapon Armory', 'laser laser laser')

the_bridge = Room('The Bridge', 'go go go')

escape_pod = Room('Escape Pod', 'help me~~~~~')

the_end_winner = Room('The End', 'You win!! Good Job!!')

the_end_loser = Room('The End', 'Lose!!')

escape_pod.add_paths({
	'2': the_end_winner,
	'*': the_end_loser
	})

generic_death = Room('death', 'You died.')

the_bridge.add_paths({
	'폭탄던지기': generic_death,
	'천천히 폭탄 설치하기': escape_pod	
	})

laser_weapon_armory.add_paths({
	'0132': the_bridge,
	'*': generic_death
	})

central_corridor.add_paths({
	'발사': generic_death,
	'회피': generic_death,
	'농담하기': laser_weapon_armory
	})

START = central_corridor