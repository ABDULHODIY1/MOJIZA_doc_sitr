from MOJIZA.engine.routing import PAGE
from projectpapca.views import fullpage, newpage, login_view, guess_number_page,project_home, generate_modern_welcome_page

base_urls = "/"  # localhost:8000/papca
space_name = "home"


@PAGE('/')
def home_view(method, params):
    return fullpage()

@PAGE('/forpage')
def new_page_view(method, params):
    return newpage()

@PAGE('/home')
def login(method, params):
    return login_view()

@PAGE('/GAME')
def guess_number(method, params):
    return guess_number_page(method, params)

@PAGE("/fullpage")
def hame_s(method, params):
    return project_home()

@PAGE('/doc')
def doc(method, params):
    return generate_modern_welcome_page()


# @PAGE('/test')
# def test(method, params):
#     return test()