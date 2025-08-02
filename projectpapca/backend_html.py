from sqlite3.dbapi2 import paramstyle
from MOJIZA.engine.server import HTML
from MOJIZA.static.make_static import Static
import random

def project_home():

    page = HTML(title_document = "new page for mojiza test")
    page.meta(name="viewport", content="width=device-width, initial-scale=1.0")
    page.link(rel="icon", href=Static("image/Sharingan_Kakashi.png"), type="image/png")
    page.div(h_class="ho").h1("hello")
    list_of_numbers = [i for i in range(100)]
    page.div(h_class="test").p(f"{list_of_numbers}")
    return page.end()




def guess_number_page(method, params):
    # Keep the secret in a module‑level var so it survives reloads
    if not hasattr(guess_number_page, "_secret"):
        guess_number_page._secret = random.randint(1, 100)

    page = HTML(title_document="🎲 Taxmin O'yini")
    page.link(rel="icon", href=Static("image/Sharingan_Kakashi.png"), type="image/png")

    page.meta(name="viewport", content="width=device-width, initial-scale=1.0")
    page.add_styles("""
        body { font-family: Arial, sans-serif; padding: 20px; background: #f7f7f7; }
        .box { max-width: 400px; margin: auto; background: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        input, button { width: 100%; padding: 10px; margin-top: 10px; border-radius: 5px; }
        .msg { margin-top: 20px; font-weight: bold; text-align: center; }
    """)

    box = page.div(h_class="box")

    box.h1("1 dan 100 gacha sonni toping!", align="center")

    # Always render the form:
    form = box.form(action="/GAME", method="POST")
    form.input(type="number", name="guess", placeholder="Son kiriting", required=True, min="1", max="100")
    form.button("Yuborish", type="submit")

    # If it was a POST, check the guess
    if method == "POST":
        raw = params.get("guess", [""])[0]
        print(raw)
        print("PARAMS:",params)
        try:
            guess = int(raw)
            secret = guess_number_page._secret
            print("number of guests:",secret)
            print(raw, guess)

            js_code = '''
             let a = document.querySelector("#idx");
             '''

            if guess < secret:
                msg = "🔼 Kattaroq son kiriting!"
            elif guess > secret:
                msg = "🔽 Kichikroq son kiriting!"
            else:
                msg = f"🎉 To‘g‘ri topdingiz! Son: {secret}"
                # reset for next game
                guess_number_page._secret = random.randint(1, 100)

        except ValueError:
            msg = "❌ Iltimos, butun son kiriting."

        box.div(h_class="msg").p(msg)

    return page.end(AUTHOR="Thony")




