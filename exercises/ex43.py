# -*- coding: utf-8 -*-

from sys import exit
from random import randint

class Scene(object):
	def enter(self):
		print "아직 만들지 않은 장면입니다. 상속해 enter()를 구현하세요."
		exit(1)

class Engine(object):
	"""docstring for Engine"""
	def __init__(self, scene_map):
		super(Engine, self).__init__()
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		print "play의 첫장면", current_scene
		while True:
			print "\n---------"
			next_scene_name = current_scene.enter()
			print "다음장면", next_scene_name
			current_scene = self.scene_map.next_scene(next_scene_name)
			print "지도에서 받은 새장면", current_scene


class Death(Scene):
	
	quips = [
		"사망, 이거 진짜 못하네요.",
		"어머니가 자랑스러워 하시겠어요... 좀 더 똑똑하셨다면요.",
		"패배자 같으니.",
		"제가 기르는 강아지도 이거보단 잘 해요."
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)


class CentralCorridor(Scene):
	def enter(self):
		print "페르칼 25번 행성의 고던족은 여러분의 우주선에 침략하고 모든 승무원을"
		print "죽였습니다. 당신은 마지막 생존자이며 마지막 임무로 무기고에서 중성자탄을"
		print "가져와 다리에 설치하고 구명정을 타기 전에 우주선을 폭파해야 합니다."
		print "\n"
		print "붉은 비늘 피부, 시커먼 때가 낀 이빨, 증오로 가득 찬 몸에서 물 흐르듯"
		print "이어지는 사악한 광대 복장의 고던인이 뛰쳐 나오는 동안 당신은 중앙"
		print "복도에서 무기고로 내달리고 있습니다. 고던인은 무기고로 가는 문을 가로막고"
		print "당신을 날려버리려 무기를 겨누는 참입니다."

		action = raw_input("> ")

		if action == "발사":
			print "기관종을 발싸"
			return 'laser_weapon_armory'

		elif action == "회피":
			print "도망갑니다."
			return 'death'

		elif action == "농담하기":
			print "농담하기"
			return 'death'

		else:
			print "처리할 수 없습니다."
			return 'central_corridor'

class LaserWeaponArmory(Scene):
	def enter(self):
		print "당신은 무기고로 뛰어 굴러 들어가 쪼르려 앉고 방을 살피며 숨어 있을지도"
		print "모르는 고던인을 찾습니다. 쥐죽은 듯이, 지나치게 조용합니다."
		print "일어서서는 문 건너편으로 달려가 컨테이너에서 중성자탄을 찾습니다."
		print "상자는 비밀번호로 잠겨 있고 폭탄을 꺼내려면 비밀번호를 알아내야만"
		print "합니다. 비밀번호를 10번 틀리면 자물쇠는 영원히 잠기고 폭탄을 꺼낼 수 "
		print "없습니다. 비밀번호는 3자리수입니다."

		code = "%d%d%d" % (randint(1,9), randint(1, 9), randint(1, 9))
		print "hint: ", code

		guess = raw_input("[번호판]>")
		guesses = 0

		while guess != code and guesses < 10:
			print "삐비비빅!!!"
			guesses += 1
			guess = raw_input("[번호판]>")

		if guess == code:
			print "철컥하며 컨테이너가 열리고 틈새로 공기가 새어나옵니다."
			print "중성자탄을 움켜쥐고 가장 빠른 속도로 달립니다."
			return "the_bridge"
		else:
			print "마지막 순간에 자물쇠가 웅웅거리고 기계장치가 엉겨 붙으며 녹아내립니다."
			print "고던 우주선이 당신의 우주선을 날려버려 죽게 됩니다."
			return "death"

class TheBridge(Scene):
	def enter(self):
		print "당신은 팔에 중성자탄을 끼고 다리로 뛰어들어 우주선 조종권을"
		print "빼앗으려던 고던인 5명을 놀라게 합니다. 그 모두가 방금 전에 본"
		print "고던인보다 더 못생긴 광대 복장을 하고 있습니다. 아직 무기를 뽑지는"
		print "않았지만 당신이 팔에 낀 활성화된 폭탄을 보고 터뜨리지 않고 싶어 합니다."

		action = raw_input(">")

		if action == "폰탄 던지기":
			print "당신은 폭탄이 터지면 고던인 모두가 터져 나가리라고 깨달으며 죽습니다."
			return "death"

		elif action == "천천히 폭탄 설치하기":
			print "이제 폭탄은 설치되었고 당신은 이깡통에서 벗어나기 위해 구명정으로"
			print "달려갑니다."
			return 'escape_pod'
		else:
			print "처리할 수 없습니다."
			return 'death'

class EscapePod(Scene):
	def enter(self):
		print "구명정이 5대 있습니다. 몇번을 타시겠습니까?"

		good_pod = randint(1,5)
		guess = raw_input("[구명정 번호]>")

		if int(guess) != good_pod:
			print "%s번 구명정으로 뛰어들어 탈출 단추를 누릅니다." % guess
			print "구명정이 폭발하고 당신의 사지가 여기저기 흩어집니다."
			return 'death'

		else:
			print "%s번 구명정으로 뛰어들어 탈출 단추를 누릅니다." % guess
			print "행성으로 날아가는 동안 뒤돌아 보니 우주선이 파괴되면서 밝은 별처럼"
			print "폭발하고 고던 우주선까지 없애버리는 것을 확인합니다."
			print "You win"
			return 'finished'


class Map(object):
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death' : Death()
	}


	"""docstring for Map"""
	def __init__(self, start_scene):
		super(Map, self).__init__()
		self.start_scene = start_scene
		print "__init__의 start_scene", start_scene
	
	def next_scene(self, scene_name):
		print "next_scene의 start_scene"
		val = Map.scenes.get(scene_name)
		print "next_scene 결과는 ", val
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()