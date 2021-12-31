from Functions import Functions

function = Functions()


def test_selecionar_categoria_tecnologia_celulares_e_telefones():
    option = 'Celulares e Telefones'
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu('Tecnologia')
    function.select_option_menu(option)
    title_expected = f'{option} no Mercado Livre Brasil'
    assert title_expected == function.get_title_page(title_expected)



def test_selecionar_categoria_tecnologia_celulares_e_smartphones():
    option = 'Celulares e Smartphones'
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu('Tecnologia')
    function.select_option_menu(option)
    title_expected = f'{option.split(" ")[0]} | MercadoLivre.com.br'
    assert title_expected == function.get_title_page(title_expected)


def test_selecionar_categoria_tecnologia_acessorios_celulares():
    option = 'Acessórios para Celulares'
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu('Tecnologia')
    function.select_option_menu(option)
    title_expected = f'{option} | MercadoLivre.com.br'
    assert title_expected == function.get_title_page(title_expected)


def test_selecionar_categoria_tecnologia_informatica():
    option = 'Informática'
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu('Tecnologia')
    function.select_option_menu(option)
    title_expected = f'{option} no Mercado Livre Brasil'
    assert title_expected == function.get_title_page(title_expected)


def test_selecionar_categoria_tecnologia_componentes_pc():
    option = 'Componentes para PC'
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu('Tecnologia')
    function.select_option_menu(option)
    title_expected = f'{option} | MercadoLivre.com.br'
    assert title_expected == function.get_title_page(title_expected)


def test_selecionar_categoria_tecnologia_impressao():
    option = 'Impressão'
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu('Tecnologia')
    function.select_option_menu(option)
    title_expected = f'{option} | MercadoLivre.com.br'
    assert title_expected == function.get_title_page(title_expected)


def test_selecionar_categoria_tecnologia_acessorios_notebook():
    option = 'Acessórios para Notebook'
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu('Tecnologia')
    function.select_option_menu(option)
    title_expected = f'{option} | MercadoLivre.com.br'
    assert title_expected == function.get_title_page(title_expected)


def test_selecionar_categoria_tecnologia_conectividade_redes():
    option = 'Conectividade e Redes'
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu('Tecnologia')
    function.select_option_menu(option)
    title_expected = f'{option} | MercadoLivre.com.br'
    assert title_expected == function.get_title_page(title_expected)


def test_selecionar_categoria_tecnologia_cameras_acessorios():
    option = 'Câmeras e Acessórios'
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu('Tecnologia')
    function.select_option_menu(option)
    title_expected = f'{option} | MercadoLivre.com.br'
    assert title_expected == function.get_title_page(title_expected)


def test_selecionar_categoria_tecnologia_acessorios_cameras():
    option = 'Acessórios para Câmeras'
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu('Tecnologia')
    function.select_option_menu(option)
    title_expected = f'{option} | MercadoLivre.com.br'
    assert title_expected == function.get_title_page(title_expected)


def test_selecionar_categoria_tecnologia_cameras():
    option = 'Câmeras'
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu('Tecnologia')
    function.select_option_menu(option)
    title_expected = f'{option} | MercadoLivre.com.br'
    assert title_expected == function.get_title_page(title_expected)


def test_selecionar_categoria_tecnologia_eletronica_audio_video():
    option = 'Eletrônicos, Áudio e Vídeo'
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu('Tecnologia')
    function.select_option_menu(option)
    title_expected = f'{option} | MercadoLivre.com.br'
    assert title_expected == function.get_title_page(title_expected)


def test_selecionar_categoria_tecnologia_acessorios_audio_video():
    option = 'Acessórios para Áudio e Vídeo'
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu('Tecnologia')
    function.select_option_menu(option)
    title_expected = f'{option} | MercadoLivre.com.br'
    assert title_expected == function.get_title_page(title_expected)


def test_selecionar_categoria_tecnologia_audio_portatil_acessorios():
    option = 'Áudio Portátil e Acessórios'
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu('Tecnologia')
    function.select_option_menu(option)
    title_expected = f'{option} | MercadoLivre.com.br'
    assert title_expected == function.get_title_page(title_expected)