# def generate_modern_welcome_page():
#     """
#     🌟 Mojiza Framework - Professional & Interactive Documentation Page
#     Ushbu sahifa Mojiza HTML engineʼdan foydalanishni professional, vizual va interaktiv tarzda bosqichma-bosqich tushuntiradi.
#     """
#
#     page = HTML(
#         title_document="✨ Mojiza Framework – Developer’s Welcome",
#         path="/doc/welcome"
#     )
#     page.link(rel="icon", href=Static("image/logo_modern.png"), type="image/png")
#
#     # ⬛ Advanced Global Styles
#     page.add_styles("""
#     * { margin:0; padding:0; box-sizing:border-box; }
#     html, body { height:100%; scroll-behavior: smooth; background: #fdfdfd; }
#     body { font-family: 'Inter', sans-serif; color:#111; line-height: 1.7; }
#     .block {
#         min-height: 100vh;
#         display: flex;
#         flex-direction: column;
#         justify-content: center;
#         align-items: center;
#         padding: 60px 30px;
#         text-align: center;
#     }
#     .intro { background: linear-gradient(120deg, #0f2027, #203a43, #2c5364); color: white; }
#     .import, .create, .explain, .usage { background: #ffffff; }
#     .footer-block { background: #f4f4f4; }
#     h1 { font-size: 3rem; margin-bottom: 20px; }
#     h2 { font-size: 2rem; margin-top: 1rem; }
#     p { max-width: 800px; font-size: 1.2rem; margin-bottom: 20px; }
#     code {
#         display: block;
#         background: #1e1e1e;
#         color: #00ffc8;
#         text-align: left;
#         padding: 20px;
#         margin-top: 20px;
#         border-radius: 10px;
#         font-family: 'Fira Code', monospace;
#     }
#     a.button {
#         margin-top: 30px;
#         padding: 0.75rem 1.5rem;
#         background: #0052cc;
#         color: white;
#         border-radius: 8px;
#         font-weight: 600;
#         text-decoration: none;
#         transition: all 0.3s ease;
#     }
#     a.button:hover {
#         background: #003d99;
#         box-shadow: 0 4px 12px rgba(0,0,0,0.2);
#     }
#     @media (max-width: 768px) {
#         h1 { font-size: 2rem; }
#         h2 { font-size: 1.5rem; }
#         p { font-size: 1rem; }
#     }
#     """)
#
#     intro = page.div(h_class="block intro")
#     intro.h1("👨‍💻 Mojiza Framework: Welcome Developers!")
#     intro.p("Mojiza — bu HTML sahifalarni Python orqali yaratish uchun ishlab chiqilgan eng yengil va kuchli tizimdir. Quyida siz undan qanday foydalanishni bosqichma-bosqich o‘rganasiz.")
#     intro.a("Get Started Now", href="#import-section", h_class="button")
#
#     imp = page.div(h_class="block import", id="import-section")
#     imp.h1("📦 1. Import qilish")
#     imp.p("Dastlab biz Mojiza Frameworkʼning kerakli modullarini import qilamiz: `HTML` sahifalar yaratish uchun, `Static` esa media fayllar uchun.")
#     imp.code("""from MOJIZA.engine.server import HTML
# from MOJIZA.static.make_static import Static""")
#
#     create = page.div(h_class="block create", id="create-section")
#     create.h1("🛠 2. HTML Sahifa Yaratish")
#     create.p("Endi esa biz HTML sahifa obʼyektini yaratamiz. Unda hujjat sarlavhasi va URL yo‘li belgilanadi.")
#     create.code("""page = HTML(
#     title_document="Mening Mojiza Sahifam",
#     path="/"
# )""")
#
#     explain = page.div(h_class="block explain", id="structure-section")
#     explain.h1("🧱 3. Sahifa Strukturasi")
#     explain.p("Mojiza yordamida HTMLʼning barcha elementlarini Python bilan yaratish mumkin. Quyidagi misol `div`, `h1`, va `p` elementlarini qanday yaratishni ko‘rsatadi.")
#     explain.code("""div = page.div(h_class='container')
# div.h1("Salom Mojiza")
# div.p("Bu Mojiza yordamida yaratilgan paragraf.")""")
#
#     usage = page.div(h_class="block usage", id="usage-section")
#     usage.h1("🧪 4. Foydalanish bo‘yicha misollar")
#     usage.p("Mojiza faqat statik emas, balki dinamik, interaktiv sahifalarni ham yaratishga imkon beradi.")
#
#     for i in range(5, 80):
#         block = page.div(h_class=f"block example-{i}", id=f"example-{i}")
#         block.h2(f"🔹 {i}. Misol: Dinamik HTML generatsiyasi")
#         block.p(f"Siz {i}-blok orqali qanday qilib Python yordamida HTML kodlar yaratish mumkinligini ko‘ryapsiz.")
#         block.code(f"""# {i}-blok uchun kod namunasi
# html = HTML(title_document='Sahifa {i}')
# div = html.div(h_class='demo')
# div.h1('Bu {i}-chi demo sarlavha')
# div.p('Bu sahifa Mojiza yordamida yaratilgan.')""")
#
#     footer = page.div(h_class="block footer-block")
#     footer.h1("✅ Yakuniy Qadam")
#     footer.p("Endi siz Mojiza Frameworkʼda sahifa yaratishni o‘rgandingiz. Endi `page.end()` orqali sahifani yakunlang va uni brauzerda ko‘ring!")
#     footer.code("""return page.end(AUTHOR="Sizning Ismingiz")""")
#     footer.center().p("Mojiza Framework source:")
#     footer.a(
#         "GitHub’da Ko‘rish",
#         href="https://github.com/ABDULHODIY1/MOJIZA_FRAMEWORK-1.0.1",
#         target="_blank",  # yangi oynada ochadi
#         rel="noopener noreferrer",  # xavfsizlik / performance uchun tavsiya etiladi
#         h_class="button"
#     )
#     return page.end(AUTHOR="Muhiddinov Abdulhodiy – Mojiza Dev Team")
from MOJIZA.engine.server import HTML
from MOJIZA.static.make_static import Static

