# -*- coding:utf-8 -*-

import web
from gothonweb import map

# make debugging false
# web.config.debug = False

urls = (
	'/', 'Index',
	'/hello', 'Hello',
	'/game', 'GameEngine',
	'/count', 'Count',
	'/reset', 'Reset'
)

app = web.application(urls, globals())

"""
> 웹 어플리케이션의 특정 지점에서는 사용자 정보 일부를 추적하고 사용자의 웹 브라우저와 연결해야 한다. 사용자의 요청 하나하나가 다른 요청과 독립적이라는 뜻으로, 웹은 (HTTP 때문에) 흔히 '상태가 없다(stateless)'고 이야기 한다.
> A 페이지를 요청하고 자료를 조금 넣어 B페이지로 가는 링크를 누르면 A페이지로 보냈던 모든 자료는 그냥 사라진다.
> 이문제를 해결하려면 각 브라우저 마다 유일한 숫자를 매겨 브라우저가 무엇을 하는지 추적하는 조그만 자료 저장소(store)(보통 데이터베이스나 디스크)를 만들면 된다.
"""

# 디버그 모드에서 세션을 쓸 수 있도록 해주는 해킹
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, initializer={'room': None, 'count':0})
	web.config._session = session
else:
	session = web.config._session

# Template setting
render = web.template.render('templates/', base='layout')

class Index:
	def GET(self):
		form = web.input(name="아무개")
		greeting = "Hello %s!" % form.name

		# session 초기화
		session.room = map.START

		# return greeting
		return render.index(greeting = greeting)

class Hello:
	def GET(self):
		return render.hello_form()

	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s" % (form.greet, form.name)
		return render.index(greeting = greeting)

class GameEngine(object):
	def GET(self):
		if session.room:
			return render.show_room(room=session.room)
		else:
			return render.you_died()

	def POST(self):
		form = web.input(action=None)

		# todo: 여기에 버그가 있음
		if session.room and form.action:
			session.room = session.room.go(form.action)

		web.seeother("/game")

class Count:
	def GET(self):
		session.count += 1
		return str(session.count)

class Reset:
	def GET(self):
		session.kill()
		web.seeother("/count")
		return ''					

if __name__ == "__main__":
	app.run()	