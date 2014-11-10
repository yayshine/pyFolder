import web

urls = (
	'/hello', 'index'
	)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class index(object):
	def GET(self):
		return render.hello_form()

	def POST(self):
		form = web.input(greet="Hai", name="Yay", image={})
		if not form.greet:
			form.greet = "Hello"
		if not form.name:
			form.name = "Yay"
		greeting = "%s %s" % (form.greet, form.name)

		filedir = '/Users/yay/Desktop/pyFolder/projects/gothonweb/static'
		if not form.image.filename:
			filename="golden gate.jpg"
		else:
			filename=form.image.filename.replace('\\','/').split('/')[-1]
			fout = open(filedir + '/' + filename, 'w')
			fout.write(form.image.file.read())
			fout.close()
		return render.index(greeting= greeting, filename=filename)

if __name__ == "__main__":
	app.run()