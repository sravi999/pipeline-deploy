import flask

app=flask.Flask(__name__)

class App(object):

    def home(self):
        return "Welcome to flask from docker instance"

    def test(self):
        return "test page"

    def details(self):
        return "Details page"

view=App()
app.add_url_rule("/", view_func=view.home, methods=['GET'])
app.add_url_rule("/test", view_func=view.test, methods=['GET'])
app.add_url_rule("/details", view_func=view.details, methods=['GET'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
