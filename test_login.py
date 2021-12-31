from Functions import Functions

function = Functions()


def test_login():
    function.access_page()
    function.access_login()
    function.set_user_login()
    function.click_btn_continuar()
    function.set_password_login()
    function.click_btn_entrar()
