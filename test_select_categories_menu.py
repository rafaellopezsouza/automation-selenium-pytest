import time

from Functions import Functions

function = Functions()
format_title = 'no Mercado Livre Brasil'


def test_selecionar_categoria_veiculos():
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu('Veículos')
    title_expected = f'Carros, Motos e Outros {format_title}'
    assert title_expected == function.get_title_page(title_expected)


def test_selecionar_categoria_supermercado():
    option = 'Supermercado'
    function.access_page()
    function.mouse_over_menu('Categorias')
    function.select_option_menu(option)
    title_expected = f'{option} {format_title}'
    assert title_expected == function.get_title_page(title_expected)


"""
Casa e Móveis
Eletrodomésticos
Esportes e Fitness
Ferramentas
Construção
Indústria e Comércio
Saúde
Acessórios para Veículos
Beleza e Cuidado Pessoal
Moda
Bebês
Brinquedos
Imóveis
Compra Internacional
Produtos Sustentaveis
Lojas oficiais
Ver mais categorias
"""
