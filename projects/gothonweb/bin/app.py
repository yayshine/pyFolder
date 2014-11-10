import web
from gothonweb import map

urls = (
	'/game', 'GameEngine',
	'/', 'Index',
	)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, initializer={'room': None})
	web.config._session = session
else:
	session = web.config._session

render = web.template.render('templates/', base="layout")


class Index(object):
	def GET(self):
		# this is used to "setup" the session with starting values
		session.room = map.START
		web.seeother("/game")


class GameEngine(object):

	def GET(self):
		if session.room:
			return render.show_room(room=session.room)
		else:
			return render.play_again()

	def POST(self):
		form = web.input(action=None)
		# when you have written an answer
		if session.room and form.action:
			# if the answer is not on the answer sheet, you die
			if session.room.go(form.action) == None:
				form.action = '*'
			session.room = session.room.go(form.action)
		# when you didn't put anything for the answer, you die
		elif session.room:
			session.room = session.room.go('*')

		web.seeother("/game")

if __name__ == "__main__":
	app.run()