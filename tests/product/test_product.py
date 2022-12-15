from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        10,
        "Chocolate",
        "Nestle",
        "2022-10-10",
        "2023-11-11",
        "58489491",
        "Local fresco",
    )

    assert type(product.id) is int
    assert type(product.nome_do_produto) is str
    assert type(product.nome_da_empresa) is str
    assert type(product.data_de_fabricacao) is str
    assert type(product.data_de_validade) is str
    assert type(product.numero_de_serie) is str
    assert type(product.instrucoes_de_armazenamento) is str
