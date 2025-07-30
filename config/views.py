from MOJIZA.engine.server import HTML

# Views will be written manually
def homepage():

    page = HTML(title_document="welcome mojiza")
    page.link(rel="icon", href="/static/favicon.ico", type="image/x-icon")
    page.center().h1("welcome to mojiza config app")

    return page.end()