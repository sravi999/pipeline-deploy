import flask

app=flask.Flask(__name__)

class App(object):

    def home(self):

        return "Welcome to flask"

view=App()
app.add_url_rule("/", view_func=view.home, methods=['GET'])
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
