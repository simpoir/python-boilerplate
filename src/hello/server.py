import bottle


@bottle.route("/")
def index():
    return "python says hello"


def main():
    bottle.run()