def generate_modern_welcome_page():
    """
    🌟 Mojiza Framework - Professional & Interactive Documentation Page
    Ushbu sahifa Mojiza HTML engineʼdan foydalanishni professional, vizual va interaktiv tarzda bosqichma-bosqich tushuntiradi.
    """

    page = HTML(
        title_document="✨ Mojiza Framework – Developer’s Welcome",
        path="/doc/welcome"
    )
    page.link(rel="icon", href=Static("image/logo_modern.png"), type="image/png")

    # ⬛ Advanced Global Styles
    page.add_styles("""
    * { margin:0; padding:0; box-sizing:border-box; }
    html, body { height:100%; scroll-behavior: smooth; background: #fdfdfd; }
    body { font-family: 'Inter', sans-serif; color:#111; line-height: 1.7; }
    .block {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 60px 30px;
        text-align: center;
    }
    .intro { background: linear-gradient(120deg, #0f2027, #203a43, #2c5364); color: white; }
    .import, .create, .explain, .usage { background: #ffffff; }
    .footer-block { background: #f4f4f4; }
    h1 { font-size: 3rem; margin-bottom: 20px; }
    h2 { font-size: 2rem; margin-top: 1rem; }
    p { max-width: 800px; font-size: 1.2rem; margin-bottom: 20px; }
    code {
        display: block;
        background: #1e1e1e;
        color: #00ffc8;
        text-align: left;
        padding: 20px;
        margin-top: 20px;
        border-radius: 10px;
        font-family: 'Fira Code', monospace;
    }
    a.button {
        margin-top: 30px;
        padding: 0.75rem 1.5rem;
        background: #0052cc;
        color: white;
        border-radius: 8px;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    a.button:hover {
        background: #003d99;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    @media (max-width: 768px) {
        h1 { font-size: 2rem; }
        h2 { font-size: 1.5rem; }
        p { font-size: 1rem; }
    }
    """)

    intro = page.div(h_class="block intro")
    intro.h1("👨‍💻 Mojiza Framework: Welcome Developers!")
    intro.p("Mojiza — bu HTML sahifalarni Python orqali yaratish uchun ishlab chiqilgan eng yengil va kuchli tizimdir. Quyida siz undan qanday foydalanishni bosqichma-bosqich o‘rganasiz.")
    intro.a("Get Started Now", href="#import-section", h_class="button")

    imp = page.div(h_class="block import", id="import-section")
    imp.h1("📦 1. Ornatish")
    imp.p(
        "Dastlab biz Mojiza Frameworkʼning kerakli modullarini oornatib olamiz""")
    imp.code("""pip install mojiza==0.1.3b1 """)


    imp = page.div(h_class="block import", id="import-section")
    imp.h1("📦 2. Import qilish")
    imp.p("Dastlab biz Mojiza Frameworkʼning kerakli modullarini import qilamiz: `HTML` sahifalar yaratish uchun, `Static` esa media fayllar uchun.")
    imp.code("""from MOJIZA.engine.server import HTML
from MOJIZA.static.make_static import Static""")

    create = page.div(h_class="block create", id="create-section")
    create.h1("🛠 3. HTML Sahifa Yaratish")
    create.p("Endi esa biz HTML sahifa obʼyektini yaratamiz. Unda hujjat sarlavhasi va URL yo‘li belgilanadi.")
    create.code("""page = HTML(
    title_document="Mening Mojiza Sahifam",
    path="/"
)""")

    explain = page.div(h_class="block explain", id="structure-section")
    explain.h1("🧱 4. Sahifa Strukturasi")
    explain.p("Mojiza yordamida HTMLʼning barcha elementlarini Python bilan yaratish mumkin. Quyidagi misol `div`, `h1`, va `p` elementlarini qanday yaratishni ko‘rsatadi.")
    explain.code("""div = page.div(h_class='container')
div.h1("Salom Mojiza")
div.p("Bu Mojiza yordamida yaratilgan paragraf.")""")

    usage = page.div(h_class="block usage", id="usage-section")
    usage.h1("🧪 5. Foydalanish bo‘yicha misollar")
    usage.p("Mojiza faqat statik emas, balki dinamik, interaktiv sahifalarni ham yaratishga imkon beradi.")

    # 1000+ qatordan kam bo‘lmasligi uchun 200+ blok generatsiyasi
    for i in range(5, 6):
        block = page.div(h_class=f"block example-{i}", id=f"example-{i}")
        block.h2(f"🔹 {i}. Misol: Dinamik HTML generatsiyasi")
        block.p(f"Siz {i}-blok orqali qanday qilib Python yordamida HTML kodlar yaratish mumkinligini ko‘ryapsiz. Har bir blok o‘ziga xos bo‘lib, real holatlarda qo‘llanishi mumkin.")
        block.code(f"""# {i}-blok uchun kod namunasi
html = HTML(title_document='Sahifa {i}')
div = html.div(h_class='demo')
div.h1('Bu {i}-chi demo sarlavha')
div.p('Bu sahifa Mojiza yordamida yaratilgan.')""")

    footer = page.div(h_class="block footer-block")
    footer.h1("✅ Yakuniy Qadam")
    footer.p("Endi siz Mojiza Frameworkʼda sahifa yaratishni o‘rgandingiz. Endi `page.end()` orqali sahifani yakunlang va uni brauzerda ko‘ring!")
    footer.code("""return page.end(AUTHOR="Sizning Ismingiz")""")
    footer.center().p("Mojiza Framework source:")
    footer.a(
        "GitHub’da Ko‘rish",
        href="https://github.com/ABDULHODIY1/MOJIZA_FRAMEWORK-1.0.1",
        target="_blank",  # yangi oynada ochadi
        rel="noopener noreferrer",  # xavfsizlik / performance uchun tavsiya etiladi
        h_class="button"
    )

    return page.end(AUTHOR="Muhiddinov Abdulhodiy – Mojiza Dev Team")
